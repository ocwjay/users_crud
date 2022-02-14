from sqlite3 import connect
from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_db').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_db').query_db(query, data)
        return cls(result[0])
    @classmethod
    def add_new_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUE (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users_db').query_db(query, data)
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=NOW() WHERE ID = %(id)s;"
        return connectToMySQL('users_db').query_db(query, data)
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL('users_db').query_db(query, data)