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
    def __init__(self, master):
        self.entry = None
        self.master = master
        title = tk.Label(self.master, text="Booruu Scraper", font=("Roman", 25)).place(relx=0.05,rely=0.1)
        entryLabel = tk.Label(self.master, text="Website: ").place(relx=0.1,rely=0.2)
        self.entry = tk.Entry(self.master)
        button = tk.Button(self.master, text="Search!",relief=tk.RAISED)
        button.bind("<Button-1>", self.webCheck)
        self.entry.place(relx=0.13,rely=0.2,relwidth=0.5)
        button.place(relx=0.64,rely=0.2)

        # Create a frame to hold the images
        self.image_frame = tk.Frame(self.master)
        self.image_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)
        

    def webCheck(self,master):
        site = self.entry.get()
        '''chromeOptions = Options()
        chromeOptions.add_argument("--headless")'''
        driver = webdriver.Chrome()
        driver.get(site)
        t.sleep(.5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        self.content = soup.find_all("img",class_="post-preview-image",recursive=True)
        self.present()


    def present(self):
        imageSRCRegEx = 'src="(.*?)"'
        dataSetter = re.findall(imageSRCRegEx, str(self.content))
        print(dataSetter)

        scroll_frame = tk.Frame(self.image_frame)
        scroll_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(scroll_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(scroll_frame, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=scrollbar.set)

        row, col = 0, 0
        for img_element in dataSetter:
            print(img_element)
            image = Image.open(urlopen(img_element))
            thumbnail = ImageTk.PhotoImage(image)
            label = tk.Label(self.image_frame, image=thumbnail)
            label.image = thumbnail
            label.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1
        
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        

if __name__ == "__main__":
      
    # Instantiating top level
    root = tk.Tk()
    root.title("Booru Scraper")
    root.geometry("1920x1080")
    app = ScraperApp(root)
    root.mainloop()