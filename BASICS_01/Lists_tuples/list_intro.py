def traversing(lists):
    print('travsering using functions :')
    for i in range(len(lists)):
     print('Index at '+str(i)+' = '+lists[i])
lists=['hey','hi','hola','Howdy']
traversing(lists)

print('travsering through slice :')
print(lists[:])