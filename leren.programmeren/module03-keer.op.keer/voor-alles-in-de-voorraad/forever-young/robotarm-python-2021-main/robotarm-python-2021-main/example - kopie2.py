from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier: 

robotArm.grab()
for i in range(9):  # 9 = number of times to run the code
  print(robotArm.moveRight())
robotArm.drop()

for i in range(5):  
  print(robotArm.moveLeft())
robotArm.grab()
for i in range(5):  
  print(robotArm.moveRight())
robotArm.drop()

for i in range(2):  
  print(robotArm.moveLeft())
robotArm.grab()
for i in range(2):  
  print(robotArm.moveRight())
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
