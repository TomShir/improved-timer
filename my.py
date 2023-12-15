#Create a Python program that emulates a timer 
from colorama import Fore 
import time 
import sys 
def error_msg(error_message):
    for n in error_message:
        sys.stderr.flush()
        time.sleep(0.01)
        sys.stderr.write(f'{Fore.RED}{n}')
    else:
        print(f'{Fore.RESET}')
try:
    number=int(input('number:'))
    if number>60:
        error_msg('NumericalError:Error,do not input a number above 60')
    else:
     while number+1>0:
        number-=1 
        if number>=10:
            print(f'{Fore.GREEN}00:{number}',end='\r')
            time.sleep(1)
        else:
            print(f'00:0{number}',end='\r')
            time.sleep(1)
     else:
        print(f'{Fore.RESET}')
except ValueError:
    error_msg('Error,not a valid value')