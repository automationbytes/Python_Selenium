import traceback
import time
def divide(a,b):
    print(a/b)

#divide(10/"a")

try:
    divide(10,0)
except:
    print("division not possible")
    traceback.print_exc()


x = -1
if x<0:
    raise Exception("Please enter the number greater than Zero")
