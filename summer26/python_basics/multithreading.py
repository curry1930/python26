# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function) 
# this does multiple tasks concurently (this is more like multitasking)

import threading
import time


def walk_dog(first_name, last_name):
    time.sleep(8)
    print("You finished walking dog")

def take_out_trash():
    time.sleep(5)
    print("You took out trash")

def get_milk():
    time.sleep(2)
    print("You took milk")


walk_dog()                       # running these functions will separetely run the outputs 
take_out_trash()                 # for eg. walkdog for 8 sec then after 8 sec takeouttrash that will 
get_milk()                       # take 5 sec then getmilk that will take 2 sec
                                 # this means it took 8+5+2 sec to run the whole things 

# but when using multithreading the commands run simultaneously 
chore1 = threading.Thread(target=walk_dog, args=("scooby", "doo"))
chore1.start()              

chore2 = threading.Thread(target=take_out_trash)
chore2.start()   

chore3 = threading.Thread(target=get_milk)
chore3.start() 

chore1.join()                 # this joins all the chores and then print the last msg 
chore2.join()                 # ie u completed all the chores if we dont use join it will
chore3.join()                 # first print the all chores are completed then the acutall chores

print("All chores are completed")