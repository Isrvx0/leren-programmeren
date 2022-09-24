from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = (3)
# Jouw python instructies zet je vanaf hier:

for i in range(3): 
  print(robotArm.grab() and robotArm.moveRight()and robotArm.drop() and robotArm.moveLeft())

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()