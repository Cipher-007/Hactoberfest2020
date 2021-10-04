import urllib.request
import time
import winsound
def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False
def check():
    if connect():
        print("Connected")
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1500  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    else:
        print('No Internet!')

while True:
    check()
    time.sleep(5)
    
    
