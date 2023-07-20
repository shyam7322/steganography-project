from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from stegano import lsb
import wave
#The wave module provides a convenient interface to the WAV sound format. 
import re
#A regular expression (or RE) specifies a set of strings that matches it; the functions in this module
import subprocess
#Subprocess in Python is a module used to run new codes and applications by creating new processes
import os
#This module provides a portable way of using operating system dependent functionality.
import subprocess
from subprocess import *


imagelocation=""
savelocation=""
result=""
imagelocation1=""
savelocation1=""
resulta=""
imagelocationv=""
savelocationv=""
resultv=""
root = Tk()
root.geometry('880x370')
root.title('SEEKMI')
root.iconbitmap("download.ico")

    
def getfile(m,x):
    filename = askopenfilename()
    imagelocation=filename
    m.config(text=imagelocation,fg="green yellow")
    x.config(text="",fg="red")

def getsave(n,y):
    filename1=askdirectory()
    savelocation=filename1
    n.config(text=savelocation,fg="green yellow")
    y.config(text="",fg="red")

def getfile1(a,x):
    filename = askopenfilename()
    imagelocation1=filename
    a.config(text=imagelocation1,fg="green yellow")
    x.config(text="",fg="red")

def getsave1(b,y):
    filename1=askdirectory()
    savelocation1=filename1
    b.config(text=savelocation1,fg="green yellow")
    y.config(text="",fg="red")

def getfilev(a,x):
    filenamev = askopenfilename()
    imagelocationv=filenamev
    a.config(text=imagelocationv,fg="green yellow")
    x.config(text="",fg="red")

def getsavev(b,y):
    filenamev=askdirectory()
    savelocationv=filenamev
    b.config(text=savelocationv,fg="green yellow")
    y.config(text="")
    
