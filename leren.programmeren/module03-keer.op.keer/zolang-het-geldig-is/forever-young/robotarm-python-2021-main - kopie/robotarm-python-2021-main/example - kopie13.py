from multiprocessing.resource_sharer import stop
from RobotArm import RobotArm

# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
# robotArm.grab()
# color = robotArm.scan()
# for i in range (1,6):
#     robotArm.grab()
#     for move in range (i):
#         robotArm.moveRight()
#     robotArm.drop()
#     for move in range (i):
#         robotArm.moveLeft()
teller= 1
while teller < 10 and teller > 0:
    robotArm.grab()
    color = robotArm.scan()
    if color == "white" or color =="blue" or color == "yellow" or color == "green" or color == "red" :
        for move in range (teller):
            robotArm.moveRight()
        robotArm.drop()
        teller +=1
        for move2 in range (teller):
            robotArm.moveLeft()
    if color == '':
        break
else:
    stop




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()



# for i in range (1,6):
#     robotArm.grab()
#     for move in range (i):
#         robotArm.moveRight()
#     robotArm.drop()
#     for move in range (i):
#         robotArm.moveLeft()

