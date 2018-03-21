#This is the python-program controlling the genetic algorithm that trains the neural networks
#Most of this will not be a typical neural network
#The think-function will probobly be the only one who gets used and the weights gets shifted after fitness etc...

import numpy as np


class Neural_Network():
    
    
    def __init__(self, synaptic_weights_):

        #the weights is the way that the neural network thinks
        self.synaptic_weights = synaptic_weights_
        
        #Is the car still alive? otherwise don't spend time on updating it
        self.crashed = False

        #How well does the car performe? this will later be the populations selection
        self.fitness = 0

        #where is it? this will be used to move it and to check if it is on the track
        self.position = [0,0]

        #rotate the car when displaying it (just for the visualization)
        self.rotation = 0
        


    def nonlin(self, x, deriv=False):
        if(deriv == True):
            return x * (1-x)
        return 1 / (1 + np.exp(-x))


    #The training part might not be used so it is commented out at the moment
    '''
    def train(self, train_set_inputs, train_set_outputs, iterations):

        for j in range(iterations):

            if j % (iterations / 100) == 0:
                print (int((j / iterations) * 100), "%")

            l0 = train_set_inputs
            l1 = self.nonlin(np.dot(l0, self.synaptic_weights))

            l1_error = train_set_outputs - l1
            l1_delta = l1_error * self.nonlin(l1, True)

            self.synaptic_weights += np.dot(l0.T, l1_delta)

        print ("Done training")
    '''


    def turn(self, degrees_to_turn):
        print("rotated ", degrees_to_turn, " degrees")
        '''rotate(degrees_to_turn)'''



    def think(self, inputs):
        #return self.nonlin(np.dot(inputs, self.synaptic_weights))
        self.turn(self.nonlin(np.dot(inputs, self.synaptic_weights)))


    #This will be called every frame to update the car
    def update(self):
        #Measure distancess

        self.think('''input the measurements as a np.array''')

        