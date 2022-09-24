from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')
robotArm.speed = (3)
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()

robotArm.grab()
for i in range(2): 
  print(robotArm.moveRight())
robotArm.drop()
for i in range(2): 
  print(robotArm.moveLeft())

robotArm.grab()
for i in range(3): 
  print(robotArm.moveRight())
robotArm.drop()
for i in range(3): 
  print(robotArm.moveLeft())

robotArm.grab()
for i in range(4): 
  print(robotArm.moveRight())
robotArm.drop()
for i in range(4): 
  print(robotArm.moveLeft())

robotArm.grab()
for i in range(5): 
  print(robotArm.moveRight())
robotArm.drop()
for i in range(5): 
  print(robotArm.moveLeft())

robotArm.grab()
for i in range(6): 
  print(robotArm.moveRight())
robotArm.drop()
for i in range(6): 
  print(robotArm.moveLeft())

robotArm.grab()
for i in range(7): 
  print(robotArm.moveRight())
robotArm.drop()
for i in range(7): 
  print(robotArm.moveLeft())

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()