import datetime
import random
import time

minutes = [1, 2, 34, 4, 5]

right_now_minutes = datetime.datetime.today().minute

for i in range(10):
    if right_now_minutes in minutes:
        print("minute in 1,2,3,4,5")
    else:
        print("minute not here")
    wait_time = random.randint(1, 10)
    time.sleep(wait_time)
