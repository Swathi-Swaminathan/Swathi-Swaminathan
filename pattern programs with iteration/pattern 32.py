#pattern 32
for i in range(65,70):
    res=i
    for j in range(5):
        print(chr(res),end=" ")
        res+=5
    print()


##ITERATION
##
##i res=i    j     print(chr(res))  res+=5    print
##
##
##65 65      1      A               70           A
##65 70      2      F               75           F        
##65 75      3      K               80           K
##65 80      4      P               85           P
##65 85      5      U                            U
##
##66 66      1      B               71           B
##66 71      2      G               76           G
##66 76      3      L               81           L
##66 81      4      Q               86           Q
##66 86      5      V                            V
##
##67 67      1      C               72           C
##67 72      2      H               77           H 
##67 77      3      M               82           M
##67 82      4      R               87           R
##67 87      5      W                            W
#
##68 68      1      D               73           D
##68 73      2      I               78           I
##68 78      3      N               83           N
##68 83      4      S               88           S
##68 88      5      X                            X
##
##69 69      1      E               74           E
##69 74      2      J               79           J
##69 79      3      O               84           O
##69 84      4      T               89           T
##69 89      5      Y                            Y

##OUTPUT
##
##A F K P U 
##B G L Q V 
##C H M R W 
##D I N S X 
##E J O T Y 
