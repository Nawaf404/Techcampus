import math
import datetime
import sys
import webbrowser
import hashlib
import socket

a = ("==========\n"
     "======Nawaf======"
     "\n==========")
today = datetime.datetime.now()
print("Current date Today : \n" , today)
print(a)
First_name = (input("type First name = "))
Last_name = (input("type Last name = "))
#for type(First_name and Last_name) == int
        #print("Error Input ")
  #  else:
 #       print("Welcome .. ! ")

    #    continue


print("\nHello " + str.lower(First_name) , str.lower(Last_name) , "\n" , "\n")


user = input("Choose Any Opreator : \n"
                 "1- Count how many words in text. \n"
                 "2- split words \n"
                 "3- count from 1 - to any no \n"
                 "4- len words\n"
                 "5- capitalize word\n"
                 "6- lower all of the words\n"
                 "7- how my old\n"
                 "8- delete whitespaces \n"
                 "9- all of words is capital \n"
                 "10- replace anyword to other words \n"
                 "11- Math \n"
                 "12- Cyper SECURiTY = Get iP Address \n"
                 "13- Crypto Password \n"
                 "14- Search in Google \n"
                 "15- Create File :) \n"
                 "16- Dict\n "
                 "?\n \n Choose ? \n= ")

if user == "1":
        count = input("enter text to count ==> ")
        whats_word = input("what's word you want count it ? ")
        if whats_word in count:
            print("i found it : ", whats_word)
        if whats_word not in count:
            print("not here . ")
        print(count.count(whats_word))
else:
    if user == "2":
        split_word = input('type words here to split ==> \n')
        arr = split_word.split(' ')
        for element in arr:
            print(element)
    if user == "13":
        print("Crypto Password ==> \n")
        password = input("Please Enter the password : ")
        byte_Password = bytes(password, 'utf-8')
        hash_password = hashlib.sha1(byte_Password)
        new_Password = hash_password.hexdigest()
        print(new_Password)

        md5OrNo= input("\nDo you want crypto By MD5() ? \nY/n\n")
        if md5OrNo == "Y":

            password = input("Please Enter the password : ")
            byte_Password = bytes(password, 'utf-8')
            hash_password = hashlib.md5(byte_Password)
            new_Password = hash_password.hexdigest()
            print(new_Password)

