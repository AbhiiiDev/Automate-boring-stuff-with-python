message='I Love You.'
count={}
for char in message:
    count.setdefault(char,0)
    count[char]=count[char]+1
print(count)