t=tuple()
print(type(t))
print(t)

t1=(1,2,3,'A','K','t')
print(t1)

t2=1,2,3,4,5
print(type(t2))
print(t2)

for i in t2:
  print(i)

print(t2[2])

t=(1,2,3)
print(t)

#t[2]=111 ERROR GENERATING CODE COZ ITS IMMUTABLE
#print(t)

t1=(111,222,333,444)
for i in t1:
      print(i)


#t1clear() AS T1 IS NOT MUTABLE TO CLEAR WILL NOT WORK ON IT
#print(t1)

t3=tuple(range(1,11))
print(t3)

t4=("bangalore")
print(t4)

print(type(t4))

t4=("bangalore",)
print(t4)

t5=(1,2,0,5,10,11,3,111)
t_l=sorted(t5)
print(t_l)

print(min(t5))
print(max(t5))

a=10
b=20
c=30
t6=a,b,c  #tuple packing
print(t6)



