import sqlite3



def login(email):
    statement = f"SELECT * from DATA WHERE EMAIL = '{email}'"
    cur.execute(statement)

    output = cur.fetchone() # This returns a tuple of data in the email and password column
    # For loop that iterates through the loop
    print(output)

    con.commit()
    con.close()



    


def sign_up():
    con.execute("""CREATE TABLE IF NOT EXISTS DATA
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, FIRST_NAME text,OTHER_NAMES text,EMAIL text,PHONE_NUMBER int CHAR(11),PASSWORD text)
                            """) #Using the execution function to create a table called DATA

    insert_query = """INSERT INTO DATA
            (FIRST_NAME, OTHER_NAMES, EMAIL, PHONE_NUMBER, PASSWORD)VALUES(?,?,?,?,?)"""

    insert_data = (first_name,last_name,email,phone_number,password)
    
    cur.execute(insert_query,insert_data)
  

if __name__=='__main__':
    con=sqlite3.connect('database.db') #Creating the database called database
    cur=con.cursor()

#  The User's Data to save in your database
    first_name = 'Solomon'
    last_name = 'Bestz'
    email = 'ojikeglobus@gmail.com'
    phone_number = '97839373863'
    password = 'aaaaa'

    login(email)

    


    
