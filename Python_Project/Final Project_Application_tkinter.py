# Harish Musthyala - Python Project

#Import Libraries
import tkinter
import tkinter.messagebox
import random

# Create a class
class MyProject:
    def __init__(self):
        # Create the main window with widgets (9 Menu buttons with lablel and frames)
        self.main_window = tkinter.Tk()
        self.main_window.title('Python Project - Harish')
        
        self.heading = tkinter.Label(self.main_window, \
                                    text = 'UNH Scripting w/Python')
        self.button_select = tkinter.Button(self.main_window, \
                                        text='Select/Create File', \
                                        command=self.select_file,bg='white')
        self.button_display = tkinter.Button(self.main_window, \
                                        text='Display', \
                                        command=self.display)
        self.button_sort = tkinter.Button(self.main_window, \
                                        text='Sorting', \
                                        command=self.sorting)
        self.button_search = tkinter.Button(self.main_window, \
                                        text='Search', \
                                        command=self.search)
        self.button_largest = tkinter.Button(self.main_window, \
                                        text='Largest', \
                                        command=self.largest)
        self.button_append = tkinter.Button(self.main_window, \
                                        text='Append', \
                                        command=self.append)
        self.button_encrypt = tkinter.Button(self.main_window, \
                                        text='Encrypt', \
                                        command=self.encrypt)
        self.button_decrypt = tkinter.Button(self.main_window, \
                                        text='Decrypt', \
                                        command=self.decrypt)
        self.button_exit = tkinter.Button(self.main_window, \
                                        text='Exit', \
                                        command=self.main_window.destroy,bg='red')
        self.top_frame = tkinter.Frame(self.main_window)
        self.label_File = tkinter.Label(self.top_frame,text = '"No File Selected"')
    
        
        # Packs the widgets in the main window.
        self.heading.pack()
        self.heading.configure(font = 'BOLD')
        self.top_frame.pack()
        self.button_select.pack()
        self.button_display.pack(side = 'top')
        self.button_sort.pack(side = 'left')
        self.button_search.pack(side = 'left')
        self.button_largest.pack(side = 'left')
        self.button_append.pack(side = 'left')
        self.button_encrypt.pack(side = 'left')
        self.button_decrypt.pack(side = 'left')
        self.button_exit.pack()
        self.label_File.pack()
        
        
        # Enter the tkinter main loop to handle events.
        tkinter.mainloop()

    check = '' # Class variable to check the file is selected or store name of the file
    en = 0 # class variable to check whether encryption is done
    word = [] # class variable to store the encrypt or decrypt data if the number is grater than 1 digit
    button_press = 0 # class variable to check the button click and destroy the select file entry

    # Function to create file with the given name(self.check)
    def create(self):
        file = open(self.check + '.txt',"w")
        file.close()
        p = 'The file " ' + self.check + '.txt " has been created'
        tkinter.messagebox.showinfo('Creat',p)

    # Function creates an entry for selecting the file 
    def select_file(self):
        if self.button_press != 0:
            self.entry1.destroy()
            self.button_Enter.destroy()
            self.label_File.destroy()
        self.button_press = 1
        self.check = ''
        self.label_File.destroy()
        self.label_File = tkinter.Label(self.top_frame,text = '"No File Selected"')
        self.entry1 = tkinter.Entry(self.top_frame)
        self.button_Enter = tkinter.Button(self.top_frame, \
                                        text='Enter', \
                                        command=self.checking)
        self.label_File.pack()
        self.entry1.pack()
        self.button_Enter.pack()

    # Function checks whether the file is present, else create one
    # Also create entry box to input filename and show which file is selected
    def checking(self):
        self.check = self.entry1.get()
        self.entry1.destroy()
        self.button_Enter.destroy()
        self.label_File.destroy()
        v = 'Selected File : '+ self.check
        self.label_File = tkinter.Label(self.top_frame,text = v,bg='green')
        self.label_File.pack()
        try:
            file = open(self.check+'.txt','r')
            load = file.read()
            file.close()
            tkinter.messagebox.showinfo('SelectFile','The File " '+self.check+'.txt " has been selected')
        except FileNotFoundError:
            tkinter.messagebox.showinfo('SelectFile','The selected file " '+self.check+'.txt " is not present')
            self.create()
    # Function displays the data in the file, Total and average
    def display(self):
        if self.check == '':
            tkinter.messagebox.showinfo('Display','Please select the file !')
        else:
            file = open(self.check+'.txt','r')
            load = file.read().split()
            file.close()
            if len(load) == 0:
                tkinter.messagebox.showinfo('Display','File is Empty !')
            else:
                sum = 0
                if len(load) != 0:
                    for i in load:
                        sum = sum + int(i)
                    average = sum/(len(load))
                    d = self.check+'.txt : ' + str(list(load))+'\nTotal : '+str(sum)+' \nAverage : '+str(round(average,2))
                    tkinter.messagebox.showinfo('Display',d)

    # Function displays the sorted data in the file
    def sorting(self):
        if self.check == '':
            tkinter.messagebox.showinfo('Sorting','Please select the file !')
        else:
            file = open(self.check+'.txt','r')
            load = file.read().split()
            file.close()
            if len(load) == 0:
                tkinter.messagebox.showinfo('Sort','File is Empty !')
            else:
                if len(load) != 0:
                    sorteddata = []
                    for i in load:
                        sorteddata.append(int(i))
                    sorteddata.sort()
                    g = "Sorted data : " + str(sorteddata)
                    tkinter.messagebox.showinfo('Sorting',g)

    # Function creates temporary window to enter the number for search 
    def search(self):
        if self.check == '':
            tkinter.messagebox.showinfo('Search','Please select the file !')
        else:
            file = open(self.check+'.txt','r')
            load = file.read()
            file.close()
            if len(load) != 0:
                self.temp_window = tkinter.Tk()
                self.label_num = tkinter.Label(self.temp_window,text = 'Enter the number to search : ')
                self.entry_temp = tkinter.Entry(self.temp_window)
                self.button_Ok = tkinter.Button(self.temp_window, \
                                                text='Ok', \
                                                command=self.searching)
                self.label_num.pack(side='left')
                self.entry_temp.pack(side='left')
                self.button_Ok.pack()
            else:
                tkinter.messagebox.showinfo('Search','File is Empty !')
                 
    # Function searches for the entered number in the file data
    def searching(self):
        # checks for the valid number entry and process operation
        try:
            self.num = int(self.entry_temp.get())
        except:
            tkinter.messagebox.showinfo('InValid Input','Please enter a valid input')
            self.num = None
       
        self.label_num.destroy()
        self.entry_temp.destroy()
        self.button_Ok.destroy()
        self.temp_window.destroy()
        file = open(self.check+'.txt','r')
        load = file.read().split()
        file.close()
        if self.num != None:
            if len(load) != 0:
                s = 0
                for i in load:
                    if int(i) == self.num:
                        s = s+1
                if s!=0:                        
                    g = "Selected number: " + str(self.num) + " appeared "+str(s)+" times in the file"
                    tkinter.messagebox.showinfo('Search',g)
                else:
                    p = 'Selected number: '+str(self.num)+' is not found in the file'
                    tkinter.messagebox.showinfo('Search',p)
            else:
                tkinter.messagebox.showinfo('Search','File is Empty !')
        else:
            tkinter.messagebox.showinfo('Search','Operation cannot be processed')

    # Function displays the largest number in the data file     
    def largest(self):
        if self.check == '':
            tkinter.messagebox.showinfo('Largest','Please select the file !')
        else:
            file = open(self.check+'.txt','r')
            load = file.read().split()
            file.close()
            if len(load) == 0:
                tkinter.messagebox.showinfo('Largest','File is Empty !')
            else:
                if len(load) != 0:
                    sorteddata = []
                    for i in load:
                        sorteddata.append(int(i))
                    sorteddata.sort()
                    g = "Largest number in the file : "+ str(sorteddata[-1])
                    tkinter.messagebox.showinfo('Largest',g)

    # Function creates temporary window to select how many random numbers to be appended    
    def append(self):
        if self.check == '':
            tkinter.messagebox.showinfo('Append','Please select the file !')
        else:
            self.temp_window = tkinter.Tk()
            self.label_num = tkinter.Label(self.temp_window,text = 'How many random numbers you want to append : ')
            self.entry_temp = tkinter.Entry(self.temp_window)
            self.button_Ok = tkinter.Button(self.temp_window, \
                                            text='Ok', \
                                            command=self.appending)
            self.label_num.pack(side='left')
            self.entry_temp.pack(side='left')
            self.button_Ok.pack()
        
    # Function append selcted number of random data to the end of the file
    def appending(self):
        # checks for a valid entry and process the operation
        try:
            self.append_num = int(self.entry_temp.get())
        except:
            tkinter.messagebox.showinfo('InValid Input','Please enter a valid input')
            self.append_num = 0

        # Destroys the temp window once the input is stored
        self.entry_temp.destroy()
        self.button_Ok.destroy()
        self.label_num.destroy()
        self.temp_window.destroy()
        
        file = open(self.check+'.txt','r')
        load = file.read()
        file.close()
        appendlist = open("temp.txt","w")
        for i in range(self.append_num):
            c = random.randint(1,100)
            d = str(c)
            appendlist.write(d)
            appendlist.write(' ')
        appendlist.close()
        appendlist = open("temp.txt","r")
        templist = appendlist.read()
        appendlist.close()
        load = load + templist
        file = open(self.check+'.txt','w')
        for i in load:
            file.write(i)
        file.close()
        if self.append_num == 0:
            tkinter.messagebox.showinfo('Append','Operation cannot be processed')
        else:
            tkinter.messagebox.showinfo('Append','File has been updated with '+str(self.append_num)+ ' random numbers')

    # Function encrypts the number which is greater than single digit
    def word_char(self):
        temp_list = []
        string = ""
        # Codes to encrypt the digits
        codes = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':'~'}
        for d in self.word:
            if d in codes:
                d = codes[d]
            else:
                d = d
            temp_list.append(d)
        self.word = string.join(temp_list)

    # Function encrypts the data in the selected file
    def encrypt(self):
        if self.check == '':
            tkinter.messagebox.showinfo('Encrypt','Please select the file !')
        else:
            file = open(self.check+'.txt','r')
            load = file.read().split()
            file.close()
            if len(load) == 0:
                tkinter.messagebox.showinfo('Encrypt','File is Empty !')
            else:
                self.en = 0
                codes = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':'~'}
                file = open(self.check+'.txt','r')
                load = file.read().split()
                file.close()
                encrypt_file = open('encrypted_text.txt','w')
                for char in load:
                    if len(char)>1:
                        self.word = char
                        self.word_char()
                        encrypt_file.write(self.word)
                        encrypt_file.write('\n')
                    else:
                        if char in codes:
                            encrypt_file.write(codes[char])
                            encrypt_file.write('\n')
                        else:
                            encrypt_file.write(char)
                            encrypt_file.write('\n')
                encrypt_file.close()
                self.en = 1
                tkinter.messagebox.showinfo('Encrypt','Data has been Encrypted !')
                file = open('encrypted_text.txt','r')
                load = file.read().split()
                load = list(load)
                file.close()   
                g = 'Encrypted data : '+str(load)
                tkinter.messagebox.showinfo('Encrypt',g)

    # Function decrypts the number which is greater than single digit
    def word_char_decrypt(self):
        temp_list = []
        string = ""
        decrypt_codes = {'!':'1','@':'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8','(':'9','~':'0'}
        for d in self.word:
            if d in decrypt_codes:
                d = decrypt_codes[d]
            else:
                d = d
            temp_list.append(d)
        self.word = string.join(temp_list)

    # Function decypts the data in the selected file
    def decrypt(self):
        if self.check == '':
            tkinter.messagebox.showinfo('Decrypt','Please select the file !')
        else:
            if self.en == 0:
                tkinter.messagebox.showinfo('Decrypt','Encrypt the file before decrypting !')
            else:
                # decrypt codes
                decrypt_codes = {'!':'1','@':'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8','(':'9','~':'0'}
                en_file = open('encrypted_text.txt','r')
                en_load = en_file.read().split()
                en_file.close()
                decrypt_file = open('decrypted_text.txt','w')
                for char in en_load:
                    if len(char)>1:
                        self.word = char
                        self.word_char_decrypt()
                        decrypt_file.write(self.word)
                        decrypt_file.write('\n')
                    else:
                        if char in decrypt_codes:
                            decrypt_file.write(decrypt_codes[char])
                            decrypt_file.write('\n')
                        else:
                            decrypt_file.write(char)
                            decrypt_file.write('\n')
                decrypt_file.close() 
                        
                d = open('decrypted_text.txt','r')
                read_decrypt = d.read().split()
                read_decrypt = list(read_decrypt)
                d.close()
                tkinter.messagebox.showinfo('Decrypt','Data has been Decrypted !')
                g = 'Decrypted data : '+str(read_decrypt)
                tkinter.messagebox.showinfo('Decrypt',g)

# Creating instance
Mypro = MyProject()

