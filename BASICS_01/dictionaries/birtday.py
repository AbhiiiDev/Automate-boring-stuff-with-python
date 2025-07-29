birthday={'John':'2 March','place':'doe palace'}
while True:
    print('Enter your name')
    name=input()
    if name=='':
        break
    
    if name in birthday:
        print(birthday[name]+' is the birthday of '+name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthday[name] = bday
        print('Birthday database updated.')    
