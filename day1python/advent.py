


def main():
  f = open("adventday1numbers.txt","r")
  text = f.readlines()
  year = 2020
  for x in text:
      x =x.strip("\n")
      x = int(x)
      for y in text:
        y =y.strip("\n")
        y = int(y)
        if(x+y == year):
            print(x * y) 
  return 



main()