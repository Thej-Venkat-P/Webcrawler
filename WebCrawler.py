from selenium import webdriver
import time
from threading import Thread
import sys
from selenium.webdriver.common.by import By

print("Thej Venkat P")
print("1DT21CS171")
print("Python WebCrawler Mini Project")
print()
driver = webdriver.Chrome(executable_path=r"C:\Users\Thej Venkat\Desktop\Projects\WebCrawler\chromedriver.exe")
driver.get('https://www.google.com')
l=[]

def printl():
    global leave
    n=-1
    while n:
        print()
        print("0 : Quit")
        print("1 : Visit a given URL")
        print("2 : Enter to print current site and list of all URLs visited")
        print("3 : Print all available URLs in the Current Webpage")
        n=int(input("Choice:"))
        if n==2:
            print()
            print("Current Link:",l[-1])
            print("Previously visited Links:")
            for i in range(len(l)):
                print(i+1,":",l[i])
            print()
            print("Visit a Previously visited URL:")
            print("0 : Stay on the Current Webpage")
            print("m : Visit M th URL in the list")
            m=int(input("m:"))
            if m==0:
                continue
            elif m in range(1,len(l)+1):
                visit(l[m-1])
            else:
                print("Invalid Value for m")
                continue
        elif n==1:
            print()
            s=input("Enter Valid URL:")
            try:
                visit(s)
            except:
                print("Invalid URL")
        elif n==3:
            availableURLs=getUrls()
            print()
            print("Visit URL that is Available on the Current Webpage:")
            print("0 : Stay on the Current Webpage")
            print("m : Visit M th URL in the list")
            m=int(input("m:"))
            if m==0:
                continue
            elif m in range(1,len(availableURLs)+1):
                visit(availableURLs[m-1])
            else:
                print("Invalid Value for m")
                continue
    leave=True
        
def visit(url):
    driver.get(url)

def getUrls():
    urls=driver.find_elements(By.TAG_NAME, "a")
    urls=[i.get_attribute("href") for i in urls]
    print()
    print("URLs Available on this Webpage are:")
    for i in range(len(urls)):
        print(i+1,":",urls[i])
    return urls

def getclink():
    global l
    while not leave:
        current_url = driver.current_url
        if current_url not in l:
            l.append(current_url)
        else:
            l.remove(current_url)
            l.append(current_url)
        time.sleep(1)

leave=False
t1 = Thread(target=printl, args=())
t2 = Thread(target=getclink, args=())

t1.start()
t2.start()

t1.join()
t2.join()
driver.close()
print("Done!")
