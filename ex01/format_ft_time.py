import datetime,time

x = datetime.datetime.now()
ts = time.time()

print("Seconds since January 1, 1970:",f"{ts:,.4f}","or",f"{ts:.2e}", "in scientific notation")
print(x.strftime("%b %d %Y"))
