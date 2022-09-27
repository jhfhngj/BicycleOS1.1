import time
import datetime
print("Welcome to BicycleOS!")
time.sleep(1)







def infinite():
    while True:
        yield


for __ in infinite():
    cmd = input("bicycleos:")

if cmd == "calc":
    print("Welcome to Calculator version 1.0!")
    time.sleep(3)
    calctype = input("What type do you want to calculate with?")



if calctype == "times":
    p = input("First number:")
    pp = input("Second number:")
    
if p == 3 and 2 == 3:
    ppp = print("9 is the result")

if calctype == "exit":
    print("Exited Calc.")

