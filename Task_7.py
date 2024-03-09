# import libraries here
from math import tan
from math import pi

def main():
  '''
  Kodunuzu buraya yazin.
  '''
s = float(input("Length: "))
n = int(input("Number of sides: "))
area = (n*s**2)/(4*math.tan(math.pi/n))
  print(f"Area: {area}")

if __name__ == "__main__":
  main()