def new_encrypt(): 
    newwin = Toplevel(root)
    newwin.configure(bg = 'black')
    newwin.geometry('800x500')
    newwin.title('SEEKMI')
    newwin.iconbitmap("download.ico")
    root.withdraw()
    display = Label(newwin, text="Encrypt @..@ !",bg="black",fg="yellow")
    display.pack()
    tab_parent = ttk.Notebook(newwin)
    style = ttk.Style()
    style.configure('new.TFrame', background='black')
    tab1 = ttk.Frame(tab_parent, style='new.TFrame')
    tab2 = ttk.Frame(tab_parent, style='new.TFrame')
    tab3 = ttk.Frame(tab_parent, style='new.TFrame')
    tab_parent.add(tab1, text="Image...")
    tab_parent.add(tab2, text="Audio...")
    tab_parent.add(tab3, text="Video...")

    style1 = ttk.Style()
    style1.configure("BW.TLabel", foreground="red",background="black")
    
    ttk.Label(tab1, text="Image Encrypt ...",style="BW.TLabel").grid(column=0,row=0,padx=10,pady=10)
    blank=Label(tab1,text="Choose the image.",fg="white",bg="black").grid(column=0,row=1,padx=10,pady=10)
    selectfile= Button(tab1,text="Choose Image",command= lambda: getfile1(blank1,errlabel),bg="black",fg="khaki1")
    selectfile.grid(column=1,row=1,padx=10,pady=10)
    blank1=Label(tab1,bg="black")
    blank1.grid(column=2,row=1,padx=10,pady=10)
    blank=Label(tab1,text="Choose the location",fg="white",bg="black").grid(column=0,row=2,padx=10,pady=10)
    selectfile= Button(tab1,text="Select folder",command= lambda: getsave1(blank2,errlabel),bg="black",fg="khaki1")
    selectfile.grid(column=1,row=2,padx=10,pady=10)
    blank2=Label(tab1,bg="black")
    blank2.grid(column=2,row=2,padx=10,pady=10)
    lable1=Label(tab1,text="Enter the message",fg="white",bg="black")
    lable1.grid(column=0,row=4,padx=10,pady=10)
    ta1=Text(tab1,height=5, width=30,bg="black",fg="white")
    ta1.grid(column=1,row=4,padx=10,pady=10)
    lable2=Label(tab1,text="Enter key ",fg="white",bg="black")
    lable2.grid(column=0,row=5,padx=10,pady=10)
    ta2 = Entry(tab1, width=30,bg="black",fg="white")
    ta2.grid(column=1,row=5,padx=10,pady=10)
    errlabel=Label(tab1,text="",fg="red",bg="black")
    errlabel.grid(column=1,row=6,padx=10,pady=10)
    b= Button(tab1,text="Press",command= lambda: encrypt(ta1,ta2,blank1,blank2,errlabel),fg="blue",bg="black")
    b.grid(column=1,row=7,padx=10,pady=10)
    
    ttk.Label(tab2, text="Audio Encrypt....",style="BW.TLabel").grid(column=0,row=0,padx=10,pady=10)
    blanka=Label(tab2,text="Choose the Audio",fg="white",bg="black").grid(column=0,row=1,padx=10,pady=10)
    selectfilea= Button(tab2,text="Choose Audio",command= lambda: getfile(blank1a,errlabela),bg="black",fg="khaki1")
    selectfilea.grid(column=1,row=1,padx=10,pady=10)
    blank1a=Label(tab2,bg="black")
    blank1a.grid(column=2,row=1,padx=10,pady=10)
    blankaud=Label(tab2,text="Choose the location",fg="white",bg="black").grid(column=0,row=2,padx=10,pady=10)
    selectfileau= Button(tab2,text="Select folder",command= lambda: getsave(blank2a,errlabela),bg="black",fg="khaki1")
    selectfileau.grid(column=1,row=2,padx=10,pady=10)
    blank2a=Label(tab2,bg="black")
    blank2a.grid(column=2,row=2,padx=10,pady=10)
    lable1a=Label(tab2,text="Enter the message ",fg="white",bg="black")
    lable1a.grid(column=0,row=4,padx=10,pady=10)
    ta1a=Text(tab2,height=5, width=30,bg="black",fg="white")
    ta1a.grid(column=1,row=4,padx=10,pady=10)
    lable2a=Label(tab2,text="Enter key ",fg="white",bg="black")
    lable2a.grid(column=0,row=5,padx=10,pady=10)
    ta2a = Entry(tab2, width=30,bg="black",fg="white")
    ta2a.grid(column=1,row=5,padx=10,pady=10)
    errlabela=Label(tab2,text="",fg="red",bg="black")
    errlabela.grid(column=1,row=6,padx=10,pady=10)
    ba= Button(tab2,text="Press",command= lambda: audenc(ta1a,ta2a,blank1a,blank2a,errlabela),bg="black",fg="blue")
    ba.grid(column=1,row=7,padx=10,pady=10)
    
    ttk.Label(tab3, text="Video Encrypt...",style="BW.TLabel").grid(column=0,row=0,padx=10,pady=10)
    blankv=Label(tab3,text="Choose the video ",fg="white",bg="black").grid(column=0,row=1,padx=10,pady=10)
    selectfilev= Button(tab3,text="Choose video",command= lambda: getfilev(blank1v,errlabelv),bg="black",fg="khaki1")
    selectfilev.grid(column=1,row=1,padx=10,pady=10)
    blank1v=Label(tab3,bg="black")
    blank1v.grid(column=2,row=1,padx=10,pady=10)
    lable1v=Label(tab3,text="Enter the message",fg="white",bg="black")
    lable1v.grid(column=0,row=4,padx=10,pady=10)
    ta1v=Text(tab3,height=5, width=30,bg="black",fg="white")
    ta1v.grid(column=1,row=4,padx=10,pady=10)
    lable2v=Label(tab3,text="Enter key ",fg="white",bg="black")
    lable2v.grid(column=0,row=5,padx=10,pady=10)
    ta2v = Entry(tab3, width=30,bg="black",fg="white")
    ta2v.grid(column=1,row=5,padx=10,pady=10)
    errlabelv=Label(tab3,text="",fg="red",bg="black")
    errlabelv.grid(column=1,row=6,padx=10,pady=10)
    bv= Button(tab3,text="Press",command= lambda: videnc(ta1v,ta2v,blank1v,errlabelv),bg="black",fg="blue")
    bv.grid(column=1,row=7,padx=10,pady=10)
    tab_parent.pack(expand=1, fill='both')
    

    
