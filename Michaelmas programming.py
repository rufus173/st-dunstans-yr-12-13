#subroutine
#dice face problem

def fiveface():
  print("0000000000")
  print("0        0")
  print("0  #  #  0")
  print("0    #   0")
  print("0  #  #  0")
  print("0        0")
  print("0000000000")


#mainprogram
fiveface()

#-----------------------------------------------------------


#----------------
#subprogram
#converts centigrade to fahrenheit
#----------------

def c_to_f():
   fahrenheit = (centigrade * 1.8) + 32
   return fahrenheit
  
  
def f_to_c():
   centi = (fahren-32)/1.8
   return fahren
#----------------
#main program
#----------------

centigrade = int(input("enter centigrade you wish to convert:"))
fahren = int(input("enter fahrenheit you wish to convert"))
print("the temperature in fahrenheit is " , c_to_f () )
print("the temp in centi is", f_to_c() )


#----------------------------------------------------------

digits = [0,1,2,3,4,5,6,7,8,9]
character = ["a","b","c","d","A","B","C","D","@","#","!","£"]
alphanumerics = digits + character 
print(alphanumerics)

#----------------------------------------------------------

#fish tank problem 
#subprogram 

def fishtank():
  volume = (length * depth * height)/1000
  print(round(volume,2))


#main program
length = float(input("enter the length of the fish tank "))
depth = float(input("enter the depth of the fish tank "))
height = float(input("enter the height of the fish tank "))


fishtank()

#-----------------------------------------------------------

#microscopy 
#subprogram 

def microscopy():
  image_size = imageSize * (10**4)
  magnification = image_size /actualSize
  print(round(magnification))
  
  
#main program 
imageSize = float(input("enter the image size of the cell in cm"))
actualSize = float(input("enter the actual size of the cell in micrometers"))

microscopy()

#---------------------------------------------------------

#carpet cost 
#subprogram 

def carpetcost():
  area = width * length
  underlay = 3 * area
  gripper = (2* width)+(2*length)
  fittingFee = 50
  carpet = width * length * price
  total = carpet + fittingFee + gripper + underlay
  print(round(total,2))

  
#main program 
width = int(input("enter the width of the room"))
length = int(input("enter the length of the room"))
price = float(input("enter the price of the carpet"))



carpetcost()

#--------------------------------------------------------------

#energy bill calculator 
#subprogram


def energyBill ():
  unitsUsed = currentRead - previousRead
  calorificValue = 39.3
  kilowatts = (unitsUsed* 1.022*calorificValue)/3.6
  totalEnergy = kilowatts *2.84
  print(round(totalEnergy,2))

#main program 
previousRead = int(input("enter the previous meter reading"))
currentRead = int(input("enter the current meter reading"))


energyBill ()

#-------------------------------------------------------------

#circle properties 
#subprogram 

def circle ():
  radius = diameter/2
  areaOfCircle = pi * (radius**2)
  circumference = diameter * pi
  arcLength = (circumference * arcAngle)/360
  print("radius =", radius)
  print("the area is", round(areaOfCircle,2))
  print("circumference =", round(circumference,2))
  print("arc length is", round(arcLength,2))
  
#main program 
diameter = int(input("enter the diameter of the circle"))
arcAngle = int(input("enter the arc angle of the circle"))
pi =3.1415926535

circle()

#--------------------------------------------------------------

#ball pit problem 
#subprogram 

def ballPit():
  volumeBallPit = pi *ballPitHeight * (ballPitRadius**2)
  print("the volume of the ball pit is",round(volumeBallPit,2))
  volumeBall = (4/3)* pi * (ballRadius ** 3)
  print("the volume of a ball is", round(volumeBall,1))
  ballsInPit = (volumeBallPit/volumeBall)* 0.75
  print("the number of balls that can fit in the ball pit is", round(ballsInPit))
  


#main program 
ballRadius = float(input("enter the radius of the balls "))
ballPitRadius = float(input("enter the radius of the ball pit"))
ballPitHeight = float(input("enter the height of the ball pit"))
pi = 3.1415926535

ballPit()

#---------------------------------------------------------------

#driving test problem 
#subprogram

def faults():
  if minorfaults < 16:
    print("pass")
  else:
    print("fail")



