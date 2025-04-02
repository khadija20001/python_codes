# Harry Potter sorting hat 💖
print(" Do you like Dawn or Dusk?")
print("1-dawn ,2-dusk")
q1=int(input("enter your choice: "))
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
if q1==1:
  Gryffindor+=1
  Ravenclaw+=1
elif q1==2:
  Hufflepuff+=1
  Slytherin+=1
else:
  print("wrong inut")
print(" When I’m dead, I want people to remember me as:\
   1-The Good\
   2-The Great\
   3-The Wise\
   4-The Bold ")
q2=int(input("enter your choice: "))
if q2==4:
  Gryffindor+=1
elif q2==3:
  Ravenclaw+=1
elif q2==1:
  Hufflepuff+=1
elif q2==2:
  Slytherin+=1
else:
  print("wrong inut")
print(" Which kind of instrument most pleases your ear?\
    1) The violin\
    2) The trumpet\
    3) The piano\
    4) The drum")
q3=int(input("enter your choice: "))
if q3==4:
  Gryffindor+=1
elif q3==3:
  Ravenclaw+=1
elif q3==2:
  Hufflepuff+=1
elif q3==1:
  Slytherin+=1
else:
  print("wrong inut")
print(" Gryffindor",Gryffindor)
#print(Gryffindor)
print("Ravenclaw ",Ravenclaw)
#print(Ravenclaw )
print(" Hufflepuff ", Hufflepuff )
print( "Slytherin",Slytherin )
if  Gryffindor>Hufflepuff  and Gryffindor>Ravenclaw and Gryffindor> Slytherin:
  print("Gryffindor")
elif Hufflepuff> Ravenclaw  and Hufflepuff> Slytherin:
  print("Hufflepuff")
elif  Slytherin>Ravenclaw:
  print(" Slytherin")
else:
  print("Ravenclaw")