# -*- coding: utf-8 -*-
# Python Version 3.4 
import matplotlib
matplotlib.use('TkAgg') #matplotlib backend, allows for plots to be injected into different applications, such as frames in this case, or webpages, and etc.

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg #imports a canvas that we will graph on, also this specific canvas can be used with the TkAgg backend
from matplotlib.figure import Figure

import tkinter as tk #imports the tkinter module, which is a Python wrapper of TCL, which is used to make GUIs
from tkinter import ttk

#Special Event tracker; graph with GUI

LARGE_FONT = ('Verdana', 12)
NORMAL_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)


def popupmsg(msg):
    popup = tk.Tk() #Calls Tk and assigns the object to popup
    
    popup.wm_title('!') #Creates title for popup window
    label = tk.Label(popup, text = msg, font = NORMAL_FONT) #Creates text in body of popup window
    label.pack(side = 'top', fill = 'x', pady = 10) #Packs label in window
    Button1 = tk.Button(popup, text = 'Okay', command = popup.destroy)
    Button1.pack()
    popup.mainloop()
    

class RemindMe(tk.Tk): #Inheriting the TK class within tkinter (tk)
    def __init__(self, *args, **kwargs): 
        '''
        initializes anything we want to happen automatically when ever we call upon this class
        Takes arguments(*args), which can be any number of variables, and key word arguments (**kwargs), which are often 
        dictionaries, as inputs
        '''
        tk.Tk.__init__(self, *args, **kwargs)
        '''
        initializes tkinter so it starts right when we call this class
        '''
        container = tk.Frame(self) #frame creates the window, or frame of the GUI, that is then assigned to the variable container
        
        container.pack(side = 'top', fill = 'both', expand = True) 
        
        container.grid_rowconfigure(0, weight = 1) 
        
        container.grid_columnconfigure(0, weight = 1)
        
        
        menubar = tk.Menu(container) #Creates a menu bar as the foundation for making drop down menus
        filemenu = tk.Menu(menubar, tearoff = 0) #Creates a menu within the menubar; tearoff allos the user to pop the menu off into a window if value is a 1
        filemenu.add_command(label = 'Save Settings', command = lambda: popupmsg('Not supported just yet!')) #Creates a button
        filemenu.add_separator() #Adds a visual line sperator between commands
        filemenu.add_command(label = 'Exit', command = quit) #Creates a button that allows the user to quit the program
        menubar.add_cascade(label ='File', menu = filemenu) #Creates a cascading menu box that connects all of the commands above
        
        tk.Tk.config(self, menu=menubar)
        
        self.frames = {} #Creates an empty dictionary, for storing each frame
        
        for F in (StartPage, RemoveEvent, Graph): #for loop cycles through a tuple of all frames
        
            frame = F(container, self) #Calls the class, and assigns the object to frame
            
            self.frames[F] = frame #Stores the object in the dictionary self.frames mapped to the corresponding key that has been cycled through by the for loop
            
            frame.grid(row = 0, column = 0, sticky = 'nsew') #Column and row determine the location of the frame in the container
        
        self.show_frame(StartPage) #Calls the self.show_frames method, and passes in the key StartPage.
        
    def show_frame(self, cont): #cont is short for controller
        
        frame = self.frames[cont] #references the dictionary in the init method, and uses the passed in key from the method call as the controller, and returns the value associated with that key, or controller. That value is then being assigned to the variable frame 
        frame.tkraise() # This takes the value stored in the variable frame, and invokes tkraise() on it to raise that window to the front of the stack; We can do this because we inhereted tk.TK
        
########################################^^^Baseline^^^ -This is the foundation for adding more frames##############################
       
