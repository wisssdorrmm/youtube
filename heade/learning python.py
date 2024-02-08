#for i in range(0,11):
 # print(i)

  #Building a basic calculator
print("Carry out some basic arithmetic")

First_value = float(input("Enter the first number: "))
Second_value = float(input("Enter the second number: "))
Add = First_value + Second_value
print(Add)

#Designing a mad Libs Game
print("Play some mad libs game")
color = input("Enter the color: ")
Plural_noun = input("Enter the Plural noun: ")
person = input("Enter the person: ")
crush = input("Enter the name of your crush: ")


print("Roses are " + color)
print(Plural_noun + " are blue")
print(person + " is beautiful")
print("I love " + crush)

#Learning about list

List1 = ["Fish","Cake","Crayfish","Ice-cream"]
List2 = ["Maggi","Garri","Eggs"]
List2.extend(List1)

print(List2)

#Learning about Functions
def greetings(name,Language,):
  print("Hello "+ name +", i am learning "+ Language)

List = ("Python","C#","c++","Power tool")

#for i in List:
if "Power tool" in List:
  print(List)
else:
  print("not possible")

greetings("frank","python")
greetings("Wisdom","C#")    
#Building a guessing game
print("Play a guessing a game")
secret_word = "Esther"
print ("Hint:the name of Jurgen's first girlfriend")
print("Kindly note that the word must begin with a uppercase")
guess = ""
guess_count = 0
guess_limit = 3
out_of_guessess = False
while guess != secret_word and not(out_of_guessess):
  if guess_count < guess_limit:
      guess = input("Enter the secret word: ")
      guess_count +=1
  else:
    out_of_guessess = True   
if out_of_guessess:
   print("out of guessess,YOU LOSE!") 
else:
   print ("Congratulations! You have won the game")