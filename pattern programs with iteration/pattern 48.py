#pattern 48
rval=1
row=5
for i in range(1,6):
    print(rval,end=" ")
    cval=rval
    col=row
    rval=rval+row
    row-=1

    for j in range(2,i+1):
        cval-=col
        col+=1
        print(cval,end=" ")
    print()

##Iteration
##
##i    print    cval    col      rval     row     j    cval     col     print          print
##
##1     1         1      5        6        4                                           1
##
##2     6         6      4       10        3      2     2        5        2            6  2
##
##3     10       10      3       13        2      3     7        4        7           10  7  
##3                                               4     3        5        3           10  7   3
##
##
##4     13       13      2       15        1      5     11       3        11          13  11        
##4                                               6     8        4         8          13  11  8
##4                                               7     4        5         4          13  11  8  4
##
##
##5     15       15      1       16        0      8     14       2        14          15  14
##5                                               9     12       3        12          15  14  12
##5                                              10     9        4         9          15  14  12  9
##5                                              11     5        5         5          15  14  12  9  5
##
##OUTPUT
##
##1 
##6 2 
##10 7 3 
##13 11 8 4 
##15 14 12 9 5 
