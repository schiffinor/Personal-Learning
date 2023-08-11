import requests as req
from bs4 import BeautifulSoup
import re
import tkinter as tk
import customtkinter as ctk
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
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        title = ctk.CTkLabel(self.master, text="Booruu Scraper", font=("Roman", 25)).place(relx=0.05,rely=0.1)
        entryLabel = ctk.CTkLabel(self.master, text="Website: ").place(relx=0.1,rely=0.2)
        self.entry = ctk.CTkEntry(self.master)
        button = ctk.CTkButton(self.master, text="Search!")
        button.bind("<Button-1>", self.webCheck)
        self.entry.place(relx=0.13,rely=0.2,relwidth=0.5)
        button.place(relx=0.64,rely=0.2)

        # Create a frame to hold the images
        self.image_frame = ctk.CTkFrame(self.master)
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
        
        scroll_frame = ctk.CTkFrame(self.image_frame)
        scroll_frame.pack(fill=tk.BOTH, expand=True)

        canvas = ctk.CTkCanvas(scroll_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ctk.CTkScrollbar(scroll_frame, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

        row, col = 0, 0
        for img_element in dataSetter:
            response = req.get(img_element, stream=True)
            if response.status_code == 200:
                image_data = Image.open(BytesIO(response.content))
                thumbnail = ImageTk.PhotoImage(image_data)
                label = tk.Label(canvas, image=thumbnail)
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
    root = ctk.CTk()
    root.title("Booru Scraper")
    root.geometry("1920x1080")
    app = ScraperApp(root)
    root.mainloop()