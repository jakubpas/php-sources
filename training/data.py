import datetime

def daty():
    """ Return date """
    idx = 1
    while True:
        idx = idx + 1
        yield datetime.timedelta(idx)
      
for x in range(100):
    print daty().next()
    