#main program
minorfaults = int(input("enter how many minor faults they have done."))

faults()

#---------------------------------------------------------------

#max program
#returns the larger of two numbers
#subprogram 

def max():
  if num1 > num2:
    print(num1)
  elif num1 == num2:
    print("both numbers are the same.")
  else:
    print(num2)

#main program 

num1 = int(input("enter a number"))
num2 = int(input("enter another number"))


max()

#---------------------------------------------------------------

#states of water 
#depending on the temp of water it will return whether solid liquid or gas
#subprogram 

def statesOfWater():
  if temp <= 0:
    print("the water is in a solid state")
  elif temp > 0 and temp < 100:
    print("the water is liquid state")
  else:
    print("the water has evaporated so it is a gas.")



#main program 

temp = float(input("enter the temp of the water"))

statesOfWater()

#-------------------------------------------------------------

#career quote problem 
#subprogram 

def occupation():
  if job1 == "ENGINEER":
    print("The engineer has been, and is, a maker of history.")
  elif job1 == "DEVELOPER":
    print("Logical thinking, passion and perseverance is the paint on your palette.")
  elif job1 == "ANALYST":
    print("Seeing what other people can’t see gives you great vision.")
  else:
    print("I'm sorry. We could not find a quote for your job.")

#main program 
job = str(input("enter your occupation"))
job1 = job.upper()

occupation()

#---------------------------------------------------------------

#currency converter 
#£1 = $1.31
#£1 = 1.18 euro
#£1 = 9.31 yuan
#£1 = 184.82 yen 
#subprogram 


def currencyConverter():
  if moneyExchange == "USD":
    americanDollars = moneyAmount * 1.31
    print("$",round(americanDollars,2))
  elif moneyExchange == "EURO":
    euro = moneyAmount * 1.18
    print(round(euro,3) , "euro")
  elif moneyExchange == "YUAN":
    yuan = moneyAmount * 9.31
    print(round(yuan,3), "yuan")
  else:
    yen = moneyAmount * 184.82
    print(round(yen,3), "yen")


#main program 
moneyType = str(input("What would you like to exchange GBP to? USD...Euro...Yuan or Yen"))
moneyExchange = moneyType.upper()
moneyAmount = float(input("enter the amount in pounds you would like to exchange"))




currencyConverter()

#--------------------------------------------------------------


def functionDose():
  if nitrateLevel >10:
    return 3
  elif nitrateLevel >2.5 and nitrateLevel <10 :
    return 2
  elif nitrateLevel >1 and nitrateLevel <2.5 :
    return 1
  else:
    return 0.5


#main program 

nitrateLevel = float(input("enter the nitrate level."))


print(functionDose())


#---------------------------------------------------------------

#periodic table 
#subprogram 

element1 = [["hydrogen",1,1],["helium",4,8],["beryllium",6,2], ["boron",10,3],["carbon",12,6], ["nitrogen",14,7]]

def elements():
  match element:
    case "hydrogen":
      print(element1[0])
    case "helium":
      print(element1[1])
    case "beryllium":
      print(element1[2])
    case "boron":
      print(element1[3])
    case "carbon":
      print(element1[4])
    case "nitrogen":
      print(element1[5])

#main program

element = input("enter an element")

elements()


#------------------------------------------------------------

#exam grade problem
#subprogram

def grade():
  if mark > 80:
    print("your grade is ", 9 )
  elif mark > 67 and mark <80:
    print("your grade is ", 8 )
  elif mark > 54 and mark < 67:
    print("your grade is", 7 )
  elif mark> 41 and mark <54:
    print("your grade is", 6)
  elif mark > 31 and mark <41:
    print("your grade is",5)
  elif mark> 22 and mark<31 :
    print("your grade is",4)
  elif mark>13 and mark<22:
    print("your grade is",3)
  elif mark>4 and mark<13:
    print("your grade is",2)
  elif mark>2 and mark <4:
    print("your grade is",1)
  else:
    print("your grade is U")
      


#main program 

mark = int(input("enter the mark you recieved in the test:"))

grade()

#--------------------------------------------------------

#day format 
#subprogram 

daysOfWeek = [["monday",1, "M"],["tuesday",2,"Tu"],["Wednesday",3,"W"], ["Thursday",4,"Thu"],["Friday",5, "F"],["Saturday",6, "sat"],["sunday",7, "Sun"]]


