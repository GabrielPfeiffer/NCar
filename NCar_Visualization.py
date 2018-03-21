#This program is a visualization of the python-based program NCar
#This program doesn´t controll any of the neural networks or the genetic algorithm
#The cars are controlled by their neural networks any purely visualized here

from NCar_Population import Population as Pop



#Fix everythin related to pocessing-python mode
def setup():
    '''size(800, 800)'''
    Pop().first_setup_generations()
    

    
#Fix everythin related to pocessing-python mode
def draw():
    '''background(0)'''

    #If there are any cars left that hasn't crashed then update them
    if Pop().check_cars() == True:
        for i in Pop().population:
            Pop().population[i].update() #Check for collision somehow
            display_car(Pop().population[i])
    
    #If all the car has crashed then start the selection process to get a new generation
    elif Pop().check_cars() == False:
        Pop().selection()

    #print an error
    else:
        print("Error: no returned value from 'check_cars()'!")



def display_track():
    print("Track ins't curently being shown")



def display_car(car_to_display):
    
    distance_lines_range = 100

    '''

    translate(car_to_display.position[0], car_to_display.position[1])
    push_matrix()

    rotate(car_to_display.rotation) 

    rectMode(CENTER)
    rect(0, 0, 10, 20)

    #left line
    line(0, 0, -distance_lines_range, 0)

    #left forward line
    line(0, 0, -distance_lines_range, -distance_lines_range)

    #forward line
    line(0, 0, 0, -distance_lines_range)

    #right line
    line(0, 0, distance_lines_range, 0)

    #right forward line
    line(0, 0, distance_lines_range, -distance_lines_range)


    pop_matrix()
    
    '''