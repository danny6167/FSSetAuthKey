#!/usr/bin/env python
"""
This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.
Daniel Barton <daniel@barteck.com.au>
http://eternalhavoc.net/site/apps/FSSetAuthKey
"""
import os
from os.path import expanduser
from Tkinter import *
import tkMessageBox
import webbrowser

class App:
    def __init__(self, master):
        self.master = master
        
        if os.name not in ['posix']: #TODO: Add windows ID
            tkMessageBox.showerror("Not supported", "OS Not supported")
        
        frame1 = Frame(self.master)
        frame1.pack()
        Label (frame1,text='Enter Auth Key').pack(side=TOP)
        self.entry_key = Entry(frame1, width=35)
        self.entry_key.pack(side=TOP,padx=50,pady=10)
        
        frame2 = Frame(self.master)
        frame2.pack()
        Button(frame2, text="Save", fg="green", command=self.setAuthKey).pack(side=LEFT)
        Button(frame2, text="About", command=self.openAbout).pack(side=RIGHT)
        Button(frame2, text="Quit", fg="red", command=self.master.quit).pack(side=RIGHT)
        
        
        # Load current key
        self.setKeyBox(self.getAuthKey())
        
    def openAbout(self):
        webbrowser.open("http://eternalhavoc.net/site/apps/FSSetAuthKey")
        
    def setAuthKey(self):
        key = self.entry_key.get()
        if not self.keyLooksValid(key):
            if not tkMessageBox.askyesno("Invalid Key", "That key looks invalid to me. Are you sure?"):
                return False
        
        fh = open(self.getKeyPath(), 'w+')
        fh.write(key)
        fh.close()
        tkMessageBox.askyesno('Saved', "AuthKey Saved!")
        
        
    def getAuthKey(self):
        if not os.path.isfile(self.getKeyPath()):
            return ''
        contents = ''
        try:
            fh = open(self.getKeyPath())
            for line in fh.readlines():
                if line[0] == "/": # Skip comments
                    continue
    
                if line.strip().__len__() == 0:# Skip blank lines
                    continue
                
                contents = line.strip()                
                            
        except:
            print "Couldnt open auth key file"
            
        return contents
    
    def keyLooksValid(self, key):
        # 32 chars long
        if key.__len__() != 32:
            print "Length is " + str(key.__len__())
            return False
        
        
        return True
            
    def setKeyBox(self,text):
        self.entry_key.delete('0', END)
        self.entry_key.insert(INSERT, text)
        return
            
        
        
        
    def getKeyPath(self):
        osname = os.name
        if osname == 'posix':
            print "Detected posix OS"
            return expanduser("~/.q3a/q3ut4/authkey")
        return False
            
            
        
        
# Create GUI root
root = Tk()
root.title("UrbanTerror 4.2 Auth Login")


# Center window
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
# calculate position x, y
w=500
h=100
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
# Spawn app and window
app = App(root)
root.mainloop();
        