def new_decrypt():
    newwin = Toplevel(root)
    newwin.geometry('850x450')
    newwin.configure(bg = 'black')
    newwin.title('SEEKMI')
    newwin.iconbitmap("download.ico")
    root.withdraw()
    display = Label(newwin, text="Decrypt @..@ !",bg="black",fg="yellow")
    display.pack()
    style = ttk.Style()
    style.configure('new.TFrame', background='black')
    tab_parent = ttk.Notebook(newwin)
    tab1 = ttk.Frame(tab_parent, style='new.TFrame')
    tab2 = ttk.Frame(tab_parent, style='new.TFrame')
    tab3 = ttk.Frame(tab_parent, style='new.TFrame')
    tab_parent.add(tab1, text="Image")
    tab_parent.add(tab2, text="Audio")
    tab_parent.add(tab3, text="Video")

    style1 = ttk.Style()
    style1.configure("BW.TLabel", foreground="red",background="black")
    
    ttk.Label(tab1, text="Image Decrypt...",style="BW.TLabel").grid(column=0,row=0,padx=10,pady=10)
    blank=Label(tab1,text="Choose the image ",fg="white",bg="black").grid(column=0,row=1,padx=10,pady=10)
    selectfile= Button(tab1,text="choose image",command= lambda: getfile(blank1,errlabel),bg="black",fg="khaki1")
    selectfile.grid(column=1,row=1,padx=10,pady=10)
    blank1=Label(tab1,bg="black")
    blank1.grid(column=2,row=1,padx=10,pady=10)   
    lable2=Label(tab1,text="enter key",fg="white",bg="black")
    lable2.grid(column=0,row=4,padx=10,pady=10)
    ta2 = Entry(tab1, width=30,fg="white",bg="black")
    ta2.grid(column=1,row=4,padx=10,pady=10)
    lable1=Label(tab1,text="Message is",fg="white",bg="black")
    lable1.grid(column=0,row=5,padx=10,pady=10)
    ta1=Text(tab1,height=5, width=30, state="disabled",bg="black",fg="white")
    ta1.grid(column=1,row=5,padx=10,pady=10)
    errlabel=Label(tab1,text="",fg="red",bg='black')
    errlabel.grid(column=1,row=6,padx=10,pady=10)
    b= Button(tab1,text="Press",command= lambda: decrypt(ta1,ta2,blank1,errlabel),bg="black",fg="blue")
    b.grid(column=1,row=7,padx=10,pady=10)


    ttk.Label(tab2, text="Audio Decrypt...",style="BW.TLabel").grid(column=0,row=0,padx=10,pady=10)
    blanka=Label(tab2,text="Choose the audio ",fg="white",bg="black").grid(column=0,row=1,padx=10,pady=10)
    selectfilea= Button(tab2,text="choose audio",command= lambda: getfile1(blank1a,errlabela),bg="black",fg="khaki1")
    selectfilea.grid(column=1,row=1,padx=10,pady=10)
    blank1a=Label(tab2,bg="black")
    blank1a.grid(column=2,row=1,padx=10,pady=10)   
    lable2a=Label(tab2,text="enter key ",fg="white",bg="black")
    lable2a.grid(column=0,row=4,padx=10,pady=10)
    ta2a = Entry(tab2, width=30,bg="black",fg="white")
    ta2a.grid(column=1,row=4,padx=10,pady=10)
    lable1a=Label(tab2,text="Message is",fg="white",bg="black")
    lable1a.grid(column=0,row=5,padx=10,pady=10)
    ta1a=Text(tab2,height=5, width=30, state="disabled",fg="white",bg="black")
    ta1a.grid(column=1,row=5,padx=10,pady=10)
    errlabela=Label(tab2,text="",bg="black",fg="red")
    errlabela.grid(column=1,row=6,padx=10,pady=10)
    ba= Button(tab2,text="Press",command= lambda: auddec(ta1a,ta2a,blank1a,errlabela),bg="black",fg="blue")
    ba.grid(column=1,row=7,padx=10,pady=10)
    
    ttk.Label(tab3, text="Video Decrypt...",style="BW.TLabel").grid(column=0,row=0,padx=10,pady=10)
    blankv=Label(tab3,text="Choose the video",fg="white",bg="black").grid(column=0,row=1,padx=10,pady=10)
    selectfilev= Button(tab3,text="choose video",command= lambda: getfilev(blank1v,errlabelv),bg="black",fg="khaki1")
    selectfilev.grid(column=1,row=1,padx=10,pady=10)
    blank1v=Label(tab3,bg="black")
    blank1v.grid(column=2,row=1,padx=10,pady=10)   
    lable2v=Label(tab3,text="enter key ",fg="white",bg="black")
    lable2v.grid(column=0,row=4,padx=10,pady=10)
    ta2v = Entry(tab3, width=30,bg="black",fg="white")
    ta2v.grid(column=1,row=4,padx=10,pady=10)
    lable1v=Label(tab3,text="Message is",fg="white",bg="black")
    lable1v.grid(column=0,row=5,padx=10,pady=10)
    ta1v=Text(tab3,height=5, width=30, state="disabled",bg="black",fg="white")
    ta1v.grid(column=1,row=5,padx=10,pady=10)
    errlabelv=Label(tab3,text="",bg="black",fg="red")
    errlabelv.grid(column=1,row=6,padx=10,pady=10)
    bv= Button(tab3,text="Press",command= lambda: viddec(ta1v,ta2v,blank1v,errlabelv),bg="black",fg="blue")
    bv.grid(column=1,row=7,padx=10,pady=10)
    tab_parent.pack(expand=1, fill='both')


