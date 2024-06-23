import random
a=random.randint(1,10)
answer=int(input("Ведите число"))
while answer!=a:
  if answer>a:
    print("Ты не угадал мое число меньше")
  else:
    print("Ты не угадал мое число больше")
  if answer-a==1 or answer-a==1 or answer-a==2 or answer-a==2:
   print("Горечо!")
  elif answer-a==3 or answer-a==3 or answer-a==4 or answer-a==4:
   print("Тепло!")
  else:
    print("холодно")
 
  answer=int(input("Ведите число"))
rint("Ты угадал число")
