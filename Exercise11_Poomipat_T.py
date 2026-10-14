number = int(input("ใส่เลขไป--> "))
for a in range(1,number+1):
  text = "* " * a
  
  b = number - a
  space = " " * b
  
  print(space,text)