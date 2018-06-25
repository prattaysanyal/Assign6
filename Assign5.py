#question1
tup=(1,2,"red","orange")
print("length is="+str(len(tup)))

#question2
tup=(1,2,6,4,8)
print("max element is="+str(max(tup)))
print("minimum element is="+str(min(tup)))


#sets question1
set1=set()
x=int(input("enter 1st number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
set1.update([x,y,z])
print(set1)
set2=set()
a=int(input("enter 1st number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
set2.update([a,b,c])
print(set2)

print(set1-set2)
print("on comparing")
if(set1==set2):
    print("sets are same")
else:
    print("sets are not same")

print(" after intersection")
set3=set1&set2
print(set3)


# dictionaries question1
a=int(input("enter 1st marks"))
b=int(input("enter 2nd marks"))
c=int(input("enter 3rd marks"))
x=int(input("enter 4th marks"))
e=int(input("enter 5th marks"))
f=int(input("enter 6th marks"))
g=int(input("enter 7th marks"))
h=int(input("enter 8th marks"))
i=int(input("enter 9th marks"))
j=int(input("enter 10th marks"))
dict={"A":a , "B":b , "C":c , "X":x , "E":e , "F":f , "G":g , "H":h , "I":i , "J":j}
dict["A"]=a
dict["B"]=b
dict["C"]=c
dict["X"]=x
dict["E"]=e
dict["F"]=f
dict["G"]=g
dict["H"]=h
dict["I"]=i
dict["J"]=j
print(dict)
sort = sorted(dict.items(), key=lambda kv: kv[1]) #question2
print(sort)

#question3
print("......printing elements occuring......")
x="MISSISSIPPI"
a=x.count("M")
b=x.count("I")
c=x.count("S")
d=x.count("P")
dict1={"M":a,"I":b,"S":c,"P":d}
dict1["M"]=a
dict1["I"]=b
dict1["S"]=c
dict1["P"]=d
print(dict1)










