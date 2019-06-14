
#---------------Upload image by file dialog(edit by codersarts)---------------

def select_image():
    
    path_to_image = tk.filedialog.askopenfilename(
        parent=mainwindow, initialdir='F:\Blog images',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('gif images', '.gif')]
        )
    img = Image.open(path_to_image)
    print(img)
    mainwindow.tkimage = ImageTk.PhotoImage(img)
    Label(mainwindow,image = mainwindow.tkimage).place(x=500, y=100, width=200, height=200)
    
# Button : Open
imageEntry = tk.Button(mainwindow, text = "choose file", command = select_image)
imageEntry.grid(row=6, column=1, padx=(0,10), pady = 20)



#-------------------------------------------
