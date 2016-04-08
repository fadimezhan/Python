def encrypt(text,value,output=""):
    for char in text:
        output="{}{}".format(output,chr(ord(char)+value))
    return output
def decyrpt(text,value,output=""):
    for char in text:
        output="{}{}".format(output,chr(ord(char)-value))
    return output

print "Enter the value"
value=int(raw_input())

print "Enter the decrypting text:"
text=raw_input()
print encrypt(text,value)

print "Enter the encrypting text:"
text=raw_input()
print decyrpt(text,value)



