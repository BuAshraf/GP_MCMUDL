
from tkinter import*  
from PIL import Image, ImageTk
from tkinter import filedialog
import PIL
from help import predict_image
from users import USERS
def close_win(root):
   root.destroy()

def wellcome():
    well=Tk()
    well.configure(bg='#A9B2F1')
    well.geometry('600x500')  
    well.title("Wellcome")
    Button(well, text='login',width=20,bg='#8359E3',fg='white',borderwidth=0,command= lambda:Login(well)).place(x=230,y=210)  
    Button(well, text='Register',width=20,bg='#8359E3',fg='white',borderwidth=0,command= lambda:Register(well)).place(x=230,y=250) 
    well.mainloop()

def loginLogic(email,password,win):
    for i in USERS:
        if i['Email']==email and i['password']==password:
            main_function(win)
        else :
            Label(win, text="Password or Email is not correct",bg='#A9B2F1',borderwidth=0).place(x=200, y=270)


def Login(win):
    close_win(win)
    login=Tk()
    login.configure(bg='#A9B2F1')
    login.geometry('600x500')  
    login.title("Sign In")
    Label(login, text="Email", bg="#A9B2F1").place(x=200, y=190)
    email=Entry(login,borderwidth=0)
    email.place(x=280,y=190)


    Label(login, text="Password",borderwidth=0, bg="#A9B2F1").place(x=200, y=220)
    password=Entry(login,borderwidth=0)
    password.place(x=280,y=220)
    Button(login, text='Sign In',width=20,bg='#8359E3',fg='white',borderwidth=0,command=lambda:loginLogic(email.get(),password.get(),login)).place(x=230,y=250) 
    login.mainloop()

def registerLogic(email,password,repass,win):
    if password==repass:
        USERS.append(
        {
            'id':USERS[-1]['id']+1,
            'Email':email,
            'password':password
        },
        )
        main_function(win)
    else:
        Label(win, text="Re password don't match with Password",bg='#A9B2F1',borderwidth=0).place(x=200, y=270)



def Register(win):
    close_win(win)
    register=Tk()
    register.configure(bg='#A9B2F1')
    register.geometry('600x500')  
    register.title("Sign Up")
    Label(register, text="Email", bg="#A9B2F1").place(x=200, y=190)
    email=Entry(register,borderwidth=0)
    email.place(x=280,y=190)


    Label(register, text="Password",borderwidth=0, bg="#A9B2F1").place(x=200, y=220)
    password=Entry(register,borderwidth=0)
    password.place(x=280,y=220)

    Label(register, text="Re Password",borderwidth=0, bg="#A9B2F1").place(x=200, y=250)
    repassword=Entry(register,borderwidth=0)
    repassword.place(x=280,y=250)

    Button(register, text='Sign Up',width=20,bg='#8359E3',fg='white',borderwidth=0,command= lambda:registerLogic(email.get(),password.get(),repassword.get(),register)).place(x=230,y=280) 
    register.mainloop()


  
def main_function(win):
    close_win(win)
    path=''
    root = Tk()
    root.title('Melanoma Classification')
    # Adjust size
    root.geometry("640x530")
    root.configure(bg='#A9B2F1')
    #################################################################
    def select_image():
        path=filedialog.askopenfilename(filetypes=[("Image File",'.*')])
        im = PIL.Image.open(path)
        tkimage = ImageTk.PhotoImage(im)
        myvar=Label(root,image = tkimage)
        myvar.image = tkimage
        myvar.pack()
        res= predict_image(path)
        
        Label(root, text="The predicted class of this image is  {}".format(res),bg='#A9B2F1',borderwidth=0).place(x=180, y=455)

    print(path)
    b=Button(root,text="Predict",width=15,bg='#8359E3',fg='white',borderwidth=0,command=lambda:select_image()).place(x=250,y=490)


    root.mainloop()

wellcome()
