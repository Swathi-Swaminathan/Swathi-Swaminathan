#Python program to check result
a=input("Enter your REGISTER NO:")
list1=['21ECE001','NANDHINI',90,91,92,93,99]
list2=['21ECE002','NIVESHA',91,92,93,98,80]
list3=['21ECE003','SHREYA',48,60,70,93,89]
list4=['21ECE004','KAVIYA',80,91,92,73,84]
list5=['21ECE005','PUNITHA',49,76,72,63,94]
if a==list1[0]:
    print("Your result is:",list1)
    x=list1[2]+list1[3]+list1[4]+list1[5]+list1[6]
    print("Total marks=",x)
    if x>380:
        print("Congratulations you have passed the exams")
    else:
        print("Failed")
elif a==list2[0]:
    print("Your result is:",list2)
    x=list2[2]+list2[3]+list2[4]+list2[5]+list2[6]
    print("Total marks=",x)
    if x>380:
        print("Congratulations you have passed the exams")
    else:
        print("Failed")
elif a==list3[0]:
    print("Your result is:",list3)
    x=list3[2]+list3[3]+list3[4]+list3[5]+list3[6]
    print("Total marks=",x)
    if x>380:
        print("Congratulations you have passed the exams")
    else:
        print("Failed")
elif a==list4[0]:
    print("Your result is:",list4)
    x=list4[2]+list4[3]+list4[4]+list4[5]+list4[6]
    print("Total marks=",x)
    if x>380:
        print("Congratulations you have passed the exams")
    else:
        print("Failed")
elif a==list5[0]:
    print("Your result is:",list5)
    x=list5[2]+list5[3]+list5[4]+list5[5]+list5[6]
    print("Total marks=",x)
    if x>380:
        print("Congratulations you have passed the exams")
    else:
        print("Failed")
else:
    print("Please check your register number!!!")
    
