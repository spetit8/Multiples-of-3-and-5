#! Python 3

# This program will find the sum of multiples of 3 or 5 below a user input number

print("What number would you like to find multiples of 3 or 5 below?")

#initialize total to 0
total = 0
number = int(input())
for x in range(number):
      if x % 3 == 0 or x % 5 == 0:
          total += x
print(total)
      
