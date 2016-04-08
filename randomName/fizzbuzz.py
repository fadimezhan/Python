def fizzbuzz(n):
    if(n%5==0 and n%3==0):
        return "fizzbuzz"
    elif(n%5==0):
        return "buzz"
    elif(n%3==0):
        return "fizz"
    else:
        return n


length=int(raw_input("Enter the length of array:"))

for i in range(1,length):
    print fizzbuzz(i)