from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for moveright in range (4):
    print (robotArm.moveRight())
for i in range (1,6):
    robotArm.grab()
    for moveright in range (5):
        print (robotArm.moveRight())
    robotArm.drop()
    for moveLeft in range (6):
        print (robotArm.moveLeft())
    robotArm.grab()
robotArm.wait()