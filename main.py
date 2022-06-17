for number in range(5) :
  for another_number in range(3):
    if number == 0 or number == 2:
      if another_number < 2:
        print("*", end = "")
      else:
        print("*", end = "" "\n")
    elif number == 1:
      if another_number == 0:
        print("*", end = "")
      elif another_number == 1:
        print(" ", end = "")
      else:
        print("*", end = "" "\n")
    elif number == 3 or number == 4:
      if another_number == 0:
        print("*", end = "")
      elif another_number == 1:
        print(" ", end = "")
      else:
        print(" ", end = "" "\n")

print("\n")

NUM_ACROSS = 3 # Number of asterisks to print across
NUM_DOWN = 5 # Number of asterisks to print down

# Write a loop to control the number of rows.
for down in range(NUM_DOWN):
    # Write a loop to control the number of columns
    for across in range(NUM_ACROSS):
        if down == 0 or down == 2 or down == 4:
          # Decide when to print an asterisk in every column.
          if across < 2:
            print("*", end = "")
          else:
            print("*", end = "" "\n")
        elif down == 1 or down == 3:
          # Decide when to print asterisk in column 1.   
          if across == 0:
            print("*", end = "")
          # Decide when to print a space instead of an asterisk.  
          elif across == 1:
            print(" ", end = "")
          else:
            print(" ", end = "" "\n")
          # Figure out where to place this statement that prints a newline.

