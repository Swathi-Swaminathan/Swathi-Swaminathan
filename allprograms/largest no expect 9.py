sent=input("Enter a sentence:")
l=[]
a=sent.split()
for word in a:
    if word.isdigit():
        if '9' not in word:
            l.append(int(word))
if(len(l))>0:
    print(max(l))
else:
    print("-1")

    
