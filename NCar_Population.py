#Controller of the population, the generations and the selection
import NCar
import NCar_Visualization

import numpy as np
import time

from random import uniform


class Population():

    def __init__(self):

        self.population_size = 10
        self.population = []

        self.generations = 0



    def selection(self):

        best_recorded_fitness = 0
        best_recorded_car = None

        #Find the car with the highest fitness
        for car in self.population:
            if car.fitness > best_recorded_fitness:
                best_recorded_fitness = car.fitness
                best_recorded_car = car

        #Create new cars
        self.create_new_generation(best_recorded_car)


    #Fix the training of the weights to a more sientific solution
    def create_new_generation(self, best_car):
        new_population = []

        for _ in range(self.population_size):
            synaptic_delta = np.array((5,1)) * uniform(-0.05, 0.05)

            new_population.append(NCar.Neural_Network(best_car.synaptic_weights + synaptic_delta))

        self.population = new_population
        self.generations += 1



    def first_setup_generations(self):

        #new seeds for every synaptic weight so that no weights are the same
        for i in range(self.population_size):
            np.random.seed(i)
            new_synaptic_weights = 2 * np.random.random((5,1)) - 1

            new_car = NCar.Neural_Network(new_synaptic_weights)
            self.population.append(new_car)        



    def check_cars(self):
        for i in range(self.population_size):

            #If any of the cars hasn't crashed yet then return true and continue training
            if self.population[i].crashed == False:
                return True

        #If all the cars have crashed then return false
        return False