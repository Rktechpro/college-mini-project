from tkinter import messagebox
from tkinter import* 
import tkinter
from PIL import ImageTk,Image
import base64



secren=Tk()
# Frontend 
secren.geometry("500x500")
secren.title("Text Encryption and Decryption ")
global data
secren.configure(bg="lightblue")
# secren1-encrypted 
def encrypt():
    password=code.get()
    if(password=="1010"):
       secren1=Toplevel(secren)
       secren1.title("Encryptions")
       secren1.geometry("400x400")
       secren1.configure(bg="lightblue")
       message=text.get(1.0,END)
       encode_text=message.encode("ascii")
       base64_bytes=base64.b64encode(encode_text)
       encrypt=base64_bytes.decode("ascii")
       
       label3=Label(secren1,text=" The Code is Encrypted",font=("Courier","24","bold"),bg="lightblue")
       label3.place(x=20,y=40)
       img1=ImageTk.PhotoImage(Image.open("image/encrpt.png"))
       Label(secren1,image=img1).place(x=565,y=0,height=850,width=800)
       #text1
       text1=Text(secren1,font="20",bd=3,wrap=WORD)
       text1.place(x=50,y=150,width=400,height=200)
       text1.insert(END,encrypt)
    #button Encrypted
       Button(secren1,text="Select",font=("Courier ","18","bold"),bd=5,bg="blue",fg="black",command=lambda:select()).place(x=60,y=400,width=100)

       Button(secren1,text="cut",font=("Courier ","18","bold"),bd=5,bg="red",fg="black",command=lambda:cut()).place(x=190,y=400,width=100)

       Button(secren1,text="Copy",font=("Courier ", "18","bold"),bd=5,bg="gold",fg="black",command=lambda:copy()).place(x=320,y=400,width=100)
       def  select():
             text1.tag_add("sel", "1.0","end") # all text selected
             text1.tag_config("sel",background="gray",foreground="black")

       def cut():
        global data 
        if text1.selection_get():
          data=text1.selection_get() # copy selected text to clipboard 
          text1.delete('sel.first','sel.last') # delete selected text 

       def copy():
        global data 
        if text1.selection_get():
           data=text1.selection_get() 

    elif(password==""):
        messagebox.showerror("error", "please enter the secret key")
    elif(password!="1010"):
        messagebox.showerror("error","invalid secret key")

# decrypt code secren2 and backend
def decrypt():
    password=code.get()
    if(password=="1010"):
       secren2=Toplevel(secren)
       secren2.title("decryption")
       secren2.geometry("400x400")
       secren2.configure(bg="lightblue")
       message=text.get(1.0,END)
       decode_text=message.encode("ascii")
       base64_bytes=base64.b64decode(decode_text)
       decrypt=base64_bytes.decode("ascii")
       
       label3=Label(secren2,text="The Code is Encrypted",font=("Courier","24","bold"),bg="lightblue")
       label3.place(x=20,y=40)
       img2=ImageTk.PhotoImage(Image.open("image/decrpt.png"))
       Label(secren2,image=img2).place(x=565,y=0,height=850,width=800)
       #text2
       text2=Text(secren2,font="20",bd=3,wrap=WORD)
       text2.place(x=50,y=150,width=400,height=200)
       text2.insert(END,decrypt)
       #button Encrypted
       Button(secren2,text="Select",font=("Courier ","18","bold"),bd=5,bg="blue",fg="black",command=lambda:select()).place(x=60,y=400,width=100)

       Button(secren2,text="cut",font=("Courier ","18","bold"),bd=5,bg="red",fg="black",command=lambda:cut()).place(x=190,y=400,width=100)

       Button(secren2,text="Copy",font=("Courier ", "18","bold"),bd=5,bg="gold",fg="black",command=lambda:copy()).place(x=320,y=400,width=100)
       def  select():
             text2.tag_add("sele", "1.0","end") # all text selected
             text2.tag_config("sele",background="orange",foreground="white")
             
       def cut():
        global data 
        if text2.selection_get():
          data=text2.selection_get() # copy selected text to clipboard 
          text2.delete('sele.first','sele.last') # delete selected text 

       def copy():
        global data 
        if text2.selection_get():
           data=text2.selection_get() 
     # validation encrypted
    elif(password==""):
        messagebox.showerror("error", "please enter the secret key")
    elif(password!="1010"):
        messagebox.showerror("error","invalid secret key")  
# reset button click function
def reset():
    Text.delete(text,1.0,END)
    code.set(" ")
def paste():
     global data
     text.insert(tkinter.END,data)
# lable
hedinglable=Label(secren, text=" Welcome to Text Encryption and \nDecryption", font=('Courier', '24', 'bold'),bg="lightblue")
hedinglable.place(x=20,y=40)
# imageTk
img =ImageTk.PhotoImage(Image.open("image/goha.png"))
Label(secren, image = img).place(x=565,y=0,height=850,width=800)
#text
text=Text(secren,font="20",bd=3)
text.place(x=55,y=150,width=400,height=200)
# lable
secretlable=Label(secren,text="Enter the Secret  key",font=('Courier','18','bold'),bg="lightblue")
secretlable.place(x=100,y=400)
# entry
code=StringVar()
enter=Entry(textvariable=code,bd=3,font="20",show="*")
enter.place(x=160,y=460)
#button
button=Button(secren,text="Encrypt",font=("Courier","18","bold",),bd=5,bg="DarkGreen",fg="black",command=encrypt)
button.place(x=50,y=500,width=180)
button=Button(secren,text="Dncrypt",font=("Courier","18","bold",),bd=5,bg="red",fg="black",command=decrypt)
button.place(x=280,y=500,width=180)
# reset button
button=Button(secren,text="Reset",font=("Courier ","18","bold"),bd=5,bg="Purple",fg="black",command=reset)
button.place(x=50,y=600,width=180)
Button(secren,text="paste",font=("Courier ","18","bold"),bd=5,bg="orange",fg="black",command=lambda:paste()).place(x=280,y=600,width=180)

mainloop()
