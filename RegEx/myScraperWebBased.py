import eel
import requests as req
from bs4 import BeautifulSoup
import re
import tkinter as tk
import time as t
from io import BytesIO
from PIL import Image,ImageTk
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ScraperApp:
    def __init__(self):
        self.entry = None


    def webCheck(self):
        site = self.entry
        driver = webdriver.Chrome()
        driver.get(site)
        t.sleep(.5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        self.content = soup.find_all("img",class_="post-preview-image",recursive=True)
        imageSRCSet = self.present()
        return imageSRCSet
        


    def present(self):
        imageSRCRegEx = 'src="(.*?)"'
        dataSetter = re.findall(imageSRCRegEx, str(self.content))
        print(dataSetter)
        return dataSetter
        

@eel.expose
def fetch(data):
    myData = data
    return myData

@eel.expose
def fetchSearch(data):
    app = ScraperApp()
    myData = data
    print(data)
    app.entry = myData
    SRCSet = app.webCheck()
    return SRCSet 


if __name__ == "__main__":
    eel.init("webUI")
    eel.start("UIAttempt.html")
    