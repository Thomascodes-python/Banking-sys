from customtkinter import *  
import customtkinter as ct
import tkinter
from PIL import Image
from tkinter import messagebox
import sqlite3
import bcrypt


ct.set_appearance_mode("light")
ct.set_default_color_theme("dark-blue")

def bankname():
    global logolabel
    logo_img = ct.CTkImage(Image.open("images/logo.png"),size=(140,110))
    logo = ct.CTkLabel(master=root,image=logo_img,text='',text_color="green")
    logo.place(x=550,y=30)
    logolabel = ct.CTkLabel(master=root,text='GLOBUS CITY BANK',text_color="green",font=ct.CTkFont("Roboto",30, 'bold'))
    logolabel.place(x=490,y=0)


def signup_dashboard():
    # parent_frame()
    global signup_page
    signup_page = ct.CTkFrame(master=father_frame,width=350,height=500)
    signup_page.place(x=180,y=20)
    """
    Calling the signup function which contains the entries,label and buttons for the signup
    """
    
    signup_bg_image = ct.CTkImage(Image.open("images\\smartphone.png"),size=(520,400))
    bg_image = ct.CTkLabel(master=father_frame,text="",image=signup_bg_image)
    bg_image.place(x=650,y=70) 
    signup_frame()


def signin_dashboard():
    global signin_page
    signin_page = ct.CTkFrame(master=father_frame,width=350,height=380)
    signin_page.place(x=180,y=20)
    """
    Calling the signin function which contains the entries,label and buttons for the signin
    """
    signin_frame()


def signup_frame():
    global firstname_entry,othernames_entry,sign_up_email_entry,phonenumber_entry,password_entry,checker,comfirm_password_entry,signup_error_label

    signup_text = ct.CTkLabel(master=signup_page,text="SIGN UP",font=general_font)
    signup_text.place(x=120,y=10)

    
    firstname_entry = ct.CTkEntry(master=signup_page,placeholder_text_color="gray",text_color="#1A1A1A",placeholder_text="First Name",width=260)
    firstname_entry.place(x=40,y=70)

    othernames_entry = ct.CTkEntry(master=signup_page,placeholder_text_color="gray",text_color="#1A1A1A",placeholder_text="Other Names",width=260)
    othernames_entry.place(x=40,y=120)

    sign_up_email_entry = ct.CTkEntry(master=signup_page,width=260,placeholder_text_color="gray",text_color="#1A1A1A",placeholder_text="Email")
    sign_up_email_entry.place(x=40,y=170)

    phonenumber_entry = ct.CTkEntry(master=signup_page,width=260,placeholder_text_color="gray",text_color="#1A1A1A",placeholder_text="Phone Number")
    phonenumber_entry.place(x=40,y=220)

    password_entry = ct.CTkEntry(master=signup_page,placeholder_text_color="gray",text_color="#1A1A1A",placeholder_text="Password",width=260)
    password_entry.place(x=40,y=270)

    comfirm_password_entry = ct.CTkEntry(master=signup_page,placeholder_text_color="gray",text_color="#1A1A1A",placeholder_text="Comfirm Password",width=260)
    comfirm_password_entry.place(x=40,y=320)

    checker = IntVar()
    terms_amd_condition_label = ct.CTkCheckBox(master=signup_page,variable=checker,text="I agree to the Terms & Condition",checkmark_color="blue",width=50,checkbox_height=24,checkbox_width=20,height=20)
    terms_amd_condition_label.place(x=40,y=355)

    signup_error_label = ct.CTkLabel(master=signup_page,font=("Helvectica",15,"bold"),text="",text_color="red")
    signup_error_label.place(x=100,y=385)

    signup_button = ct.CTkButton(master=signup_page,text="SIGN UP",font=("Helvectica",14,"bold"),width=140,height=28,command=signup_button_command)
    signup_button.place(x=100,y=420)

    
    haveanaccct_label = ct.CTkLabel(master=signup_page,font=("Helvetica", 14),text="Already Have An Account?",fg_color="transparent")
    haveanaccct_label.place(x=50,y=460)
    
    presigni_button = ct.CTkButton(master=signup_page,hover="none",command=presignin_button_command,font=ct.CTkFont("Helvectica",14,"bold",underline=True),text_color="green",text="SIGN IN",width=14,fg_color="transparent")
    presigni_button.place(x=218,y=460)
    

def signup_button_command():
    first_name = firstname_entry.get()
    othernames= othernames_entry.get()
    email = sign_up_email_entry.get()
    phonenumber = phonenumber_entry.get()
    password = password_entry.get()
    comfirm_password = comfirm_password_entry.get()

    checking_entries_in_signup(first_name,othernames,email,phonenumber,password,comfirm_password) 

