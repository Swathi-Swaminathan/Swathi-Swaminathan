import random
questions = {"What is the radix number for binary?":
["a.2",
"b.3",
"c.4",
"d.5","a"],
"What is the radix number for decimal?":
["a.20",
"b.10",
"c.35",
"d.12","b"],
"What is the radix number for octal?":
["a.7",
"b.6",
"c.8",
"d.9","c"],
"What is the radix number for Hexadecimal?":
["a.15",
"b.18",
"c.20",
"d.16","d"],
"What is 1 byte equals to?":
["a.8 bits",
"b.12 bits",
"c.16 bits",
"d.9 bits","a"],}
questions = list(questions.items())
random.shuffle(questions)
questions = dict(questions)
count = 0
for i in questions.keys():
    print(i)
    for j in range(0,len(questions[i])-1,1):
        print(questions[i][j])
    answer = input("Enter your answer : ")
    if answer == questions[i][len(questions[i])-1]:
        count +=1
print("Total Score:",count)

