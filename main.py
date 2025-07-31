#EXERCICE CODEDEX

'''
The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin


Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the score for each house.

Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!
'''



gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Q1) Do you like Dawn or Dusk? \n 1) Dawn \n 2) Dusk")
resposta = int(input("resposta: "))

if resposta == 1:
    gryffindor += 1
    ravenclaw += 1
    print("Gryffindor and Ravenclaw both get a +1")
elif resposta == 2:
    hufflepuff += 1
    slytherin += 1
    print("Hufflepuff and Slytherin both get a +1")
else: 
    print("Wrong input!")

print("Q2) When I’m dead, I want people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold")
resposta = int(input("resposta: "))

if resposta == 1:
    hufflepuff += 2
    print("Hufflepuff +2")
elif resposta == 2:
    slytherin += 2
    print("Slytherin +2")
elif resposta == 3:
    ravenclaw += 2
    print("Ravenclaw +2")
elif resposta == 4:
    gryffindor += 2
    print("Gryffindor +2")
else:
    print("Wrong input!")

print("Q3) Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum")
resposta = int(input("resposta: "))

if resposta == 1:
    slytherin += 4
    print("Slytherin +4")
elif resposta == 2:
    hufflepuff += 4
    print("Hufflepuff +4")
elif resposta == 3:
    ravenclaw += 4
    print("Ravenclaw +4")
elif resposta == 4:
    gryffindor += 4
    print("Gryffindor +4")
else:
    print("Wrong input!")

print("-----------------------------")
print("|       gryffindor:", gryffindor, "      |")
print("|       slytherin:", slytherin,   "       |")
print("|       ravenclaw:", ravenclaw,   "       |")
print("|       hufflepuff:", hufflepuff, "      |")
print("-----------------------------")


print("-------------------BONUS----------------------")
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('Ravenclaw!')
elif hufflepuff >= slytherin:
  print('Hufflepuff!')
else:
  print('Slytherin!')
print("-----------------------------------------------")