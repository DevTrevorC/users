from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod 
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(firstName)s, %(lastName)s, %(email)s, now(), now());"
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def del_user(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users').query_db(query, {'id': id})

    @classmethod
    def get_user(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query, {'id': id})[0]

    @classmethod
    def edit_user(cls, data):
        query = "UPDATE users SET first_name = %(firstName)s, last_name = %(lastName)s, email = %(email)s, updated_at = now() where id = %(id)s"
        return connectToMySQL('users').query_db(query, data)