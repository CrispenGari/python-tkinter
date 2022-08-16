
import sqlite3
from argon2 import PasswordHasher
from functions import *

# from pip._internal import main as install
# try:
#     import argon2
# except ImportError:
#     install(["install", "argon2-cffi"])


conn = sqlite3.connect("./db/users.db")
cursor = conn.cursor()
hash = PasswordHasher(salt_len=12)

# cursor.execute("DROP TABLE IF EXISTS users;")
with open('./sql/table.sql', 'r') as reader:
    CREATE_TABLE_SQL = reader.read().strip()

cursor.execute(CREATE_TABLE_SQL)

# CRUD operations

while True:
    choice = int(input('''Choose: 1. add user 2. get user 3. update user 4. delete user 5. get all users 0. exit\n'''))
    if choice == 0:
        break
    if choice < 0 or choice > 5:
        break

    if choice == 1:
        addUser(cursor, conn, hash)
    elif choice == 2:
        getUser(cursor, hash)
    elif choice == 3:
        updateUser(cursor, conn, hash)
    elif choice == 4:
        deleteUser(cursor, conn, hash)
    else:
        getUsers(cursor)

conn.close()