def dayFormat():
  if weekday == 1:
    print(daysOfWeek[0])
  elif weekday ==2:
    print(daysOfWeek[1])
  elif weekday ==3:
    print(daysOfWeek[2])
  elif weekday ==4:
    print(daysOfWeek[3])
  elif weekday ==5:
    print(daysOfWeek[4])
  elif weekday ==6:
    print(daysOfWeek[5])
  else:
    print(daysOfWeek[6])



#main program 
weekday = int(input("enter an integar number from 1 to 7"))


dayFormat()
#--------------------------------------------------------
#ployhedral dice problem 
#subprogram 

import random

def rollDice():
  print(random.randrange(0,facesOfDice))
  
  
#main propgram 
facesOfDice = int(input("enter the number of faces of dices"))


rollDice()
#------------------------------------------------------

#clamp problem 
#subprogram

def largerNumber():
  if num1 > num2:
    print(num2)
  else:
    print(num1)


#main program
num1 = int(input("enter a number"))
num2 = int(input("enter another number"))

largerNumber()

#------------------------------------------------------
#leap year problem 
#subprogram

def leapYear():
  if ( year % 4) == 0:
    print("true, it is a leap year")
  elif (year % 100) == 0:
    print("false, it is not a leap year")
  elif (year% 400)== 0:
    print("true, it is a leap year")
  else:
    print("it is not a leap year")



#main program 

year = int(input("enter a year"))

leapYear()

#---------------------------------------------------

#hours in a day problem 
#subprogram

def hoursIntoDays():
  days = hours//24
  hour = hours % 24
  print("this is",days,"days",hour,"hours")



#main program
hours= int(input("enter the amount of hours"))

hoursIntoDays()
#-------------------------------------------------
#dice problem 
#subprogram 

import random 

def diceGame():
  die1 = random.randint(0,6)  #a random number from 0-6
  die2 =random.randint(0,6)
  die3 = random.randint(0,6)
  print("you rolled",die1)
  print("you rolled",die2)
  print("you rolled",die3)
  if (die1 == die2) and (die2 == die3):
    total = die1 + die2 + die3
    print(total)
  elif die1 == die2 !=  die3:
    total = (die1 +die2)- die3
    print(total)
  elif die2 == die3 != die1:
    total = (die2+ die3)- die1
    print(total)
  elif die1 == die3 != die2:
    total = (die1 + die3)- die2
    print(total)
  else:
    print("you scored 0")
    

#main program

diceGame()
#--------------------------------------------------------

#divisible problem
#subprogram

def divisibleProblem():
  num1 = int(input("enter a whole number "))
  num2 = int(input("enter a whole number "))
  if num1 == 0 or num2 == 0:
    print("false")
  elif num1 % num2 == 0:
    print("true")
  else:
    print("false")


#main program

divisibleProblem()

#-----------------------------------------------------

#dogs life problem 
#subprogram

def humanToDogYears():
  if humanYears <= 2:
    dogYears = humanYears * 12
  else:
    dogYears = 24 + (6 * humanYears) - 2
  print("your dog is",dogYears, "in dog years!")



#main program
humanYears = float(input("enter how old your dog is in human years (does not have to be whole number)"))

humanToDogYears()
#---------------------------------------------------
#electric car problem 
#subprogram

minimumCharge = 3
minimumPoints = 22

def totalCost():
  if noOfMinutes < 15:
    total = 1 + minimumCharge
  else:
    extraMins = noOfMinutes - 15
    total = 1 + minimumCharge + (extraMins * 0.2)
  print("the cost is" , round(total,2))
  
  
def numOfPoints():
  totalPoints = minimumPoints + (noOfMinutes * 1.5)
  print("your total points earned is ",totalPoints)



#main program 
noOfMinutes = int(input("enter the number of minutes spent charging your electric car"))

totalCost()
numOfPoints()

#------------------------------------------------------

#tweet problem 
#subprogram


def goodPost():
  if len(tweet) <= 20:
    print("true")
  else:
    print("false")


#main program
tweet = str(input("enter the tweet"))

goodPost()

#-------------------------------------------------------

#initial and surname problem
#subprogram

