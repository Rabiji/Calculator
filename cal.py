a = input("enter your number: ")
c = input("Enter Operatot: ")
b = input("enter your number: ")

P=int (a) ** int(b)
D=int(a) + int(b)
E=int(a) / int(b)
F=int(a) - int(b)
G=int(a) * int(b)

if c == "+":
  print(D)
elif c == "-":
  print(F)
elif c == "/":
  print(E)
elif c == "*":
  print(G)
elif c== "**":
  print (P)
else:
  print("invalid")

