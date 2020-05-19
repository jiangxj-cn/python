import string,random
import math
#6bytes
capta=''
words=''.join((string.ascii_letters,string.digits))
for i in range(6):
    capta+=random.choice(words)
print(capta)
print(words)
#input
#name = input('please input your name:')
#print(name)
#math
value=199**99
print(value)
value=0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1
print(value)
#image
print('   *','\n',' * *','\n','* * *')
#math
x=2
value=x**2-4
print(value)

value=6*(x/7)
print(value)

value=6/(4+5*x)
print(value)

#page_26_sample_3
a=input('please input the char:')
print(' '+a*4,'\n',a,'\n',a*4,'\n',a+'  '+a,'\n',a*4)


#page_44_sample
num=input('please input a number:')
print(int(num)**2)

'''
list=[]
value=input('please input a num1:')
list.append(int(value));
value=input('please input a num2:')
list.append(int(value));
value=input('please input a num3:')
list.append(int(value));
value=input('please input a num4:')
list.append(int(value));
value=input('please input a num5:')
list.append(int(value));
print(list[1:5:2])
'''
print({'a':1,'b':2})

print(dict({'a':1,'b':2}))

value={'a':1}
value.update({'b':2})
print(value)
x=(int(input('please input a num1:')),int(input('please input a num2:')))
x1=min(x)
x2=max(x)
for value in range(x1,x2+1):
    for i in range(2,value-1):
        if value%i==0:
            break
    else:
        print(value,"is right.")

for i,item in enumerate('jiang'):
    print('%d:%s'%(i,item))

for i in sorted([3,1,3,1,22,4,6]):
    print(i)

for i in sorted('jiang'):
    print(i)

for i in reversed([3,1,3,1,22,4,6]):
    print(i)

for i in reversed('jiang'):
    print(i)

lsta=(1,2)
lstb=(3,4)
lstc=(5,6,7,8)
for i,j,k in zip(lsta,lstb,lstc):
    print('%d:%d:%d'%(i,j,k))

square_odd=[i**i for i in range(1,11) if (i**i)%2==0]
for i in square_odd:
    print(i)

def hello(name='Python'):
    print('hello,%s!'%name)

hello()
hello('jack')

class MyClass:
    pass
print(dir(MyClass))