def checking_entries_in_signup(f_name,o_names,email,phonenumber,password,con_password):
        if f_name == "" or o_names == "" or email == "" or  phonenumber == "" or password == "" or con_password == "":
            signup_error_label.configure(text="All Feilds Required *")
            print("NOT completed")

        elif password != con_password:
            messagebox.showerror("PASSWORD ERROR","PASSWORD IS NOT SAME WITH COMFIRM PASSWORD")
        
        elif checker.get() == 0:
            messagebox.showerror("Error","KINDLY ACCPET THE TERMS & CONDITION")

        else:
            signup_error_label.configure(text=" ")
            password = hash_password(password.encode())
            save_data_to_db(f_name,o_names,email,phonenumber,password)
            signup_clear_all()
    
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed


def signup_clear_all():
    firstname_entry.delete(0,ct.END)
    othernames_entry.delete(0,ct.END)
    sign_up_email_entry.delete(0,ct.END)
    phonenumber_entry.delete(0,ct.END)
    password_entry.delete(0,ct.END)
    checker.set(0)
    comfirm_password_entry.delete(0,ct.END)

def save_data_to_db(first_name,othernames,email,phonenumber,password):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    connection.execute("""CREATE TABLE IF NOT EXISTS DATA
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, FIRST_NAME text,OTHER_NAMES text,EMAIL text,PHONE_NUMBER int CHAR(11),PASSWORD text)
                            """)

    insert_query = """INSERT INTO DATA
            (FIRST_NAME, OTHER_NAMES, EMAIL, PHONE_NUMBER, PASSWORD)VALUES(?,?,?,?,?)"""

    insert_data = (first_name,othernames,email,phonenumber,password)
    
    cursor.execute(insert_query,insert_data)
    connection.commit()
    connection.close()
    messagebox.showinfo("Success","REGISTRATION SUCCESSFUL")

    
def signin_frame():
    global sign_in_email_entry,sign_in_password_entry,signin_error_label

    signin_text = ct.CTkLabel(master=signin_page,text="SIGN IN",font=general_font)
    signin_text.place(x=120,y=20)

    back_img = ct.CTkImage(Image.open("images\\back_con.png"))
    exit_img = ct.CTkButton(master=signin_page,hover="False",text=" ",command=back_button,width=10,image=back_img,fg_color="transparent")
    exit_img.place(x=0,y=10)

    sign_in_email_entry = ct.CTkEntry(master=signin_page,width=260,placeholder_text="Email")
    sign_in_email_entry.place(x=40,y=120)

    sign_in_password_entry = ct.CTkEntry(master=signin_page,width=260,placeholder_text="Password")
    sign_in_password_entry.place(x=40,y=180)

    forgoten_password_button = ct.CTkButton(master=signin_page,text_color="green",font=ct.CTkFont("Arial",14,underline=True),fg_color="transparent",text="Forgotten Password?")
    forgoten_password_button.place(x=150,y=220)

    signin_error_label = ct.CTkLabel(master=signin_page,text="",font=("Helvectica",15,"bold"),text_color="red")
    signin_error_label.place(x=100,y=260)

    signin_button = ct.CTkButton(master=signin_page,command=signin_button_command,text="SIGN IN",font=("Helvectica",14,"bold"),width=140,height=28)
    signin_button.place(x=100,y=300)



def signin_button_command():

    user_email = sign_in_email_entry.get()
    user_password = sign_in_password_entry.get()
    # signin_button
    checking_entries_in_signin(user_email,user_password)

def checking_entries_in_signin(user_email,user_password):
    if user_email == "" or user_password == "":
        signin_error_label.configure(text="All Feilds Required *")
    else:
        login(user_email, user_password)
        signin_error_label.configure(text="")

def login(email, user_password):
    con=sqlite3.connect('database.db')
    cur=con.cursor()
    statement = f"SELECT * from DATA WHERE EMAIL = '{email}'"
    cur.execute(statement)

    _, _, _, _, _,password = cur.fetchone()

    if bcrypt.hashpw(user_password.encode(), password) == password:
        print('Login Successful')
    else:
        print('Incorrect Details')
    
        
    # elif email=='':
    #     messagebox.showerror("RMS", "Email can't be empty")
    # elif password=='':
    #     messagebox.showerror("RMS", "Password can't be empty")
    # else:
    #     #print('Welcome')
    #     messagebox.showinfo('RMS', 'You have successfully Log in')

def back_button():
    signin_page.place_forget()
    signup_dashboard()
    # logo()
    # signup_frame()

def presignin_button_command():
    signup_page.place_forget()
    # logolabel.place_forget()
    signin_dashboard()


if __name__=="__main__":

    root = ct.CTk()
    root.geometry("1200x670+50+10")

    general_font = ct.CTkFont(family="Roboto",size=26,weight="bold")

    father_frame = ct.CTkFrame(master=root,width=1150,height=540,fg_color="transparent")
    father_frame.place(x=22,y=120)

    
    bankname()
    signup_dashboard()

    root.mainloop()
    
