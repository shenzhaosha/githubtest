import time
star = time.time()
time.sleep(3)
for i in range(30):
    print(i)
stop = time.time()
tim = stop-star
print(tim)
