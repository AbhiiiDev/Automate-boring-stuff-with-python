def listToString(spam):
        for index,item in enumerate(spam):
         if index==len(spam)-1 and len(spam)>1:
          print('and '+item)
         elif len(spam)==1:
            print(item)
         else:
            print(item+', ',end='')
       

spam=['apple','guava']
listToString(spam)