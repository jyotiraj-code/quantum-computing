#We will train a circuit to model a sine function

#Imports
import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt


#Creating the training data

X = np.linspace(0, 2*np.pi, 5) #5 input datapoints 0 and 2pi
#Telling the optimizer that this is not a parameter but an input datapoint

X.requires_grad = False
Y = np.sin(X) #The output  for the input datapoints

#Creating the test data
#Shifted from the training data by 0.2
X_test = np.linspace(0.2, 2*np.pi + 0.2, 5)
Y_test = np.sin(X_test) #Outputs for test datapoints

#Creating the Device (1 qubit = 1 wires)
dev = qml.device('default.qubit', wires=1)

#Creating the Quantum Circuit
@qml.qnode(dev)

def quantum_circuit(datapoint, params):
    #Encoding the data as an RX rotation
    qml.RX(datapoint, wires=0)

    #Create rotation based on the angles in "params"
    qml.Rot(params[0], params[1], params[2], wires=0)

    #Return the expected value along the Z axis after measurement
    return qml.expval(qml.PauliZ(wires = 0))

#Creating Loss Function

def loss_func(predictions):

    total_losses = 0

    for i in range(len(Y)):
        output = Y[i]
        prediction = predictions[i]
        loss = (prediction - output)**2
        total_losses += loss
    return total_losses


#Creating Cost Function

def cost_func(params):

    predictions = [quantum_circuit(x, params) for x in X]

    cost = loss_func(predictions)

    return cost

#Defining the Optimizer
opt = qml.GradientDescentOptimizer(stepsize=0.3)

params = np.array([0.1,0.1,0.1], requires_grad = True)

for i in range(100):
    
    params, prev_cost = opt.step_and_cost(cost_func, params)

    if i%10 == 0:
        print(f"Cost at step {i} is {cost_func(params)}")



#Test and graph the results
test_predictions = []
for x_test in X_test:
    prediction = quantum_circuit(x_test, params)
    test_predictions.append(prediction)

fig = plt.figure()
ax1 = fig.add_subplot(111)


ax1.scatter(X, Y, s=30, c='b', marker="s", label='Train outputs')
ax1.scatter(X_test,Y_test, s=60, c='r', marker="o", label='Test outputs')
ax1.scatter(X_test,test_predictions, s=30, c='k', marker="x", label='Test predicitons')
plt.xlabel("Inputs")
plt.ylabel("Outputs")
plt.title("QML results")

plt.legend(loc='upper right');
plt.show()