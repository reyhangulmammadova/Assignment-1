# import libraries here
from math import log
def main():
a = int(input("Enter a: "))
b = int(input("Enter b: "))
  print(f"{a} + {b} = {a+b}")
  print(f"{a} - {b} = {a-b}")
  print(f"{a} * {b} = {a*b}")
  print(f"{a} % {b} = {a%b}")
  print(f"{a} // {b} = {a//b}")
  print(f"log10( {a} ) = {log(a,10):.2f}")

if __name__ == "__main__":
  main()
