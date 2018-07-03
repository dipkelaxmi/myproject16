#assg:2==set operations
A=set([1,2,3,4]);
B=set([1,3,4,5,6,7,8]);
print("set A:")
print(A)
print("length of set A=")
print(len(A))
print("set B:")
print(B)
print("length of set B=")
print(len(B))
print("union of set==")
print(A.union(B))
print("intersection of set==")
print(A.intersection(B))
print("difference ==")
print(A-B)
print("symmetric difference==")
print(A^B)
print("difference ==")
print(B-A)
print('Is there 2 in set A ? :',2 in A)
print('is there 5 in set A ? :',5 in A)
print('is there 5 in set B ? :',5 in B)
print('is there 9 in set B ? :',9 in B)
print('Union of A and B :',A | B)  
print('Common in A and B :',A & B)
print('Unique in A and B :',A ^ B)
print('Elements which are in set A but not in set B : ',A - B)
print('Elements which are in set B but not in set A : ',B - A)



