#python program to print roundsum
def round_sum(a,b,c):
  return round(a) + round(b) + round(c)

def round(num):
    n=num%10
    if(n>=5):
        return (num-n+10)
    else:
        return (num-n)


print("round_sum(16,17,18) is =",round_sum(16,17,18))
print("round_sum(12,13,14) is =",round_sum(12,13,14))
print("round_sum(6,4,4) is =",round_sum(6,4,4))
