# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25

@author: Paul
"""


import random, operator

#external libary
import  matplotlib.pyplot

agents = [] 

# Set Up Varibles
#agent 1
"""
y0 = random.randint(0,99)
x0 = random.randint(0,99)
#agent 2
y1 = random.randint(0,99)
x1 = random.randint(0,99)

agents.append([y0,x0])
"""

#Testing the creation of the container
#print(agents)


#End of page 2 code. Condense the varibles

#agent 2


#Randomises the y,x starting location of agent1
agents.append([random.randint(0,99),random.randint(0,99)])
#Randomises the y,x starting location of agent2
agents.append([random.randint(0,99),random.randint(0,99)])



print ("Start postion for agent 1 is - y " + str(agents[0][0]) + " x " + str(agents[0][1]))
print ("Start postion for agent 2 is - y " + str(agents[1][0]) + " x " + str(agents[1][1]))


#Move Agent 1 2 steps in random direction
#y Step 1
if random.random() < 0.5:
    agents[0][0] += 1 
else:
    agents[0][0] -= 1
#x Step 1
if random.random() < 0.5:
    agents[0][1] += 1 
else:
    agents[0][1] -= 1  

#y Step 2
if random.random() < 0.5:
    agents[0][0] += 1 
else:
    agents[0][0] -= 1

#x Step 2
if random.random() < 0.5:
    agents[0][1] += 1 
else:
    agents[0][1] -= 1  


#Move Agent 2 2 steps in random direction
#y Step 1
if random.random() < 0.5:
    agents[1][0] += 1 
else:
    agents[1][0] -= 1
#x Step 1
if random.random() < 0.5:
    agents[1][1] += 1 
else:
    agents[1][1] -= 1  

#y Step 2
if random.random() < 0.5:
    agents[1][0] += 1 
else:
    agents[1][0] -= 1

#x Step 2
if random.random() < 0.5:
    agents[1][1] += 1 
else:
    agents[1][1] -= 1  

print ("New postion for agent 1 is - y " + str(agents[0][0]) + " x " + str(agents[0][1]))
print ("New postion for agent 2 is - y " + str(agents[1][0]) + " x " + str(agents[1][1]))

#Calculate the distance between the two agents
#uses Y difference squared added to X difference squared then square rooted
euclidiean_distance = (((agents[0][0]-agents[1][0])**2)+((agents[0][1]-agents[1][1])**2))**0.5

print ("The euclidiean distance between the two agents is " + str(euclidiean_distance))

#pulls out the higest y
print ("The Furthest north Agent- " + str(max(agents)))

#pulls out the higest x. Varible used to allow string function
furthest_east = max(agents, key=operator.itemgetter(1))
print ("The Furthest East Agent- " + str(furthest_east))


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(furthest_east[1],furthest_east[0], color='red')
matplotlib.pyplot.show()

