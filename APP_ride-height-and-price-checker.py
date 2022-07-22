print("Welcome to our rollercoaster ride!")
height = int (input ("What is your height in cm?: "))

if height >= 120:
  age = int (input ("How old are you?: "))
  if age <= 12:
    print("It will be $5")
  elif age >12 and age <= 18:
    print("It will be $7")
  else:
    print("It will be $12")
else:
  print("You still need to grow taller to ride")
