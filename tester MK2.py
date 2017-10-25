import time

Q1= input("Are you ready fore the lagggggg!!!")
if Q1 == ('yes'):
  Q2 = int(input("1.Stars:\n 2.math"))
  if Q2 == int(1):
    for t in range (1,6):
      print (t)
      time.sleep (1)
    NumLine = int(200000000000000000000000000000000000000000000000)
    NumStars= int(200000000000000000000000000000000000000000000000 )
    for line in range (0, NumLine):
      for star in range (0,NumStars):
        print ('*'* star)
    print 
    
