n=int(input())
sum=0
for i in range(10,n,-2):
    sum=sum+i
    print(i,end="+")
print(str(n)+"="+str(sum+n))

##n=2
##start  stop  sum=sum+i   result    step
##
##10       2    sum=0+10=10  10+      8
##
##        2     sum=10+8=18  10+8+    6
##        2     sum=18+6=24  10+8+6+  4
##        2     sum=24+4=28  10+8+6+4 2
##
##10+8+6+4+2=30
