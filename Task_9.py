def main():
  '''
  Kodunuzu buraya yazin.
  '''
loaves = int(input("Number of loaves: "))
  print(f"Total price: {loaves*3.49:.3f} dollars")
  print(f"Discount: {loaves*3.49*0.6} dollars")

if __name__ == "__main__":
  main()
