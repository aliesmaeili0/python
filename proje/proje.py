def reverse_countdown(seconds):
    while seconds > 0:
        print(seconds)
        seconds -= 1
        # تاخیر یک ثانیه
        current_time = 0
        while current_time < 5000000:
            current_time += 1

def timer(seconds):
    while seconds > 0:
        print(f"{seconds} ثانیه مانده")
        seconds -= 1
        # تاخیر یک ثانیه
        current_time = 0
        while current_time < 5000000:
            current_time += 1
    print("زمان تمام شد!")

# شمارش معکوس به مدت ۵ ثانیه
reverse_countdown(5)

# تایمر به مدت ۳۰ ثانیه
timer(10)
