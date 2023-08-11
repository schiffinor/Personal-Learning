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
        title = tk.Label(self.master, text="Booruu Scraper", font=("Roman", 25))
        title.grid(row=0, column=0, columnspan=2)
        entryLabel = tk.Label(self.master, text="Website: ")
        entryLabel.grid(row=1, column=0)
        self.entry = tk.Entry(self.master)
        self.entry.grid(row=1, column=1)
        button = tk.Button(self.master, text="Search!", relief=tk.RAISED)
        button.bind("<Button-1>", self.webCheck)
        button.grid(row=1, column=2)

        self.canvas = tk.Canvas(self.master)
        self.canvas.grid(row=2, column=0, columnspan=3)

        self.image_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.image_frame, anchor=tk.NW)

    def webCheck(self, master):
        site = self.entry.get()
        driver = webdriver.Chrome()
        driver.get(site)
        t.sleep(.5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        self.content = soup.find_all("img", class_="post-preview-image", recursive=True)
        self.present()

    def present(self):
        imageSRCRegEx = 'src="(.*?)"'
        dataSetter = re.findall(imageSRCRegEx, str(self.content))

        row, col = 0, 0
        for img_element in dataSetter:
            response = req.get(img_element, stream=True)
            if response.status_code == 200:
                image_data = Image.open(BytesIO(response.content))
                thumbnail = ImageTk.PhotoImage(image_data)
                label = tk.Label(self.image_frame, image=thumbnail)
                label.image = thumbnail
                label.grid(row=row, column=col, padx=5, pady=5)

                col += 1
                if col > 2:
                    col = 0
                    row += 1

        # Update canvas scrolling region
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ScraperApp(root)
    root.mainloop()
