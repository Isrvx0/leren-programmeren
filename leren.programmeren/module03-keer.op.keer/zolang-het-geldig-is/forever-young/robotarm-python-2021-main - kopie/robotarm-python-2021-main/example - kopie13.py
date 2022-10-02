from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
for i in range (1,6):
    robotArm.grab()
    for move in range (i):
        robotArm.moveRight()
    robotArm.drop()
    for move in range (i):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()