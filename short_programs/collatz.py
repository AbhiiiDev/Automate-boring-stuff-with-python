def collatz(num):
    while num!=1:
     print(num,end='=>')
     if num%2==0:
        num= num // 2
     else:
        num=3*num+1
    print(1)

try:
 num=int(input('Enter number'))
 collatz(num)
except:
  print('please enter only numbers')