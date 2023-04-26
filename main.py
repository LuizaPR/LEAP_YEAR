year = int(input("Which year do you want to check? "))

division1 = year % 4
division2 = year % 100
division3 = year % 400

if division1 == 0:
  if division2 != 1:
    print("Leap year.")
  elif division3 == 0:
    print("Leap year.")
  else:
    print("Not leap year.")
else:
  print("Not leap year.")