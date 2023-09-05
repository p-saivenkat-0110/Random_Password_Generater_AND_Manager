import random
import dbm
import os
import tkinter

os.chdir(r"C:\Users\saive\OneDrive\Desktop\CODING WORK\Python programs\Random Password Generator")

accountsDB = dbm.open("accountsDB", 'c')
access_to_save = False

# 8 : (1 up + 2 lc + 2 num + 3 spc)
# 9 : (2 up + 2 lc + 2 num + 3 spc)
# 10: (2 up + 3 lc + 2 num + 3 spc)
# 11: (2 up + 3 lc + 3 num + 3 spc)
# 12: (2 up + 4 lc + 3 num + 3 spc)
# 13: (2 up + 4 lc + 3 num + 4 spc)
# 14: (3 up + 4 lc + 3 num + 4 spc)
# 15: (3 up + 4 lc + 4 num + 4 spc)

class allChars:
    def __init__(self):
        self.special_chars = ['~', '!', '@', '#', '$', '%',
                              '^', '&', '*','=', '+', '_',
                              '<', '>', '?', '[', ']', '{', '}']

        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        self.lower_case = ['a', 'b', 'c', 'd', 'e', 'f',
                           'g', 'h', 'i', 'j', 'k', 'l',
                           'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x',
                           'y', 'z']

        self.upper_case = ['A', 'B', 'C', 'D', 'E', 'F',
                           'G', 'H', 'I', 'J', 'K', 'L',
                           'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X',
                           'Y', 'Z']

    def generate(self):
        self.password_length = random.choice(range(8,17))
        if self.password_length==8:
            up  = 1
            lc  = 2
            num = 2
            spc = 3
        elif self.password_length==9:
            up  = 2
            lc  = 2
            num = 2
            spc = 3
        elif self.password_length==10:
            up  = 2
            lc  = 3
            num = 2
            spc = 3
        elif self.password_length==11:
            up  = 2
            lc  = 3
            num = 3
            spc = 3
        elif self.password_length==12:
            up  = 2
            lc  = 4
            num = 3
            spc = 3
        elif self.password_length==13:
            up  = 2
            lc  = 4
            num = 3
            spc = 4
        elif self.password_length==14:
            up  = 3
            lc  = 4
            num = 3
            spc = 4
        elif self.password_length==15:
            up  = 3
            lc  = 4
            num = 4
            spc = 4
        else:
            up  = 4
            lc  = 4
            num = 4
            spc = 4

        str_u = [random.choice(self.upper_case)    for _ in range(up)]
        str_l = [random.choice(self.lower_case)    for _ in range(lc)]
        str_n = [random.choice(self.numbers)       for _ in range(num)]
        str_s = [random.choice(self.special_chars) for _ in range(spc)]
        pswrd = str_u+str_l+str_n+str_s
        random.shuffle(pswrd)

        return ("".join(pswrd))


