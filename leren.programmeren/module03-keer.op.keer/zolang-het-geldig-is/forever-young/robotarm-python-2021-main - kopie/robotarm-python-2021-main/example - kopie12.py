from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = (5)

# Jouw python instructies zet je vanaf hier:
for i in range (20):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for i in range (10):
            robotArm.moveRight()
        robotArm.drop()
        for i in range (10):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

