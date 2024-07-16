import datetime, time

curr = time.time()
print("Seconds since January 1, 1970:", f"{curr:,.4f}", "or", "{:.2e}".format(curr), "in scientific notation")

x = datetime.datetime.now()
print(x.strftime("%b %d %Y"))

