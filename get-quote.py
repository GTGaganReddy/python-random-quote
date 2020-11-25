import random
def main():
  #print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  rand=random.randint(0, 13)
  print(quotes[rand])

if __name__== "__main__":
  main()