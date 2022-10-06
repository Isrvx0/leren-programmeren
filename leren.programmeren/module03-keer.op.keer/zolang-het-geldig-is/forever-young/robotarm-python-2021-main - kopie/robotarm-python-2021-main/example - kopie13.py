from multiprocessing.resource_sharer import stop
from RobotArm import RobotArm

# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

teller= 1
while teller < 10 and teller > 0:
    robotArm.grab()
    color = robotArm.scan()
    for move in range (teller):
        robotArm.moveRight()
    robotArm.drop()
    teller +=1
    for move2 in range (teller):
        robotArm.moveLeft()
    if color == '':
        break

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


