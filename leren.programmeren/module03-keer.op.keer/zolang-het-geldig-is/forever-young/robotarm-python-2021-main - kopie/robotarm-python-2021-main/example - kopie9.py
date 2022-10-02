from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for i in range (4):
    for moveRobotArm in range(4):
        robotArm.grab()
        for moveRobotArm1 in range (5):
            robotArm.moveRight()
        robotArm.drop()  
        for moveRobotArm1 in range(4):
            robotArm.moveLeft()
    for moveRobotArm1 in range(4):
        robotArm.moveLeft()
robotArm.wait()