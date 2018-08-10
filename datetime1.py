import datetime

t = datetime.time(1,15,0)
print(type(t))
print(t.hour)

d = datetime.date.today()
print(d)
d = datetime.date(2018,8,13)
print(d)

dt = datetime.datetime.now()
print(dt)

t0 = datetime.datetime.now()
result = [x**2 for x in range(10000)]
t1 = datetime.datetime.now()
diff = t1 - t0
print(diff.microseconds)
