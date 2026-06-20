import datetime

date = datetime.date(2024, 11, 16)
today = datetime.date.today() 

time = datetime.time(12, 41, 41)
now = datetime.datetime.now()
now_str = datetime.datetime.now().strftime("%H:%M:%S")      #strftime is string format time 
                                                            #%H,%M etc can be find online for strftime
print(date)
print(today)
print(time)
print(now)
print(now_str)

target_date = datetime.datetime(2020, 1, 2, 12, 30, 0)
current_date = datetime.datetime.now()

if target_date < current_date:
    print("Target date has passed")
else:
    print("Target has not passsed")  

print(target_date)      