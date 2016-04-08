#import math as m
#sin=m.sin
#print m.sin(60)
#print sin(60)

#from math import sin,cos
#print sin(60)

#belgeler istihza
#omdb api


#dict={}
#dict['a']=123
#dict['b']=345

#print dict.keys()
#print dict
#print dict.values()
#print dict['b']
#dict['x']='3'
#print dict


f=open('gladiator.txt','r')
dict={}
count=0
for line in f:
     for word in line.split():
         word=word.replace(',','').replace('"','').replace("'","").replace('.','')
         if word.lower() in dict:
            dict[word.lower()]+=1
         else:
             dict[word.lower()]=1
#print dict

#for key in sorted(dict.keys()):
#    print key,dict[key]

for value in sorted(dict.values()):
    print value

