#Python program to count the no of words and characters in a sentence
i=1
count=0
for i in range(1,4,1):
   sent=input("Enter the sentence:")
   res = len(sent.split())
   print("The number of words in the sentence are:",str(res))
   print("The number of characters in sentence are:",len(sent))