Label1=Label(root, text= "SEEKMI", font=100,bg="black",fg="white")
Label1.grid(column=1,row=0,padx=10,pady=10)


button1=Button(root, text ="ENCODE", command =new_encrypt,fg="white") 
button1.config(width=90,height=5,background="black")
button1.config(font=120)
button1.grid(column=1,row=2,padx=10,pady=10)
button2=Button(root, text ="DECODE", command =new_decrypt,fg="white") 
button2.config(width=90,height=5,background="black")
button2.config(font=120)
button2.grid(column=1,row=4)

def encrypt(text1,s1,l,sv,errlabel):
    errlabel.config(text="")
    result = ""
    lbl=l.cget("text")
    svl=sv.cget("text")  
    text=text1.get("1.0",END)
    s2=s1.get()

    
    if(lbl!="" and svl!="" and text!="" and s2!=""):
        s=int(s2)
        for i in range(len(text)):
            char = text[i] 

            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)

            elif (char==(" ")):
                result += "~"

            elif (char.isnumeric()):
                num=int(char)
                result += str(num)
            elif(re.match("[@_!#$%^&*()<>?/\|}{~`:]",char)):
                result+=char
                 
  

            else: 
                result += chr((ord(char) + s - 97) % 26 + 97)
        secret = lsb.hide(lbl,result)
        secret.save(svl+"/sample-secret1.png")
        errlabel.config(text="done @@")
        l.config(text="")
        sv.config(text="")
        s1.delete(0,END)
    
        text1.delete(1.0,END)

    else:
        errlabel.config(text="check ")

def decrypt(res,key,loc,errlabel):
    errlabel.config(text="")
    res.config(state="normal")
    res.delete(1.0,END)
    res.config(state="disabled")
    result = "" 
    location=loc.cget("text")
    s2=key.get()
    if(location!="" and s2!=""):
        s=int(key.get())
        clear_message = lsb.reveal(location)
        text=clear_message

        for i in range(len(text)):
            char = text[i] 
  
            if (char.isupper()):
                result += chr((ord(char) - s -65) % 26 + 65)

            elif (char==("~")):
                result += " "

            elif (char.isnumeric()):
                num=int(char)
                result += str(num)
            elif(re.match("[@_!#$%^&*()<>?/\|}{~`:]",char)):
                result+=char
        
            else: 
                result += chr((ord(char) - s - 97) % 26 + 97)

        result=result[:-1]
        res.config(state="normal")
        res.insert(END,result)
        res.config(state="disabled")
        errlabel.config(text="done @@")
        loc.config(text="")
        key.delete(0,END)
    else:
        errlabel.config(text="check")


def audenc(text1a,s1a,la,sva,errlabela):
    errlabela.config(text="")
    resulta=""
    lbla=la.cget("text")
    svla=sva.cget("text")  
    text=text1a.get("1.0",END)
    s2=s1a.get()
    if(text!="" and s2!="" and lbla!="" and svla!=""):
        s=int(s1a.get())
        for i in range(len(text)):
            char = text[i] 
  

            if (char.isupper()):
                resulta += chr((ord(char) + s-65) % 26 + 65)

            elif (char==(" ")):
                resulta += "~"

            elif (char.isnumeric()):
                num=int(char)
                resulta += str(num)
            elif(re.match("[@_!#$%^&*()<>?/\|}{~`:]",char)):
                resulta+=char
  
            else: 
                resulta += chr((ord(char) + s - 97) % 26 + 97)
            
        song = wave.open(lbla, mode='rb')
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))
        string=resulta
        string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'    
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit

        frame_modified = bytes(frame_bytes)
        with wave.open(svla+'/song_embedded.wav', 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)
        song.close()
        errlabela.config(text="done @@")
        la.config(text="")
        sva.config(text="")
        text1a.delete(1.0,END)
        s1a.delete(0,END)
    else:
        errlabela.config(text="check")
        

