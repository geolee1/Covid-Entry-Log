import time

t0 = time.time()
print(time.strftime("%I %M %p", time.localtime(t0)))

t1 = t0 + 60*60
print(time.strftime("%I %M %p", time.localtime(t1)))
