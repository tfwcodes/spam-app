# all the imports I am gonna use for the app
import pyautogui
import threading
from time import sleep

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4'
   END = '\033[0m'
   CWHITE  = '\33[37m'


print(
color.BLUE + """
              _ __ ___   ___  __ _  __ _ ___ _ __   __ _ _ __ ___  
             | '_ ` _ \ / _ \/ _` |/ _` / __| '_ \ / _` | '_ ` _ \ 
             | | | | | |  __/ (_| | (_| \__ \ |_) | (_| | | | | | | ~> Made by tfwcodes(github)<~
             |_| |_| |_|\___|\__, |\__,_|___/ .__/ \__,_|_| |_| |_| ~~> Spamming app, hope you enjoy it:) <~~ 
                             |___/          |_|
""")
# The word/preposition to spam
x = input(color.PURPLE + "Enter the word/proposition you want to spam: ")
# The time to sleep untill the programm starts to spam
time_sleep = int(input(color.PURPLE + "Enter the time you want to stay untill the programm wil start to spam: "))
# the number of threads to spam
number_of_threads = input(color.PURPLE + "Enter the number of threads: ")


def gg():
   str(sleep(time_sleep))
   # while loop to spam with the variable x 
   while True:
      # write x
      pyautogui.write(x + "\n")
      # press
      pyautogui.press("enter")

# The list of the threads   
threads = []
# start to spam with the variable number_of_threads
for i in range(int(number_of_threads)):
   #threading.Thread with the target gg
   t = threading.Thread(target=gg)
   t.daemon = True
   threads.append(t)

for i in range(int(number_of_threads)):
   #start the threads
   threads[i].start()

for i in range(int(number_of_threads)):
   #join the threads
   threads[i].join()