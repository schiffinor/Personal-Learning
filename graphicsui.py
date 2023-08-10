import tkinter as tk

class GraphicsUI:
    def __init__(self, master):
        self.master = master
        master.title("3D Graphics Engine")
        
        self.label = tk.Label(master, text="Welcome to the 3D Graphics Engine!")
        self.label.pack()
        
        self.display_button = tk.Button(master, text="Display 3D Scene", command=self.display_scene)
        self.display_button.pack()
        
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()
        
    def display_scene(self):
        # Code to call your 3D graphics engine to display the scene
        print("Displaying the 3D scene...")

root = tk.Tk()
app = GraphicsUI(root)
root.mainloop()