#1
a = 80
b = 75
c = 55
d = (a+b+c)/3
print(d)

#2
a = 13
b = a % 2
print(b)

#3
pin = "881120-1068234"
yyyymmdd = pin[:6] 
number = pin[7:] 
print(yyyymmdd) 
print(number)

#4
pin = "881120-1068234"
print(pin[7])  

#5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#6
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#8
a = (1, 2, 3)
a = a + (4,)
print(a)

#9
# a[[1]] = 'python' 
##  File "/Users/mzc01-hyong/python-test/2.되새김.py", line 37, in <module>
##    a[[1]] = 'python' 
## TypeError: 'tuple' object does not support item assignment

#10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)          
print(result)

#11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)     
b = list(aSet)    
print(b)  

#12
a=b=[1,2,3]
a[1] = 4
print(b) 

#13
