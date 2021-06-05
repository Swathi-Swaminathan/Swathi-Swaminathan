#pattern 31
for i in range(65,70):
    res=i
    for j in range(5):
        print(chr(res),end=" ")
        res+=1
    print()

##ITERATION
##
##i res=i    j     print(chr(res))  res+=1    print
##
##
##65 65      1      A               66           A
##65 65      2      B               67           B        
##65 65      3      C               68           C
##65 65      4      D               69           D
##65 65      5      E               70           E
##
##66 66      1      B               67           B
##66 66      2      C               68           C
##66 66      3      D               69           D
##66 66      4      E               70           E
##66 66      5      F               71           F
##
##67 67      1      C               68           C
##67 67      2      D               69           D 
##67 67      3      E               70           E
##67 67      4      F               71           F
##67 67      5      G               72           G
##
##68 68      1      D               69           D
##68 68      2      E               70           E
##68 68      3      F               71           F
##68 68      4      G               72           G
##68 68      5      H               73           H
##
##69 69      1      E               70           E
##69 69      2      F               71           F
##69 69      3      G               72           G
##69 69      4      H               73           H
##69 69      5      I                            I

##OUTPUT
##
##A B C D E 
##B C D E F 
##C D E F G 
##D E F G H 
##E F G H I 
