# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
starting_fuel_level = 0
num_astronauts_aboard = 0
altitude = 0

# Exercise #4: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 
starting_fuel_level = int(input("Enter the starting fuel level:"))
while (starting_fuel_level < 5000 or starting_fuel_level > 30000):
  starting_fuel_level = int(input("Invalid input. Please enter a value between 5000 and 30000:"))

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
num_astronauts_aboard = int(input("Enter the number of astronauts:"))
while (num_astronauts_aboard < 0 or num_astronauts_aboard > 7):
    num_astronauts_aboard = int(input("Invalid input. Please enter a value between 0 and 7:"))
  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
while altitude < 2000:
  starting_fuel_level -= 100*num_astronauts_aboard
  altitude += 50
  print(f"The shuttle gained an altitude of {altitude} km and has {starting_fuel_level} kg of fuel left")
  if altitude >= 2000:
    print("Orbit achieved!")
  else:
    print("Failed to reach orbit.")



# Exercise #5: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
