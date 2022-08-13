import tkinter as tk
from tkinter import *
from PIL import Image
from tkinter import filedialog
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import colorchooser

def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "D:\yashs\Pictures\Screenshots",
										title = "Select a File",
										filetypes = (("all files",
														"*.*"),
                                                        ("Text files",
														"*.txt*")
													))
	
	label_file_explorer.configure(text="File Opened: " + filename)
	outputMeme(filename)
	
def outputMeme(pathIMG):
	im = Image.open(pathIMG)
	newsize = (800, 700)
	W = 800;
	H =  700;
	im = im.resize(newsize)
	inp = inputTextTop.get(1.0, "end-1c").strip()
	inp1 = inputTextBottom.get(1.0, "end-1c").strip()
	im1 = ImageDraw.Draw(im)
	myFont = ImageFont.truetype('Impacted.ttf', 65)
	color_code = colorchooser.askcolor(title ="Choose font color")
	im1.text((W/2, H/2-350), inp, font=myFont, fill=(int(color_code[0][0]),int(color_code[0][1]), int(color_code[0][2])), anchor="ma")
	im1.text((W/2, H/2+250), inp1, font=myFont, fill=(int(color_code[0][0]),int(color_code[0][1]), int(color_code[0][2])), anchor="ma")
	im.show()


window = Tk()

window.title('Meme Creator')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 500

x_coord = (screen_width/2) - (window_width/2)
y_coord = (screen_height/2) - (window_height/2)

window.geometry(f"{window_width}x{window_height}+{int(x_coord)}+{int(y_coord)}")

window.config(background = "white")

label_file_explorer = Label(window,
							text = "Select an image",
							width = 75, height = 4,
							fg = "blue")

	
button_explore = Button(window,
						text = "Browse Images and generate Meme",
						command = browseFiles)

button_exit = Button(window,
					text = "Exit",
					command = exit)

label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)

label_top_text = Label(window,
							text = "Enter top text",
							width = 75, height = 4,
							fg = "blue").grid(column=1, row=5)

label_bottom_text = Label(window,
							text = "Enter bottom text",
							width = 75, height = 4,
							fg = "blue").grid(column=1, row=7)

inputTextTop = tk.Text(window,
                   height = 5,
                   width = 20)
  
inputTextTop.grid(column = 1,row = 6)

inputTextBottom = tk.Text(window,
                   height = 5,
                   width = 20)
  
inputTextBottom.grid(column = 1,row = 8)
window.mainloop()