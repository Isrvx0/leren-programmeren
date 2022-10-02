from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for move in range (7):
    robotArm.grab()
    for move1 in range (8):
        robotArm.moveRight()
    robotArm.drop()
    for move2 in range (8):
        robotArm.moveLeft()
robotArm.wait()