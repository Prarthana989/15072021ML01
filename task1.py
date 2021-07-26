#2----------------------------------------------------------------------------------------------------------------------
'''>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a = 20; a+= 30; a%=3; print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)
False
'''


#3-------------------------------------------------------------------------------------------------------------------------
s1 = "Nice to have it"
s2 = "here"
print(s1 + " " +s2 )



#4-------------------------------------------------------------------------------------------------------------------------
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])




#5-------------------------------------------------------------------------------------------------------------------------
a.insert(0,s1)
a.append(s2)
print(a)


#6--------------------------------------------------------------------------------------------------------------------------
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
b=[]
for i in numbers:
    if i==237:
        break
    else:
        if not(i%2):
            b.append(i)
print(b)



#7---------------------------------------------------------------------------------------------------------------------------
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1 - color_list_2)



#8----------------------------------------------------------------------------------------------------------------------------
def find_pangram(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        if a not in s.lower():
            return False
    return True
    
print(find_pangram("Hello How are you"))



#9------------------------------------------------------------------------------------------------------------------------------
def cal(n):
    sum = n
    for i in range(2,4):
        new = int(str(n)*i)
        sum +=new
    return sum
        
n1 = int(input("enter a single digit number: "))
print(cal(n1))




#10------------------------------------------------------------------------------------------------------------------------------
def filter(i):
    l1=[]
    l2=[]
    for a in range(len(i)):
        if a ==0:
            l1 = [int(n) for n in i[a].split(" ")] 
        else:
            l2=[int(n) for n in i[a].split(" ")]
    return(l1,l2)
    
i1 = input("enter input in the form 23 54 12#98 3 17:").split("#")
x,y=filter(i1)
print(f"x = {x} and y = {y}")




#11-------------------------------------------------------------------------------------------------------------------------------
seq = list(input("enter few words seperated by comma").split(","))
seq.sort()
for i in seq:
    print(i,end=",")

    


#12-------------------------------------------------------------------------------------------------------------------------------
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
l1 = tuple(d['Marks'])
d['Marks'].sort()
print(d['Student'][l1.index(d['Marks'][-1])])




#13-------------------------------------------------------------------------------------------------------------------------------
s = "hello world! 123"
letter =0
number=0
for char in s.lower():
    if (ord(char)>=48 and ord(char)<=57):
        number +=1
    else:
        if(ord(char)>=97 and ord(char)<=122):
            letter +=1
print(f"letter = {letter},number = {number}")




#14-------------------------------------------------------------------------------------------------------------------------------
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

x = list(zip(d['Name'],d['Subject'],d['Ratings']))

y=[]
for i in range(len(x)):
	if x[i][1]== 'Python':
		y.append(x[i])

l1 =[]
l2=[]
l3=[]

for i in range(len(y)):
	l1.append(y[i][0])
	l2.append(y[i][1])
	l3.append(y[i][2])
newData= {}
newData['Name']= l1
newData['Subject']= l2
newData['Ratings']= l3

print(newData)



#16--------------------------------------------------------------------------------------------------------------------------------
t = (('UP',5),('DOWN',3),('LEFT',3),('RIGHT',2))
x = t[0][1]- t[1][1]
y = t[2][1]- t[2][1]
dis = int((((t[0][1]- t[1][1])**2) + ((t[2][1]- t[2][1])**2))**(0.5))
print(f"The distance is : {dis}")
