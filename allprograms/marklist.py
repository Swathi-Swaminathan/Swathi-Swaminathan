mark = []
for i in range(5):
    m = int(input('Enter the  mark:'))
    mark.append(m)

print("Total=", sum(mark))
print("Average=", sum(mark)/len(mark))
