name1=raw_input("Enter your name:")
name2=raw_input("Enter your boyfriend's/girlfriend's name:")

calculate=len(name1)+len(name2)
if len(name1)>len(name2):
    calculate-=5
else:
    calculate+=3

calculate*=42
calculate=calculate/(100+len(name2))

if calculate>10:
    calculate=10
else:
    round(calculate,0)
print ("{} and {} score is {} out of 10").format(name1,name2,calculate)
