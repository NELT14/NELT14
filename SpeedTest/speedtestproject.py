from threading import Thread
import speedtest
from colorama import init, Fore
from os import system
import time
init()


#Creating the class with information about speedtest
class speedresults:
    def __init__(self) -> None:
        self.finisheddown = False
        self.finishedup = False

    def start(self) -> None:
        self.common = speedtest.Speedtest()
        self.download = ('%.2f Mbit/s' % (self.common.download() / 1e6))
        self.finisheddown = True
        self.upload = ('%.2f Mbit/s' % (self.common.upload() / 1e6))
        self.finishedup = True


# I think you already understood this line
res = speedresults()

# Function for running the function which runs the speedtest from class


def start():
    global res
    res.start()


# Creating thread function
mainthread = Thread(target=start)

# Running thread function
mainthread.start()

# Creating loading animation while result of download speed isnt done
while not res.finisheddown:
    print(f'{Fore.WHITE}Testing {Fore.RED}Download: {Fore.WHITE}\\', end='\r')
    time.sleep(0.2)
    print(f'{Fore.WHITE}Testing {Fore.RED}Download: {Fore.WHITE}|', end='\r')
    time.sleep(0.2)
    print(f'{Fore.WHITE}Testing {Fore.RED}Download: {Fore.WHITE}/', end='\r')
    time.sleep(0.2)
    print(f'{Fore.WHITE}Testing {Fore.RED}Download: {Fore.WHITE}__', end='\r')

# Printing result of download speed at console
print(f'{Fore.WHITE}Download Speed: {Fore.RED}{res.download}')

# Creating loading animation while result of upload speed isnt done
while not res.finishedup:
    print(f'{Fore.WHITE}Testing {Fore.GREEN}Upload: {Fore.WHITE}\\', end='\r')
    time.sleep(0.2)
    print(f'{Fore.WHITE}Testing {Fore.GREEN}Upload: {Fore.WHITE}|', end='\r')
    time.sleep(0.2)
    print(f'{Fore.WHITE}Testing {Fore.GREEN}Upload: {Fore.WHITE}/', end='\r')
    time.sleep(0.2)
    print(f'{Fore.WHITE}Testing {Fore.GREEN}Upload: {Fore.WHITE}__', end='\r')


# Printing result of upload speed at console
print(f'{Fore.WHITE}Upload Speed: {Fore.GREEN}{res.upload}')

#Changing color to white and pausing our program because otherwise the program will be closed
print(Fore.WHITE)
system(f'pause')
