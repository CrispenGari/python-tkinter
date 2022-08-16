
from commands import Commands
from helperfns.tables import tabulate_data
column_names = ["ID", "USERNAME", "EMAIL", "CREATE AT"]

def deleteUser(cursor, conn, hash):
    try:
        usernameOrEmail = input("Enter username or email: ").strip()
        password = input("Enter the password: ").strip()
        user = cursor.execute(Commands.GET_USER.format(usernameOrEmail, usernameOrEmail)).fetchone()
        hashedPassword = user[-2]
        if hash.verify(hashedPassword, password):
            cursor.execute(Commands.DELETE_USER.format(user[0]))
            conn.commit()
            print("User was Deleted.")
        else:
            print("Invalid Credentials.")
    except Exception as e:
        print("Invalid Credentials.")

def updateUser(cursor, conn, hash):
    try:
        usernameOrEmail = input("Enter username or email: ").strip()
        password = input("Enter new password: ").strip()
        user = cursor.execute(Commands.GET_USER.format(usernameOrEmail, usernameOrEmail)).fetchone()
        if user:
            hashedPassword = hash.hash(password)
            cursor.execute(Commands.UPDATE_USER.format(hashedPassword, user[0]))
            conn.commit()
            print("User password updated.")
        else:
            print("No user with that username or email.")
    except Exception as e:
        print("Invalid Credentials.")

def getUser(cursor, hash):
    try:
        usernameOrEmail = input("Enter username or email: ").strip()
        password = input("Enter the password: ").strip()
        user = cursor.execute(Commands.GET_USER.format(usernameOrEmail, usernameOrEmail)).fetchone()
        hashedPassword = user[-2]
        if hash.verify(hashedPassword, password):
            data = [[user[0], user[1], user[2], user[-1]]]
            tabulate_data(column_names, data, title="User")
        else:
            print("Invalid Credentials.")
    except Exception as e:
        print("Invalid Credentials.")

def getUsers(cursor):
    data = list()
    try:
        users = cursor.execute(Commands.GET_USERS)
        for id, username, email, _, created_at in users:
            data.append([id, username, email, created_at])
        tabulate_data(column_names, data, title="All Users")
    except Exception as e:
        print(e)

def addUser(cursor, conn, hash):
    username = input("Enter the username: ").strip()
    email = input("Enter the email: ").strip()
    password = input("Enter the password: ").strip()
    password = hash.hash(password)
    try:
        cursor.execute(Commands.ADD_USER.format(username, email, password))
        conn.commit()
        print("A user was created.")
    except Exception as e:
        print(e)