def foreSurName():
  firstLetter = forename[0]
  upperletter = firstLetter.upper()
  capsSurname = surname.upper()
  fullName = upperletter + capsSurname
  print(fullName)


#main program
forename = input("enter your first name")
surname = input("enter your surname")

foreSurName()

#----------------------------------------------------

#airplane ticket 
#subprogram

def destination():
  takeOff = takeOffDes[:4]  #takes the first four letters of the take off name2
  arrival = arrivalDes[:4] #takes the first four letters of the arrival destination
  takeOff = takeOff.upper()
  arrival = arrival.upper()
  total = print(takeOff ,"-" ,arrival )
  

#main program

takeOffDes = input("enter the city you are travelling from")
arrivalDes =input("enter the city you are travelling to")

destination()

#------------------------------------------------

#teacher code problem 
#subprogram 

def initials():
  first_name = firstName[:1]
  first_name = first_name.upper()
  sur_name = surName[:1]
  sur_name = sur_name.upper()
  if middleName == "":
    middle_name = "Z"
  else:
    middle_name = middleName[:1]
    middle_name = middle_name.upper()  
  total = first_name + middle_name +sur_name
  print(total)


#main program

firstName = input("enter your first name")
middleName = input("enter your middle name ")
surName = input("enter your surname")

initials()

#----------------------------------------------

#valid address problem 
#subprogram 

def validation():
  length =len(email)
  for x in range[0,length]:
    if email != "@" and email != ".":
      print("false, the email is not valid")
    else:
      print("true, the email is valid")

#main program
email = str(input("enter your email"))


validation()
#--------------------------------------------
#name separator problem
#subprogram

def nameSeparator():
  full_name = fullName.split()
  #this splits the full name into two different strings
  print(full_name[0])
  print(full_name[1])

#main program 

fullName = str(input("enter your full name"))


nameSeparator()
#-------------------------------------------

#naming convetion 
#subprogram

def namingConvention():
  if choice == "kebab case":
    word1= identifier1.lower()
    word2 = identifier2.lower()
    x ="-"
    print(word1+x+word2)
  elif choice == "camel case":
    word1 = identifier1.lower()
    word2 = identifier2.capitalize()
    total = print(word1 +word2)
  elif choice == "pascal case":
    word1 = indentifier.capitalize()
    word2 = identifier.capitalize()
    total = print(word1 +word2)
  else:
    word1= identifier1.lower()
    word2 = identifier2.lower()
    y ="_"
    print(word1+y+word2)
    


#main program
identifier1  = input("enter the first word identifier")
identifier2 = input("enter the second word identifier")
choice = input("enter the format (kebab case, snake case, camel case or pascal case")

namingConvention()
#---------------------------------------------------

#acsii and ebcdic
#subprogram

letter = input("enter a letter from the english alphabet")


def characterSets():
  letters = letter.upper()
  asciiTranslation = ord(letters)
  ascii = print("the number for this in ASCII is",asciiTranslation)
  if asciiTranslation >64 and asciiTranslation <74:
    ebcdicTranslation = asciiTranslation + 128 
  elif asciiTranslation >73 and asciiTranslation < 83:
    ebcdicTranslation = asciiTranslation + 135
  else:
    ebcdicTranslation = asciiTranslation + 143
  print("the number for this in ebcdic is",ebcdicTranslation)  
    
#main program

characterSets()

#-----------------------------------------------
#times table problem 
#subprogram

def timesTable():
  x = 0 
  while x != 12:
    x = x +1
    total = x * number 
    print(total)
    
#main program 

number = int(input("enter a number from 1 to 12 for the times table"))

timesTable()
#-----------------------------------------------

#discount counter problem 
#subprogram

currentSale = 10


while currentSale != 60 or currentSale < 60:
  import random
  randnum = random.randint(1,10)
  currentSale = currentSale + randnum
  print(currentSale,"%")
  
#-----------------------------------------------


#prime number problem 

number = int(input("enter a number"))

def isPrime():
  if number <1:
    print("this number is not prime")
  else:
    for i in range(number,0, -1):
      remainder= number% (number -1)
    count = 0
    if remainder == 0:
     count = count+1
    if count == 2:
     print("number is prime")
    else:
     print("number is not prime")


isPrime()

#------------------------------------------
