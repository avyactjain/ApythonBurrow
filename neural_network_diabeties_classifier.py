from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy
import matplotlib.pyplot as plt


numpy.random.seed(7)

#load data
dataset = numpy.loadtxt("pima-indians-diabetes.csv",delimiter =",")
#Split data into input and output

X = dataset[:,0:8] #0 to 7 columns are inputs
Y = dataset[:,8] #8th column is the output
# print(dataset)

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size = 0.2, random_state = 42)


model = Sequential() #We are creating a sequential model, that means i will define each layer as i move accross

#I will have multiple hidden layer in this network.

model.add(Dense(12, input_dim = 8, activation = 'relu')) #Created the first layer(0 layer) of the network. it is essentially the input. it has 12 Neurons, each has 8 dimensions. No. of neurons can be changed(I guess).
model.add(Dense(15,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(10,activation= 'relu'))
model.add(Dense(1,activation= 'sigmoid')) #Sigmoid, because sigmoid function maps to probability. hence used sigmoid in the last layer. in this case last layer would only have 1 neuron. because its only 1 value. either true or false. 0 or 1


#Compile the model, mimize loss function using gradient descent method. 
model.compile(loss ='binary_crossentropy', optimizer="adam",metrics=['accuracy'])
#'adam' is a part of keras. it is used to optimize the weights to minimize the error
#Train the model. fit data in.
model.fit(x_train,y_train,epochs= 1000, batch_size= 10, validation_data=(x_test,y_test))

model.save('weights.h5')

xnew = numpy.array([[6,143,68,29,0,29.7,0.345,43]])
        
ynew = model.predict_proba(xnew)

print(ynew)

