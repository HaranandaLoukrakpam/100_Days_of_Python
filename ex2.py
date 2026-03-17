import time

current_time = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(formatted)

hour=time.strftime("%H")
print(hour)

if(hour<"12"):
    print("Good morning")
elif("12"<=hour<"18"):
    print("Good Afternoon")
elif("18"<=hour<"20"):
    print("Good Evening")
else:
    print("Good night")