# colors=['red','blue','green']
# print colors[0]
# print colors[2]
# print len(colors)
#
# #does not copy the list
# b=colors
# print b
#
# #for and in
# squares=[1,4,9,16]
# sum=0
# for num in squares:
#     sum+=num
# print sum
#
# #value in collection
# list=['larry','curly','moe']
# if 'curly' in list:
#     print 'yay'
# else:
#     print 'not'
#
# #print the numbers from 0 through 99
# for i in range(100):
#     print i
#
# #access every 3rd element in list
# i=0
# a=[1,2,3,5]
# while i<len(a):
#     print a[i]
#     i=i+3

# list = ['larry','curly', 'moe']
# list.append('shemp')         ##append element at end
# list.insert(0,'xxx')         ##insert element at index 0
# list.extend(['yyy','zzz'])   ##add list of elements at end
# print list
# print list.index('curly')
#
# list.remove('curly')         ##search and remove that element
# list.pop()                   ##removes and returns element of index -1
# list.pop(1)                  ##removes and returns element of index 1
# print list


# list=[1,2,3]
# print list.append(4)           ##does not work, append returns none
#
# list.append(4)                 ##correct pattern
# print list
#
# list=[]                        ##start as the empty list
# list.append('x')               ##Use append() to add elements
# list.append('y')

# list=['a','b','c','d']
# print list[1:-1]                ##returns elements of index 1 and 0
# list[0:2]='z'                   ##replace ['a','b'] with ['z']
# print list
