from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = (5)
# Jouw python instructies zet je vanaf hier:

for i in range(7): 
  print(robotArm.moveRight())
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for i in range(2): 
  print(robotArm.moveLeft())
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for i in range(2): 
  print(robotArm.moveLeft())
print (robotArm.grab() and robotArm.moveRight() and robotArm.drop())

for i in range(2): 
  print(robotArm.moveLeft())
print (robotArm.grab() and robotArm.moveRight() and robotArm.drop())

for i in range(2): 
  print(robotArm.moveLeft())
print (robotArm.grab() and robotArm.moveRight() and robotArm.drop())

for i in range(2): 
  print(robotArm.moveLeft())
print (robotArm.grab() and robotArm.moveRight() and robotArm.drop())

for i in range(2): 
  print(robotArm.moveLeft())
print (robotArm.grab() and robotArm.moveRight() and robotArm.drop())

for i in range(2): 
  print(robotArm.moveLeft())
print (robotArm.grab() and robotArm.moveRight() and robotArm.drop())

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()