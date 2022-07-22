print("Welcome to our rollercoaster ride!")
height = int (input ("What is your height in cm?: "))

bill = 0

if height >= 120:
  age = int (input ("How old are you?: "))
  if age <= 12:
    bill = 5
    print(f"Child tickets are ${bill}")
  elif age >12 and age <= 18:
    bill = 7
    print(f"Teenager tickets are ${bill}")
  elif age >= 45 and age <= 55:
    print("Everything's gonna be fine. Here's a free ride on us!")
  else:
    bill = 12
    print(f"Adult tickets are ${bill}")
    
  photo = input ("Do you want a $3 photo? Y / N: \n")
  if photo == "Y":
    bill += 3
    
  print(f"Your total is ${bill}") 
                
else:
  print("You still need to grow taller to ride")