def auddec(resa,keya,loca,errlabela):
    errlabela.config(text="")
    resa.config(state="normal")
    resa.delete(1.0,END)
    resa.config(state="disabled")
    resulta = "" 
    location=loca.cget("text")
    s2=keya.get()
    if(location!="" and s2!=""):
        s=int(keya.get())
        song = wave.open(location, mode='rb')
        frame_bytes = bytearray(list(song.readframes(song.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        decoded = string.split("###")[0]
        text=decoded
        song.close()
        for i in range(len(text)):
            char = text[i] 

            if (char.isupper()):
                resulta += chr((ord(char) - s -65) % 26 + 65)

            elif (char==("~")):
                resulta += " "

            elif (char.isnumeric()):
                num=int(char)
                resulta += str(num)
            elif(re.match("[@_!#$%^&*()<>?/\|}{~`:]",char)):
                resulta+=char
  
            else: 
                resulta += chr((ord(char) - s - 97) % 26 + 97)

        resulta=resulta[:-1]
        resa.config(state="normal")
        resa.insert(END,resulta)
        resa.config(state="disabled")
        errlabela.config(text="done @@")
        loca.config(text="")
        keya.delete(0,END)
    else:
        errlabela.config(text="check")
        

def videnc(text1v,s1v,lv,errlabelv):
    errlabelv.config(text="")
    resultv=""
    lblv=lv.cget("text")
    text=text1v.get("1.0",END)
    s2=s1v.get()
    
    if(lblv!="" and text!="" and s2!=""):
        s=int(s1v.get())
        input_file=lblv
        for i in range(len(text)):
            char = text[i]

            if (char.isupper()):
                resultv += chr((ord(char) + s-65) % 26 + 65)

            elif (char==(" ")):
                resultv += "~"

            elif (char.isnumeric()):
                num=int(char)
                resultv += str(num)
            elif(re.match("[@_!#$%^&*()<>?/\|}{~`:]",char)):
                resultv+=char
  
            else: 
                resultv += chr((ord(char) + s - 97) % 26 + 97)

        v1=resultv
        exe1="exiftool.exe"
        call([exe1,"-Copyright=" + v1 , "test.mp4"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        errlabelv.config(text="done @@")
        text1v.delete(1.0,END)
        s1v.delete(0,END)
        lv.config(text="")
    else:
        errlabelv.config(text="check")
        

def viddec(resv,keyv,locv,errlabelv):
    errlabelv.config(text="")
    resv.config(state="normal")
    resv.delete(1.0,END)
    resv.config(state="disabled")
    resultv = "" 
    location=locv.cget("text")
    s2=keyv.get()
    if(location!="" and s2!=""):
        s=int(keyv.get())
        variable =''
        input_file=location
        exe="exiftool.exe"
        process = subprocess.Popen([exe,input_file],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
        metadata=[]
        for output in process.stdout:
            info={}
            line=output.strip().split(":")
            info[line[0].strip()] = line[1].strip()
            metadata.append(info)

        
        for e in metadata:
            if(not(e.get('Copyright'))):
                pass
        
            else:
                variable=e.get('Copyright')
         
        text=variable

        for i in range(len(text)):
            char = text[i] 

            if (char.isupper()):
                resultv += chr((ord(char) - s -65) % 26 + 65)

            elif (char==("~")):
                resultv += " "

            elif (char.isnumeric()):
                num=int(char)
                resultv += str(num)
            elif(re.match("[@_!#$%^&*()<>?/\|}{~`:]",char)):
                resultv+=char
  
            else:
                resultv += chr((ord(char) - s - 97) % 26 + 97)

        resultv=resultv[:-1]

        resv.config(state="normal")
        resv.insert(END,resultv)
        resv.config(state="disabled")
        errlabelv.config(text="done @@")
        locv.config(text="")
        keyv.delete(0,END)
    else:
        errlabelv.config(text="check")
        

root.configure(background = 'black')
root.mainloop()
