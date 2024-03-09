def main():
  '''
  Kodunuzu buraya yazin.
  '''
s1 = int(input("Side1: "))
s2 = int(input("Side2: "))
s3 = int(input("Side3: "))
s4 = (s1 + s2 + s3)/ 2
s_ucbucaq =(s4*(s4-s1)*(s4-s2)*(s4-s3))**0.5
  print(f"Area of triangle: {s_ucbucaq:.2f}")


if __name__ == "__main__":
  main()
