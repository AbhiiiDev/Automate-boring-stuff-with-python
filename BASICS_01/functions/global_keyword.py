def localMeinGlobal():
    global eggs
    eggs="global wala bana ab local wala eggs"

eggs="global wala eggs"
localMeinGlobal()
print(eggs)