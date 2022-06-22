from app import db_conn
import psycopg2

#database connection: method two - psycopg2
t_host = ""
t_port = ""
t_dbname = ""
t_user = ""
t_pw = ""

db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()

sql_scripts_create = [
    "CREATE TABLE order_table (order_id SERIAL PRIMARY KEY, order_number integer NOT NULL, order_total_amount double precision NOT NULL, transaction_id character varying NOT NULL, card_cvc integer NOT NULL, card_expiry_month character varying NOT NULL, card_expiry_year character varying NOT NULL, order_status character varying NOT NULL, card_holder_number character varying NOT NULL, email_address character varying NOT NULL, customer_name character varying NOT NULL, customer_address character varying NOT NULL, customer_city character varying NOT NULL, customer_pin character varying NOT NULL, customer_state character varying NOT NULL, customer_country character varying NOT NULL);",

    "CREATE TABLE order_item (order_item_id SERIAL PRIMARY KEY NOT NULL, order_id integer NOT NULL, order_item_name character varying NOT NULL, order_item_quantity integer NOT NULL, order_item_price double precision NOT NULL);"
]

sql_scripts_insert = [
    "INSERT INTO administrator (username, smtp_email, smtp_email_pwd, level, administrator_pwd) VALUES ('juaneric','smtp.gmail.com', 'Dubai2015*', 1, 'mySQLdb03')",

    "INSERT INTO favorite_topics (topic, description, recommended_user, comments) VALUES ('Book', 'Paperback or Digital Reading Material', 'juan', 'Reading takes you on a special journey through the soul.'), ('Quote', 'Personal or Replicated', 'juan', 'Our daily mantras to help us manage and prosper in life.')",

    "INSERT INTO favorite_topics (topic, description, recommended_user, comments) VALUES ('Social', 'Select a wide range of online communications media including facebook, twitter, instagram, etc.', 'juan', 'Keeping in touch with friends and family around the world'), ('Breakfast', 'The most important meal of the day.', 'Juan', 'A good breakfast gives you the energy to have a great day.'), ('Movie', 'The number one entertainment is cinema in short or long form.', 'Juan',	'The easiest social activity to participate in is the movie.'), ('Song', 'Music sooths all souls, especially SOUL music.', 'Juan', 'Singing to a treasure beat lights up the momnent.');",

    "INSERT INTO order_table (order_number, order_total_amount, transaction_id, card_cvc, card_expiry_month, card_expiry_year, order_status, card_holder_number, email_address, customer_name, customer_address, customer_city, customer_pin, customer_state, customer_country) VALUES (1234, 10.00, 'abcd', );",

    "INSERT INTO order_item (username, email, password) VALUES ('johnson', 'johnson@email.com', 'users_3');",

    "INSERT INTO users (username, email, password) VALUES ('johnson', 'johnson@email.com', 'users_3');"
]

sql_scripts_select = [
    "SELECT * FROM users;",
    "SELECT * FROM adminstrator",
    "SELECT * FROM favorite_topics",
    "SELECT * FROM favorites",
    "SELECT * FROM order_item",
    "SELECT * FROM order_table",
    "SELECT * FROM smtp_accounts",
    "SELECT * FROM tbl_product",
    "SELECT * FROM trivia_question",
    "SELECT * FROM users",    
]

'''
sql_Command = sql_scripts_create[0]
db_cursor.execute(sql_Command)

try:
    db_conn.commit()
except psycopg2.Error as e:
    t_msg = "Login: Database error: " + e + "/n SQL: " + s
    print(t_msg)

sql_Command = sql_scripts_select
db_cursor.execute(sql_Command)
rows = db_cursor.fetchall()

for row in rows:
    print(f"{row[0]} {row[1]} {row[2]}")


sql_Command = sql_scripts_insert[2]
db_cursor.execute(sql_Command)

try:
    db_conn.commit()
except psycopg2.Error as e:
    t_msg = "Login: Database error: " + e + "/n SQL: " + sql_Command
    print(t_msg)

'''



#sql_scripts_find = "SELECT * FROM users WHERE username = " + str(username) + " LIMIT 1;"
#sql_scripts_find = "SELECT * FROM users WHERE username = {} LIMIT 1;".format(username)
#sql_scripts_find = "SELECT * FROM users WHERE username = %1 LIMIT 1;" % username
#sql_scripts_find = f"SELECT * FROM users WHERE username = {username} LIMIT 1;"

username = 'juan'
db_cursor.execute("SELECT * FROM users WHERE username = %s;",(username,))

#users = db_cursor
#print(users)

#users = list(db_cursor)
#print users

#user_row = db_cursor.fetchone()
#print(user)

#users = db_cursor
#for record in users:
    #print(record)    

user = db_cursor.fetchone()
print(user)

db_cursor.close()
db_conn.close()


