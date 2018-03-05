
###########################
####### CREATE TABLES #####
###########################

import sqlite3
from sqlite3 import Error
import os


sql_create_application_table = """ CREATE TABLE IF NOT EXISTS  application (
                                    camper_id text PRIMARY KEY,
                                    name_first text,
                                    name_last text,
                                    address text,
                                    age integer,
                                    band_role text, 
                                    roomate_pref integer,
                                    band_pref text,
                                    email text,
                                    camp_dates text,
                                    status text)
                                    ; """
 
sql_create_emergency_contact_table = """CREATE TABLE IF NOT EXISTS emergency_contact (
                            camper_id integer PRIMARY KEY,
                            name_first text,
                            name_last text,
                            emergency_contact text)
                            ;"""


sql_create_legal_table = """CREATE TABLE IF NOT EXISTS legal (
                                    camper_id integer PRIMARY KEY,
                                    name_first text,
                                    name_last text,
                                    age integer,
                                    gender text,
                                    parent text);"""
                                    

sql_create_medical_table = """CREATE TABLE IF NOT EXISTS medical (
                                    camper_id integer PRIMARY KEY,
                                    name_first text,
                                    name_last text,
                                    medical_insturance text,
                                    doctor text,
                                    dentist text,
                                    allergies text,
                                    medications text);"""

sql_create_notification_table = """CREATE TABLE IF NOT EXISTS notification (
                                        camper_id integer PRIMARY KEY,
                                        name_first text,
                                        camp_dates text,
                                        director_decision text,
                                        director_comments text,
                                        director_rank integer,
                                        category text,
                                        letter_type text,
                                        notification_sent_date text);"""

sql_create_check_in_table = """--form's, equiptment, and clothes are boolean 1,0's indicating if camper brought it or not
                                    CREATE TABLE IF NOT EXISTS check_in (
                                    camper_id integer PRIMARY KEY,
                                    check_in_date text,
                                    application_form integer,
                                    emergency_contact_form integer,
                                    legal_form integer,
                                    medical_form integer,
                                    equiptment integer,
                                    clothes integer)
                                    ;"""  

sql_create_dorm_table = """CREATE TABLE IF NOT EXISTS dorm (
                                camper_id integer PRIMARY KEY,
                                camp_date text,
                                dorm_number integer,
                                category text,
                                gender text,
                                age integer);"""  

sql_create_band_table = """CREATE TABLE IF NOT EXISTS band(
                                camper_id integer PRIMARY KEY,
                                camp_date text,
                                band text,
                                category text,
                                gender text,
                                director_rank integer,
                                request text);""" 







def connect_to_db():
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	return c, conn  



def create_tables(c):

	c.execute(sql_create_application_table)


def create_db():
	if os.path.exists("example.db"):
		c, conn = connect_to_db()  
	else:
		c, conn = connect_to_db()
		create_tables(c)

	return c, conn 




def save_db_changes(conn):
	conn.commit()
	conn.close()



"""
# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")



for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
        print(row[0])


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

"""

