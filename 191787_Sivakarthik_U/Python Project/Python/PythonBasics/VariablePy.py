f=101
e=111
print(f)
print(e)
def somefuntion():
    global f
    print(f)
    f= "Changing the Global Variable"


somefuntion()
print(f)
del e
print(e)



