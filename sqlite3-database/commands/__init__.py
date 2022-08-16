
class Commands:
    ADD_USER = "INSERT INTO users(username, email, password) VALUES('{}', '{}', '{}');"
    GET_USER = "SELECT * FROM users WHERE username='{}' OR email='{}' LIMIT 1;"
    GET_USERS = "SELECT * FROM users;"
    UPDATE_USER = "UPDATE users SET password='{}' WHERE id={};"
    DELETE_USER = "DELETE FROM users WHERE id={};"
