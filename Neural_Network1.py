import numpy as np

def sigmoid(x, deriv = False): #Sigmoid Function, it maps every value to a value between 0-1
    if (deriv == True):
        return x*(1-x);
    else:
        return 1/(1+np.exp(-x))
    

#Input Data 
X = np.array([[0,0,1], 
              [0,1,1],
              [1,0,1],
              [1,1,1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

#np.random.seed(1) #So that I get the same random numbers everytime I run my program

#Randomly initializing the synapse matrics

syn0 = 2*np.random.random((3,4)) - 1 
syn1 = 2*np.random.random((4,1)) - 1


for j in range(60000):
    
    #Feed forward through layers 0,1,2
    l0 = X #First layer of neural network is the inputs
    l1 = sigmoid(np.dot(l0,syn0)) #Second layer of the neural network
    l2 = sigmoid(np.dot(l1,syn1)) #Third Layer of the neural network
    
    l2_error = y - l2 #how much did we miss the target(Actual) value
    
    if(j%10000) == 0:
        print("Error : " + str(np.mean(np.abs(l2_error))))
    
    l2_delta = l2_error * sigmoid(l2, deriv = True)
    
    #Backpropagation
    l1_error = l2_delta.dot(syn1.T)
    
    l1_delta = l1_error * sigmoid(l1, deriv = True)
    
    #Update the weights 
    
    syn1 = syn1 + l1.T.dot(l2_delta)
    syn0 = syn0 + l0.T.dot(l1_delta)

print(l2)  