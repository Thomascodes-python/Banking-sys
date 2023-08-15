import bcrypt

# Declaring our password
password = b'GeekPassword'

# Adding the salt to password
salt = bcrypt.gensalt()
# Hashing the password
hashed = bcrypt.hashpw(password, salt)

# printing the salt
print("Salt :")
print(salt)

# printing the hashed
print("Hashed")
print(hashed)

if bcrypt.hashpw(password, hashed):
    print('Login Successful')
