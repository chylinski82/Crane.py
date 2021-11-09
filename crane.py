#defining a function that allows a user to define a minimum radius of the crane in metres. user needs to give a value which is a number > 0 

def user_min_radius(min_radius):
  try:
    min_radius = float(min_radius)
    min_radius = round(min_radius, 1)
    if min_radius <= 0:
      print("please enter a valid radius in metres")
      min_radius = user_min_radius(input("What's the minimum radius in metres?"))
      return min_radius
      
    else:
      print("The minimum radius is set to " + str(min_radius) + "m")
      return min_radius

  except ValueError:
    print("please enter a valid radius in metres")
    min_radius = user_min_radius(input("What's the minimum radius in metres?"))
    return min_radius
  
min_radius = user_min_radius(input("What's the minimum radius in metres?"))

def user_max_radius(max_radius):
  try:
    max_radius = float(max_radius)
    max_radius = round(max_radius, 1)
    if max_radius <= min_radius:
      print("please enter a radius that is higher than the minimum radius")
      max_radius = user_max_radius(input("What's the maximum radius in metres?"))
      return max_radius
      
    else:
      print("The maximum radius is set to " + str(max_radius) + "m")
      return max_radius

  except ValueError:
    print("please enter a valid radius in metres")
    max_radius = user_max_radius(input("What's the maximum radius in metres?"))
    return max_radius
  
max_radius = user_max_radius(input("What's the maximum radius in metres?"))

current_radius = min_radius

def dropping_load(current_radius):
  next_radius = input("To what radius is this going?")
  next_radius = float(next_radius)
  next_radius = round(next_radius, 1)
  try:
    if next_radius < min_radius or next_radius > max_radius:
      print("This radius is not within the reach of the crane")
      dropping_load(current_radius)
    else:
      current_radius = next_radius
      print("current radius is " + str(current_radius) + " m.")
  except ValueError:
    print("Input a radius in metres")
    dropping_load(current_radius)

def lifting(current_radius):
  print("current radius is " + str(current_radius) + " m.")
  next_radius = input("At what radius is the next load?")
  next_radius = float(next_radius)
  next_radius = round(next_radius, 1)
  try:
    if next_radius < min_radius or next_radius > max_radius:
      print("The load is not within the reach of the crane")
      return current_radius
    else:
      current_radius = next_radius
      print("current radius is " + str(current_radius) + " m.")
      dropping_load(current_radius)
  except ValueError:
    print("Enter a valid radius in metres")
    return current_radius

work = True
def work_shift(work):
  while work == True:
    lifting(current_radius)
    answer = input("Would you like to continue lifting? Press 'y' and 'enter' for 'yes'")
    if answer != "y":
      print("Bye")
      work = False

work_shift(work)



#lifting(current_radius)