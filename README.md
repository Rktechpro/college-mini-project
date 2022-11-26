# college-mini-project
2.1-Python Introduction:-
Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code.
>>> print("Hello, World!")
Hello, World!

2.2-Python modules:-Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.
1-Tkinter:-  Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, Tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python.

import tkinter
m = tkinter.Tk()
'''
widgets are added here
'''
m.mainloop()


2-Base64:- The Base64 encoding is used to convert bytes that have binary or text data into ASCII characters. Encoding prevents the data from getting corrupted when it is transferred or processed through a text-only system. In this article, we will discuss about Base64 encoding and decoding and its uses to encode and decode binary and text data.
variable_name.decode("ascii")
import base64

input_string = "U3Vubnk="
base64_converted_string = input_string.encode("ascii")
decode = base64.b64decode(base64_converted_string)
decimal_converted_string = decode.decode("ascii")
print(decimal_converted_string)
3.MessageBox:- The messagebox module is used to display the message boxes in the python applications. There are the various functions which are used to display the relevant messages depending upon the application requirements.
import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
4.Imagetk:- The ImageTk module contains support to create and modify Tkinter  BitmapImage and PhotoImage objects from PIL images.

photo_image = tk.PhotoImage(file=path_to_image)
