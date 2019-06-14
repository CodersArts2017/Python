

#-----------------------------------------------place holder(add by codersarts)----------------------------------------

class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'

def add_placeholder_to(a, placeholder, color="white", font=10):
    normal_color = a.cget("fg")
    normal_font = a.cget("font")
    
    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=10
    state.placeholder_color=color
    state.placeholder_font=10
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, a=a, state=state):
        if state.with_placeholder:
            a.delete(0, "end")
            a.config(fg = state.normal_color, font=state.normal_font)
        
            a.with_placeholder = False

    def on_focusout(event, a=a, state=state):
        if a.get() == '':
            a.insert(0, state.placeholder_text)
            a.config(fg = state.placeholder_color, font=state.placeholder_font)
            
            state.with_placeholder = True

    a.insert(0, placeholder)
    a.config(fg = color, font=font)

    a.bind('<FocusIn>', on_focusin, add="+")
    a.bind('<FocusOut>', on_focusout, add="+")
    
    a.placeholder_state = state

    return state
#--------------------------------------------------------------------------------
rand = StringVar()

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w', bg="white")
lblreference.grid(row=0,column=0)
a = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
#a.insert(0, 'Enter Number here')
#---------------------------------------------------------Add place holder here-----------------------------------------
add_placeholder_to(a, 'Quantity')
#-----------------------------------------------------------------------------------------------------------------------
a.grid(row=0,column=1)
