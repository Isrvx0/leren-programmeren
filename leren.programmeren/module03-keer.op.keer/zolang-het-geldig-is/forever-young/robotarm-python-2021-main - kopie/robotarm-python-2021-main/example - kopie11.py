from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
# van recht naar links
for moveright in range (10):
    robotArm.moveRight()

for i in range (1,10):
    robotArm.grab()
    color = robotArm.scan()
    print (color)
    if color == 'white':
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
robotArm.wait()