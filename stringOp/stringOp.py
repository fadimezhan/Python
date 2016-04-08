s = 'hi'
print s[0]
print len(s)
print s + ' there'

pi = 3.14
text = 'The value of pi is ' + str(pi)
print text

raw = r'This\n\t and that'
print raw

raw = 'This\n\t and that'
print raw

multi = """dsgsmkdsjlasjfalsdf
sdjkfahfkjsd
skjdhfkjshfkjs"""
print multi

s = 'hello world'
print s.upper()
print s.lower()
print s.lower().upper()

s1 = '     hello  world     '
print s1.strip()

print s1.isdigit()
print s1.isalpha()
print s1.isspace()

print s1.startswith('other')
print s1.endswith('other')
print s1.find('hello')
print s1.replace('l', '*')
print s1.split()
print s1.split(' ')
print s1.join(['aaa', 'bbb', 'ccc'])

text1=("%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down'))
print text1

ustring=u'A unicode \u018e string \xf1'
print ustring


