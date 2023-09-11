import time
import os
def times():
    return time.strftime('%H:%M:%S %p')

while True: 
    print(times())
    os.system('cls')