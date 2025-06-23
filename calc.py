import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

calc={"+": add, "-": sub, "*": mul, "/": div}
go=True

while go:
 n1=int(input("Enter first number: "))
 rep=False
 while rep==False:
  curr=0
  op=(input("Enter operation: +,_,*,/\n"))
  n2=int(input("Enter second number: "))
  if op=="+":
    result=calc["+"](n1=n1,n2=n2)
    curr+=result
    print(result)
  elif op=="-":
    result=calc["-"](n1=n1,n2=n2)
    curr+=result
    print(result)
  elif op=="*":
    result=calc["*"](n1=n1,n2=n2)
    curr+=result
    print(result)
  elif op=="/":
    result=calc["/"](n1=n1,n2=n2)
    curr+=result
    print(result)
  else:
    print("Invalid operation")
  repeat=input(f"Press enter 'y' to start new calculation else press 'n' to start calculation with {curr} as first number").lower()
  if repeat=="n":
    go=True
    rep=False
    n1=curr
  elif repeat=="y":
     go=True
     rep=True
