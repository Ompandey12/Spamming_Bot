import pyautogui as pt
import time
import random
while True:
    print("Let's See how good you are")
    print("1.I will not spam")
    print("2.Spamming is my life")
    print("Press any other key to exit")
    n=eval(input("Enter your choice"))
    if n==1:
       print("Tumhe puruskrit karenge")
    elif n==2:
       print("Bahut Galat aadmi hai yeh!!")

       print("Phir bhi apni iksha puri karle")
       p = eval(input("Enter number of different types of messages that you want to spam"))
       a=[]
       for j in range(1,p+1):
           message = input("Enter message")
           a.append(message)
       limit = input("Enter limit")

       i=0
       time.sleep(3)
       while i<int(limit):
            pt.typewrite((random.choice(a)))
            pt.press("enter")
            i=i+1
    else:
       print("Thank you for playing")
       break



