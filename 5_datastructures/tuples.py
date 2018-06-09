#tuple cannot be changed once it created so it is immutable
our_tuple =1,2,3,"a","b","c"
print(type(our_tuple))
our_tuple =(1,2,3,"a","b","c")
print(type(our_tuple))
print(our_tuple[0:3])
#our_tuple[2]=100 not allowed but possible in list

C =[1,2,3]
print(C)
print(tuple(C))
print(C)
C=tuple(C)
print(C)
(A,B,C)=1,2,3  #tuple
print(A)
print(B)
print(C)
D,E,F=[1,2,3]  #list
print(D)
print(E)
print(F)
G,H,I="789"    #string
print(G)
print(H)
print(I)
