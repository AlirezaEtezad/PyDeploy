import bcrypt

password = "1234"
p2 = "1234" 

password_byte = password.encode("utf-8")
hashed = bcrypt.hashpw(password_byte, bcrypt.gensalt())

p2_byte = password.encode("utf-8")

if bcrypt.checkpw(hashed, p2_byte):
    print("match")

print( hashed)