class interface(allChars):
    def LOGIN(self):
        login_window = tkinter.Tk()
        screen_width  = login_window.winfo_screenwidth()
        screen_height = login_window.winfo_screenheight()
        login_window.state('zoomed')
        login_window.title("Login")

        bg_login = tkinter.PhotoImage(file="login.png")
        bg_Label = tkinter.Label(login_window,
                                 width=screen_width,
                                 height=screen_height,
                                 image=bg_login)

        bg_Label.pack()

        def goto_signup():
            login_window.destroy()
            self.SIGNUP()

        def verify():
            get_username = username_entry.get()
            get_password = password_entry.get()
            if len(get_username)==0:
                info2["text"] = "Enter Username"
            else:
                if get_username.encode() in accountsDB:
                    if get_password == accountsDB[get_username].decode():
                        info2['text'] = "Login successful"
                    else:
                        if len(get_password)==0:
                            info2["text"] = "Enter Password"
                        else:
                            info2['text'] = "Invalid Password!!"
                else:
                    info2["text"] = "Invalid Username!!"

        def forgot():
            search_username = username_entry.get()
            if search_username.encode() in accountsDB:
                def show():
                    info2["text"] = f"Your password is {accountsDB[search_username].decode()}"
                def fetch():
                    info2["text"] = "Fetching your password..."
                    info2.after(8000,show)
                def verified():
                    info2["text"] = "Verified"
                    info2.after(1000,fetch)
                def verify_email():
                    info2["text"] = "Verification code is sent to your E-mail"
                    info2.after(3500,verified)
                verify_email()

            else:
                if len(search_username)==0:
                    info2["text"] = "Enter Username"
                else:
                    info2["text"] = "Invalid Username!!"

        def saved():
            password_entry.delete(0, 'end')
            find_username = username_entry.get()
            if len(find_username) == 0:
                info2["text"] = "Enter Username/Password"
            else:
                fptr = open(r'remember_me.txt', 'r')
                username_list = fptr.readlines()
                fptr.close()
                if find_username + '\n' in username_list:
                    pswrd = accountsDB[find_username]
                    password_entry.insert(0,pswrd.decode())
                else:
                    info2['text'] = "Password not saved for this username"

        frame = tkinter.Frame(login_window,
                              width=400, height=500,
                              bg="black")

        frame.place(x=1000,y=100)

        loginL = tkinter.Label(frame,
                               text="LOGIN",
                               fg="white", bg="black",
                               font=("Times New Roman", 50, 'bold'),
                               pady=65)

        loginL.pack(anchor="center")

        frame1 = tkinter.Frame(frame,
                               width=400, height=400,
                               bg="black")

        frame1.pack(padx=10, pady=20)

        frame2 = tkinter.Frame(frame,
                               width=400,
                               height=200,
                               bg="black")

        frame2.pack(padx=10, pady=20)

        info2 = tkinter.Label(frame,
                              fg="yellow", bg="black",
                              width=32,
                              font=("Times New Roman", 14, 'italic'))

        info2.pack(anchor="center")

        username = tkinter.Label(frame1,
                                 text="Username ",
                                 height=1,
                                 font=("Times of Roman", 14, 'bold'))

        username.grid(row=0, column=0, pady=10, padx=5)

        username_entry = tkinter.Entry(frame1,
                                       width=30,
                                       bd=3,
                                       font=(15))

        username_entry.grid(row=0, column=1, pady=10, padx=15, sticky='e')

        password = tkinter.Label(frame1,
                                 text="Password ",
                                 height=1,
                                 font=("Times of Roman", 14, 'bold'))

        password.grid(row=1, column=0, pady=10, padx=5)

        password_entry = tkinter.Entry(frame1,
                                       width=30,
                                       font=(15),
                                       bd=3)

        password_entry.grid(row=1, column=1, pady=10, padx=15, sticky='e')

        savedButton = tkinter.Button(frame2,
                                      text="Remembered me?",
                                      padx=0, pady=0,
                                      bd=0, borderwidth=2,
                                      font=("Times New Roman", 13, 'italic'),
                                      command=saved)

        savedButton.place(x=55, y=19)

        ForgetButton = tkinter.Button(frame2,
                                      text="Forgot password?",
                                      padx=0, pady=0,
                                      bd=0, borderwidth=2,
                                      font=("Times New Roman", 13, 'italic'),
                                      command=forgot)

        ForgetButton.place(x=215, y=19)

        loginButton1 = tkinter.Button(frame2,
                                      text="Login",
                                      width=30,
                                      padx=0, pady=0,
                                      bd=0,
                                      borderwidth=2,
                                      font=("Times New Roman", 15, 'italic'),
                                      command=verify)

        loginButton1.place(x=38, y=67)

        signupButton = tkinter.Button(frame2,
                                      text="Don't have account? Sign Up",
                                      width=30,
                                      padx=0, pady=0,
                                      bd=0, borderwidth=2,
                                      font=("Times New Roman", 15, 'italic'),
                                      command=goto_signup)

        signupButton.place(x=38, y=118)

        login_window.mainloop()

    def SIGNUP(self):
        signUP_window = tkinter.Tk()
        screen_width = signUP_window.winfo_screenwidth()
        screen_height = signUP_window.winfo_screenheight()
        signUP_window.state('zoomed')
        signUP_window.title("Create Account")

        signup = tkinter.PhotoImage(file="signup.png")
        bg_signup = tkinter.Label(signUP_window,
                                  width=screen_width,
                                  height=screen_height,
                                  image=signup)
        bg_signup.pack()

        def gotoLogin():
            signUP_window.destroy()
            self.LOGIN()

        def remember():
            find_username = username_entry.get()
            pswrd = password_entry.get()
            if len(find_username)==0 or len(pswrd)==0:
                info["text"] = "Enter username/password"
            elif len(pswrd)<8 or len(pswrd)>16:
                info["text"] = "Password must be of 8-16 characters"
            else:
                fptr = open(r'remember_me.txt','r')
                username_list = fptr.readlines()
                fptr.close()
                if find_username+'\n' in username_list:
                    info['text'] = "Password already saved"
                else:
                    fptr = open(r'remember_me.txt', 'a')
                    fptr.write(find_username+'\n')
                    fptr.close()
                    info['text'] = "Password saved successfully"

        def createAccount():
            global access_to_save
            info["text"] = ""
            get_name = name_entry.get()
            get_email = email_entry.get()
            get_username = username_entry.get()
            get_password = password_entry.get()
            if len(get_name)==0:
                info["text"] = "Enter your Name"
            else:
                if len(get_email)==0:
                    info["text"] = "Enter your E-mail"
                else:
                    if len(get_username)==0:
                        info["text"] = "Enter username"
                    else:
                        if get_username.encode() in accountsDB:
                            info["text"] = "Username already exists...\nChoose a different username"
                        else:
                            if 8<=len(get_password)<=16:
                                accountsDB[get_username] = get_password
                                if access_to_save:
                                    remember()
                                    access_to_save=False
                                info["text"] = "Account created successfully... Please Login"
                                accountButton["state"] = "disabled"
                                suggestButton['state'] = 'disabled'
                            else:
                                info["text"] = "Password must be of 8-16 characters"

        def suggestpass():
            global access_to_save
            password_entry.delete(0,'end')
            generated_password = self.generate()
            password_entry.insert(0,generated_password)
            suggestButton["text"] = "Suggest another password"
            access_to_save = True


        frame = tkinter.Frame(signUP_window,
                               width=500, height=400,
                               bg="#2e0742")

        frame.place(x=500,y=75)

        signupL = tkinter.Label(frame,
                                text="SIGN UP",
                                fg="white",
                                bg="#2e0742",
                                font=("Times New Roman", 50, 'bold'),
                                pady=65)

        signupL.pack(anchor="center")



        frame1 = tkinter.Frame(frame,
                               width=500,
                               bg="#2e0742")

        frame1.pack(padx=10, pady=0)

        frame2 = tkinter.Frame(frame,
                               width=400, height=150,
                               bg="#2e0742")

        frame2.pack(padx=10, pady=5)

        name = tkinter.Label(frame1,
                             text="Name ",
                             height=1,width=8,
                             font=("Times of Roman", 14, 'bold'))

        name.grid(row=0, column=0, pady=10, padx=5)

        name_entry = tkinter.Entry(frame1,
                                   width=30,
                                   bd=3,
                                   font=(15))

        name_entry.grid(row=0, column=1, pady=10, padx=15)

        email = tkinter.Label(frame1,
                              text="Email ",
                              height=1, width=8,
                              font=("Times of Roman", 14, 'bold'))

        email.grid(row=1, column=0, pady=10, padx=5)

        email_entry = tkinter.Entry(frame1,
                                    width=30,
                                    bd=3,
                                    font=(15))

        email_entry.grid(row=1, column=1, pady=10, padx=15)

        username = tkinter.Label(frame1,
                                 text="Username ",
                                 height=1,
                                 font=("Times of Roman", 14, 'bold'))

        username.grid(row=2, column=0, pady=10, padx=5)

        username_entry = tkinter.Entry(frame1,
                                       width=30, bd=3,
                                       font=(15))

        username_entry.grid(row=2, column=1, pady=10, padx=15)

        password = tkinter.Label(frame1,
                                 text="Password ",
                                 height=1,
                                 font=("Times of Roman", 14, 'bold'))

        password.grid(row=3, column=0, pady=10, padx=5)

        password_entry = tkinter.Entry(frame1,
                                       width=30,
                                       font=(15),
                                       bd=3)

        password_entry.grid(row=3, column=1, pady=10, padx=15)

        rememberButton = tkinter.Button(frame1,
                                       text="Remember Me",
                                       padx=0, pady=0,
                                       bd=0, borderwidth=2,
                                       font=("Times New Roman", 11, 'italic'),
                                        command=remember)

        rememberButton.grid(row=4, column=1, sticky='w', padx=15)

        suggestButton = tkinter.Button(frame1,
                                       text="Suggest a password",
                                       padx=0, pady=0,
                                       bd=0, borderwidth=2,
                                       font=("Times New Roman", 11, 'italic'),
                                       command=suggestpass)

        suggestButton.grid(row=4,column=1,sticky='e',padx=15)

        info = tkinter.Label(frame,
                             bg="#2e0742",fg="yellow",
                             width=50,height=2,
                             font=("Times New roman", 15, "italic"))

        info.pack(pady=15)

        accountButton = tkinter.Button(frame2,
                                       text="Create Account",
                                       width=30,
                                       padx=0, pady=0,
                                       bd=0, borderwidth=2,
                                       font=("Times New Roman", 15, 'italic'),
                                       command=createAccount)

        accountButton.place(x=30, y=50)

        loginButton = tkinter.Button(frame2,
                                     text="Already have account? Login",
                                     width=30,
                                     padx=0, pady=0,
                                     bd=0, borderwidth=2,
                                     font=("Times New Roman", 15, 'italic'),
                                     command=gotoLogin)

        loginButton.place(x=30, y=100)

        signUP_window.mainloop()


start = interface()
start.SIGNUP()

accountsDB.close()