from flask_login import UserMixin
import psycopg2

t_host = ""
t_port = ""
t_dbname = ""
t_user = ""
t_pw = ""


class User(UserMixin):
    id = 0
    username = ""
    useremail = ""
    userpassword = ""
    def __init__(self):
        #print("User Instance Created")
        pass

    def get_user(self, user_id):
        db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
        db_cursor = db_conn.cursor()
        db_cursor.execute("SELECT * FROM users WHERE id = %s;",(user_id,))   
        user_row = db_cursor.fetchone()
        db_cursor.close()
        db_conn.close()
        if(user_row):
            #print("User Exists")
            self.id = user_id
            #print(self.id)
            self.username = user_row[1]
            print(self.username)
            self.useremail = user_row[2]
            self.userpassword = user_row[3]
            return self
        else:
            print("User Does Not Exist")
            return None

    def get_username(self):
        if(self.user):
            return self.username
        else:
            print("Username Not Found")
            return None 

    def get_useremail(self):
        if(self.user):
            return self.useremail
        else:
            print("Useremail Not Found")
            return None

    def get_userpassword(self):
        if(self.user):
            return self.userpassword
        else:
            print("Userpassword Not Found")
            return None       

    def __repr__(self):
        return "%d/%s/%s/%s" % (self.id, self.username, self.useremail, self.userpassword)
       








