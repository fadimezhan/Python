dict={}
dict['a']='alpha'
dict['g']='gamma'
dict['o']='omega'

# print dict
# print dict['a']
# dict['a']=6
# print dict['a']
# print 'a' in dict
# #print dict['z']                  ##KeyError
# if 'z' in dict: print dict['z']
# print dict.get('z')               ##instead of KeyError


# for key in dict:
#     print key
# for key in dict.keys():
#     print key
# print dict.keys()
# print dict.values()

# for key in sorted(dict.keys()):
#     print key,dict[key]
#
# print dict.items()
#
# for k,v in dict.items():
#     print k,'>',v
#


# hash={}
# hash['word']='garfield'
# hash['count']=42
# s='I want %(count)d copies of %(word)s' %hash
# print s
#
# var=6
# print var
# del var
# #print var             ##NameError
#
# list=['a','b','c','d']
# del list[0]
# del list[-2:]
# print list
#
# dict={'a':1,'b':2,'c':3}
# del dict['b']
# print dict

# f=open('gladiator.txt','r')
# dict={}
# for line in f:
#     for word in line.split():
#        word=word.replace(',','').replace('.','').replace('"','').replace("'","").replace('!','').replace('?','').replace(':','')
#        if word in dict:
#            dict[word.lower()]+=1
#        else:
#            dict[word.lower()]=0
#print dict

# for key in dict:
#     print key,dict[key]
#
# for key in sorted(dict.keys()):
#     print key,dict[key]


# for value in sorted(dict.values()):
#      print value
#f.close()


#unicode problems
# import codecs
# f=codecs.open('gladiator.txt','r','utf-8')
# for line in f:
#     print line
