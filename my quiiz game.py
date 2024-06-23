print("Welcome to my quiz")

play = input('Want to play? \n ') 

if(play.lower() != 'yes'):
    quit()


score = 0

ans = input("Q1> Who is the national animal of India\nA)tiger\nB)lion\nC)deer\n->")
if(ans.lower() == "a"):                                             #.upper/.lower he sgly i/p la small letter mde karta 
     print('correct!! :)')
     score += 1
else:
    print("Incorrect!! :( 'the correct answer is Tiger'")

ans = input("Q2> Who introduce the law of gravity?, choose the correct option \n A) Newton\nB) Enstine\nC) APJ abdul kalam\n->")
if(ans.upper() == "A"):
    print('correct!! :)')
    score += 1
else:
     print("Incorrect!! :( 'The correct answer is A'")

ans = input("Q3> Who is the Developer of PYTHON programing language \n A)Bjarne \nB)James \nC)Guido\n->")
if(ans.upper() == "C"):
     print('correct!! :)')
     score += 1
else:
    print("Incorrect!! :( 'The correct answer is B'")    

ans = input("Q4> Who is the CEO of MICROSOFT?? \n A) SUNDAR PECHAI \nB) SATYA NADELA\nC) BILL GATES\n-> ")
if(ans.upper() == "B"):
     print('correct!! :)')
     score += 1
else:
     print("Incorrect!! ): 'The correct answer is B'")

ans = input("Q5> What is the gravitational constant\nA) 3*10^8 m/s\nB) 9.8 m/s\nC) 3.14 m/s\n->")
if(ans.upper() == "B"):
     print('correct!! :)')
     score += 1
else:
    print("Incorrect!! :( 'the correct answer is B'")

print("conguralation you got " + str(score) + "/5 in my quiz")
print("you got " + str((score)/5 * 100) + "%")