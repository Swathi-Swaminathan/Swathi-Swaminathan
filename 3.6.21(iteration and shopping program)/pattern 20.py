#pattern 20
for i in range(1,6):
  for j in range(1,6):
    print(""+str((i*j)%2),end=" ")
  print(" ")

##ITERATION
##i       j     str((i*j)%2)    print
##
##
##1       1       1%2=1          1
##1       2       2%2=0          0
##1       3       3%2=1          1
##1       4       4%2=0          0
##1       5       5%2=1          1
##
##2       1       2%2=0          0
##2       2       4%2=0          0
##2       3       6%2=0          0
##2       4       8%2=0          0
##2       5       10%2=0         0
##
##3       1       3%2=1          1
##3       2       6%2=0          0
##3       3       9%2=1          1
##3       4       12%2=0         0
##3       5       15%2=1         1
##
##4       1       4%2=0          0
##4       2       8%2=0          0
##4       3       12%2=0         0
##4       4       16%2=0         0
##4       5       20%2=0         0
##
##5       1       5%2=1          1
##5       2       10%2=0         0
##5       3       15%2=1         1
##5       4       20%2=0         0
##5       5       25%2=1         1

##OUTPUT
##
##1 0 1 0 1  
##0 0 0 0 0  
##1 0 1 0 1  
##0 0 0 0 0  
##1 0 1 0 1  
