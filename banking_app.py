# from logging import root
from customtkinter import *  
import customtkinter as ct
import tkinter
from PIL import Image
from tkinter import messagebox
# from PIL import Image


ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")
######################################################################################################
                        #Logo
def bankname():
    global logolabel
    # logo_img = ct.CTkImage(Image.open("logo.png"),size=(140,110))
    logolabel = ct.CTkLabel(master=root,text="GLOBUS CITY BANK",text_color="green",font=ct.CTkFont("Roboto",30))
    logolabel.place(x=460,y=25)

# def logo():
#     global logolabel
#     logo_img = ct.CTkImage(Image.open("logo.png"),size=(140,110))
#     logolabel = ct.CTkLabel(master=root,image=logo_img,text="",fg_color="transparent")
#     logolabel.place(x=550,y=5)


######################################################################################################
                       #CHILDREN FRAME

def signup_dashboard():
    # parent_frame()
    global signup_page
    signup_page = ct.CTkFrame(master=father_frame,width=350,height=500)
    signup_page.place(x=180,y=20)
    """
    Calling the signup function which contains the entries,label and buttons for the signup
    """
    
    signup_bg_image = ct.CTkImage(Image.open("images\\1.png"),size=(340,360))
    bg_image = ct.CTkLabel(master=father_frame,text="",image=signup_bg_image)
    bg_image.place(x=750,y=70) 
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

    ################################

    #######################################################################################################
                    #SIGN UP ENTRIES,BUTTONS AND LABEL

    signup_text = ct.CTkLabel(master=signup_page,text="SIGN UP",font=general_font)
    signup_text.place(x=120,y=10)

    #######################################################################################################
    
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

    #########################################################################################################
    
    haveanaccct_label = ct.CTkLabel(master=signup_page,font=("Helvetica", 14),text="Already Have An Account?",fg_color="transparent")
    haveanaccct_label.place(x=50,y=460)
    
    presigni_button = ct.CTkButton(master=signup_page,hover="none",command=presignin_button_command,font=ct.CTkFont("Helvectica",14,"bold",underline=True),text_color="green",text="SIGN IN",width=14,fg_color="transparent")
    presigni_button.place(x=218,y=460)
    

def signup_button_command():
    global first_name,othernames,email,phonenumber,password,comfirmpassword
    first_name = firstname_entry.get()
    othernames= othernames_entry.get()
    email = sign_up_email_entry.get()
    phonenumber = phonenumber_entry.get()
    password = password_entry.get()
    comfirmpassword = comfirm_password_entry.get()

    # print("your comfirm password is" + ( comfirmpassword))
    # print(first_name,othernames,email,phonenumber,password,comfirmpassword)
    checking_entries_in_signup()

def checking_entries_in_signup():    
    if first_name == "" or othernames == "" or email == "" or  phonenumber == "" or password == "" or comfirmpassword == "":
        signup_error_label.configure(text="All Feilds Required *")
        print("NOT completed")

    else:
        signup_error_label.configure(text=" ")
        print("COMPLETED")

    if checker.get() == 0:
        messagebox.showerror("Error","KINDLY ACCPET THE TERMS AND CONDITIO")

    if password != comfirmpassword:
        messagebox.showerror("PASSWORD ERROR","PASSWORD IS NOT SAME WITH COMFIRM PASSWORD")
        pass 
    else:
        print("correct")

def signin_frame():
    global sign_in_email_entry,sign_in_password_entry,signin_error_label
    ########################################################################################################
                        #SIGN UP ENTRIES,BUTTONS AND LABEL

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
    global user_email,user_password
    user_email = sign_in_email_entry.get()
    user_password = sign_in_password_entry.get()
    print(user_email,user_password)
    # signin_button
    checking_entries_in_signin()

def checking_entries_in_signin():
    if user_email == "" or user_password == "":
        signin_error_label.configure(text="All Feilds Required *")
    else:
        signin_error_label.configure(text="")
# def logo():
    # log0frame = ct.CTkFrame(master=root,width=1000,height=100).place(x=20,y=10)
    # logo_img = ct.CTkImage(Image.open("logo.png"),size=(100,100))
    # logolabel = ct.CTkLabel(master=log0frame,image=logo_img,text="")
    # logolabel.place(x=10,y=20)

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
    root.geometry("1200x670+60+20")

    general_font = ct.CTkFont(family="Roboto",size=26,weight="bold")
    
    ######################################################################################################
                        #PARENT FRAME

    father_frame = ct.CTkFrame(master=root,width=1150,height=540)
    father_frame.place(x=22,y=120)
    
    # log0frame = ct.CTkFrame(master=root,width=1000,height=100).place(x=20,y=10)
    # logo_img = ct.CTkImage(Image.open("logo.png"),size=(140,110))
    # logolabel = ct.CTkLabel(master=root,image=logo_img,text="",fg_color="blue")
    # logolabel.place(x=550,y=5)

    ######################################################################################################
    
    bankname()
    # logo()
    signup_dashboard()

    

    root.mainloop()
    

    # logo = ct.CTkImage(Image.open("logo.png"),size=((160,100)))
    # logo = ct.CTkLabel(root,text=" ",image=logo,fg_color="transparent")
    # logo.place(x=550,y=40)
