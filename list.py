our_list =[10,20,30,-50]
print(our_list)
print(type(our_list))
jackson =["A","B","C",1,2,3,"Dutta","Roy",True,False]
print(jackson[4])
print(jackson[-2])
print(jackson[0:3])  #slicing a list
our_list=[1,2,[3,4,5],6,7,8]
print(our_list[2])
print(our_list[2][0])
our_table=[[1,2,3],[4,5,6],[7,8,9]]
print(our_table[0])
print(our_table[1])
print(our_table[2])
print(our_table[0][2])
A=[5,12,72,55,89]
print(A)
A=A+[1]
print(A)
A=A+["bcd"]
print(A)
A=A+list("bcd")
print(A) 
A=A+list(str(123))
print(A)
A=A+[[5,6,7,8]]
print(A)
print(A[-1])
A.append([10,11,12])
print(A)
A=[5,12,72,55,89]
A.insert(2,100)
print(A)
#A=A.insert(2,[1,2,3]) not allowed lists are immutable
A[0]=3
print(A)