class StartPage(tk.Frame): #inheriting tk.Frame, so it doesn't have to be typed out everytime we call a method within it
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) #The parent class in this case is RemindMe
        label = tk.Label(self, text = 'Welcome to the RemindMe App', font = LARGE_FONT)
        label.grid(row = 0, column = 15)  #Use pack when there are 2-3 items, otherwise use grid. Pad adds padding around label
        
        choices = ('Birthday', 'Anniversary', 'Meeting', 'Seminar','Doctor\'s Apt.', 'Dentist\'s Appt.')        
        
        tk.Label(self, text="Event:").grid(row=0, column = 0)
        event = ttk.Combobox(self, values = choices, state = 'readonly').grid(row=0, column = 1)
        
        
        tk.Label(self, text="First Name:").grid(row=1, column = 0)
        tk.Label(self, text="Last Name:").grid(row=1, column = 2)
        firstName = tk.Entry(self).grid(row=1, column=1)
        lastName = tk.Entry(self).grid(row=1, column=3)
        
        months = ('Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.')
        tk.Label(self, text="Month:").grid(row=3, column = 0)
        month = ttk.Combobox(self, values = months, state = 'readonly').grid(row=3, column = 1)
        
        
        days = []        
        for i in range(1, 32):
            days.append(str(i))
        
        
        tk.Label(self, text="Day:").grid(row=3, column = 2)
        day = ttk.Combobox(self, values = days, state = 'readonly').grid(row=3, column = 3)
        
        years = (2015, 2016, 2017)        
        
        tk.Label(self, text="Year:").grid(row=3, column = 4)
        year = ttk.Combobox(self, values = years, state = 'readonly').grid(row=3, column = 5)
        
        graph = tk.Button(self, text = 'Event Timeline', 
                            command=lambda: controller.show_frame(Graph)) #Takes user to the Graph Frame
        
        graph.grid(row=4, column=15) #packs button and pads, again can use grid when necesarry.
       
        removeEventButton = tk.Button(self, text = 'Remove Event', 
                            command=lambda: controller.show_frame(RemoveEvent)) #Takes user to the RemoveEvent Frame
        
        removeEventButton.grid(row=5, column=15) #packs button and pads, again can use grid when necesarry.  
        
        
       
class RemoveEvent(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Please Select an Event to Remove', font = LARGE_FONT)
        label.pack(pady=30, padx = 30)
        
        mainMenu = tk.Button(self, text = 'Main Menu', 
                            command=lambda: controller.show_frame(StartPage)) #Takes user to the Main Menu(StartPage) Frame
        
        mainMenu.pack(pady=0, padx=0) #packs button and pads, again can use grid when necesarry.
        
        graph = tk.Button(self, text = 'Graph', 
                            command=lambda: controller.show_frame(Graph)) #Takes user to the Graph Frame
        
        graph.pack(pady=30, padx=0) #packs button and pads, again can use grid when necesarry.
        
class Graph(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Upcoming Events', font = LARGE_FONT)
        label.pack(pady=30, padx = 30)
        
        mainMenu = tk.Button(self, text = 'Main Menu', 
                            command=lambda: controller.show_frame(StartPage)) ##Takes user to the Main Menu(StartPage) Frame
        
        mainMenu.pack(pady=0, padx=0) #packs button and pads, again can use grid when necesarry.
        
        removeEventButton = tk.Button(self, text = 'Remove Event', 
                            command=lambda: controller.show_frame(RemoveEvent)) #Takes user to the RemoveEvent Frame
        
        removeEventButton.pack(pady=30, padx=0) #packs button and pads, again can use grid when necesarry.
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111) #the 111 denotes a 1x1 subplot with the last 1 being the subplot number
        a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])
        
        canvas = FigureCanvasTkAgg(f, self) #passing in the variable f which has been assigned the figure dimensions
        canvas.show() #Shows the canvas, or plots it
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True) #Gets a widget for th graph and packs it, could use grid to change location
        
        toolbar = NavigationToolbar2TkAgg(canvas, self) # Adds the toolbar for the graph to the canvas
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True) #Packs 
        
        
        
app = RemindMe() # Calls RemindMe and then sets app equal to the returned object
app.geometry('1280x720') #Changes the dimensions of the GUI container
app.mainloop() #can just call mainloop() method because app inherited from tk.Tk