#author : Goodzilam
#tested on Python 3.7.3 and windows 10
#                       For educational purposes
#how to use :
#               *******************************************
#               *******************************************
#               ***** Run as Run module in your idler *****
#               *******************************************
#               *******************************************

#open cmd > type : pip install selenium
#go to "http://chromedriver.chromium.org/downloads" and download the ChromeDriver which matches with your ***version***
#***for finding your chrome version you have to check it at "chrome://settings/help" in your chrome browser***
#then replace the downloaded ChromeDriver path to the marked line in the code

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

#**************************************************************************
chromedriver = "C:/Users/123/Downloads/chromedriver.exe" #replace the path here 
#**************************************************************************


#exaple dorks which can be used with this script :
# site:.com inurl:"index.php?id="

#dork importing
driver = webdriver.Chrome(chromedriver)
Dorkf = open("OrgDorks - Copy1.txt", "r") #replace your file which contains dorks
missed = "Urls which are missed:"
#Googling steps

df = Dorkf.readlines()
for Dork in df:
    try:
        time.sleep(15) #the time is optional but u have to make a dealy for solving the recapthca
        urln = 1
        url = "https://www.google.com/search?newwindow=1&site=&q="+Dork+"&start=0&num=100"
        driver.get(url)
        while(urln != 101): 
            linkf = '//*[@id="rso"]/div/div/div['+str(urln)+']/div/div/div[1]/a'
            sc = driver.find_element(By.XPATH, linkf)
            sc.location_once_scrolled_into_view
            res = sc.get_attribute("href")
            print(res)
            urln = urln + 1
    except:
        missed = missed + " " + Dork + " "
        pass
                
print("done !!!") #at this point your urls are ready and u have to save it as text
Dorkf.close()
