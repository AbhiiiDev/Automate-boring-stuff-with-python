import time,sys
indent=0
indent_increasing=True
try:
    while True:
        print(' '*indent,end='')
        print('********')
        time.sleep(0.1)

        if indent_increasing==True:
            indent=indent+1
            if indent==20:
                indent_increasing=False
        
        else:
            indent=indent-1
            if indent==0:
                indent_increasing=True
except KeyboardInterrupt:
    sys.exit()