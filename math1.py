try:
  a=float(input("Enter first number:"))
  b=float(input("Enter second number:"))
  print(f"Add:{a+b}")
  print(f"sub:{a-b}")
  print(f"mul:{a*b}")
  if b!=0:
    print(f"div:{a/b}")
  else:
    print("not divisible")
except ValueError:
  print("enter valid choice")
