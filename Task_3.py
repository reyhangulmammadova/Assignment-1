def main():
  '''
  Kodunuzu buraya yazin.
  '''
number = int(input("Enter 4 digit number: "))
first = number//1000
second = (number//100)%10
third = (number//10)%10
fourth = number%10
  print(f"Digits: {number//1000} {(number//100)%10} {(number//10)%10} {number%10}")
  print(f"Sum of digits: {first} + {second} + {third} + {fourth} = {first + second + third + fourth}")
  print(f"Product of digits: {first} * {second} * {third} * {fourth} = { first * second * third * fourth}")
  

if __name__ == "__main__":
  main()
