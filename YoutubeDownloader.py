from time import sleep
print("-------------------------------------")
print("|    Youtube Downloader By Gazor    |")
print("| Version 2.1 last update 4/10/2021 |")
print("-------------------------------------")
sleep(2)
print("Youtube Downloader Started Successfuly")
print("Loading | please wait")
import time
import pafy
print("Loaded  | Will ready in 1 second")
sleep(1)
while True:
 video = input("Video Link : ")
 url = pafy.new(video)
 print("------------------------------")
 print("Channel Name  >" + url.author)
 print("------------------------------")
 print("Video Length  >" + url.duration)
 print("------------------------------")
 print("Video Title   >" + url.title)
 print("------------------------------")
 dn = url.getbest()
 dn.download()
 print("---------------------------------------")
 print("Video Download Success or already exist")
 print("---------------------------------------")

 print ("Do you want to download more video?")
 print ("Yes | type 1")
 print ("No | type 2")
 print ("Typing except 1 and 2 the program will close automaticly")

 option = input("Choose option : ");
 if not option in ('1','2'):
     print("Error")  
     exit();   
    
 if option == '1':
   continue;
 elif option == '2':
   exit();