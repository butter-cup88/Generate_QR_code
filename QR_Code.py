from tkinter import *
import pyqrcode
import png 
from tkinter import filedialog
from PIL import Image, ImageTk
import PIL.Image
from tkinter import *
import ttkbootstrap as tb

root=tb.Window(themename="vapor")

root.title("Generating QR Codes")

#on Ubuntu
#root.iconphoto(False, PhotoImage(file='/media/buttercup/Expecto_Patronum/Python_Examples/QR_Code.png'))

#on windows
root.iconphoto(False, PhotoImage(file='K:/Python_Examples/QR_Code.png')) #make sure this points to a file on ur machine or u can comment out this line of code

root.geometry('500x350')

def create_code():
    #File Dialog
    input_path=filedialog.asksaveasfilename(title="Save Image", filetype=(("PNG File", ".png"),
                                                                          ("All Files", "*.*")))
    if input_path:
        #if the user inputs '.png' at the end of file name
        if input_path.endswith(".png"):
            #Create QR Code from entry box
            get_code=pyqrcode.create(my_Entry.get())
            
            #Save as PNG file
            get_code.png(input_path, scale=6, module_color="#c96605",
                                     background="#121e38")
        #if the user does not put '.png' at the end of file name
        else:
            #Add that .png to the end of the file name
            input_path=f'{input_path}.png'
            
            #Create QR code from entry box
            get_code=pyqrcode.create(my_Entry.get())
            
            #Save as PNG file. 
            #Change module_color and background color if output noes not meet ur color requirement. Below code has navy blue as bgcolor and orenge as fgcolor.
            get_code.png(input_path, scale=6, module_color="#c96605",
                                     background="#121e38")
        
        #Put QRcode on screen
        global get_image
        get_image=ImageTk.PhotoImage(PIL.Image.open(input_path))
        
        #Add image to label
        my_Label.config(image=get_image)
        
        #Delete Entrybox
        my_Entry.delete(0, END)
        
        #Flash up finished
        my_Entry.insert(0, "Finished!!")

def clear_all():
    my_Entry.delete(0,END)
    my_Label.config(image='')


#Creating the GUI
my_Label1=tb.Label(root, text="Enter the URL to be used to generate the QR code",
                   font=("Helvetica", 14))
my_Label1.pack(pady=10)

my_Entry=tb.Entry(root, bootstyle="success", font=("Helvetica", 14),
                  foreground="red",
                  width=40)
                  #show="*")
my_Entry.pack(pady=0)

my_button=tb.Button(root, bootstyle="danger, outline", text="Generate Code", 
                    command=create_code)
my_button.pack(pady=20)

my_button2=tb.Button(root, bootstyle="danger, outline", text="Clear",
                    command=clear_all)
my_button2.pack(pady=20)

my_Label=tb.Label(root, text="")
my_Label.pack(pady=20)





root.mainloop()
