from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
for i in range (1,10):
    robotArm.grab()
    color = robotArm.scan()
    print (color)
    if color == 'white':
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()