#pattern 9
res=1
for i in range(1,6):
  for j in range(1,6):
    if i>0 and res!=10:
      
      print(" "+str(i*j),end="")
    else:
      print(str(res),end="")
      res+=2
  print("")
    
