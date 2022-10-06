from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = (2)
teller= 9
# Jouw python instructies zet je vanaf hier:
while teller < 10 and teller > 0 :
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for move1 in range (0,teller):
            robotArm.moveRight()
        robotArm.drop()
        teller -= 1
        for move2 in range (0,teller):
            robotArm.moveLeft()
    else:
        teller -= 1
        robotArm.drop()
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()