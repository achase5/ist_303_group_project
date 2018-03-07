
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
                                    gender text,
                                    age integer,
                                    band_role text, 
                                    roomate_pref integer,
                                    band_pref text,
                                    email text,
                                    camp_dates text,
                                    status text,
                                    payment text)
                                    ; """
 
sql_create_emergency_contact_table = """CREATE TABLE IF NOT EXISTS emergency_contact (
                            camper_id text PRIMARY KEY,
                            name_first text,
                            name_last text,
                            emergency_contact text)
                            ;"""


sql_create_legal_table = """CREATE TABLE IF NOT EXISTS legal (
                                    camper_id text PRIMARY KEY,
                                    name_first text,
                                    name_last text,
                                    age integer,
                                    parent text);"""
                                    

sql_create_medical_table = """CREATE TABLE IF NOT EXISTS medical (
                                    camper_id text PRIMARY KEY,
                                    medical_insturance text,
                                    doctor text,
                                    dentist text,
                                    allergies text,
                                    medications text);"""

sql_create_notification_table = """CREATE TABLE IF NOT EXISTS notification (
                                        camper_id text PRIMARY KEY,
                                        name_first text,
                                        camp_dates text,
                                        director_decision text,
                                        director_comments text,
                                        director_rank integer,
                                        category text,
                                        letter_type text,
                                        notification_sent_date text);"""

sql_create_check_in_table = """CREATE TABLE IF NOT EXISTS check_in (
                                    camper_id text PRIMARY KEY,
                                    check_in_date text,
                                    has_checked_in integer,
                                    application_form integer,
                                    emergency_contact_form integer,
                                    legal_form integer,
                                    medical_form integer,
                                    equiptment integer,
                                    clothes integer)
                                    ;"""  

sql_create_dorm_table = """CREATE TABLE IF NOT EXISTS dorm (
                                camper_id text PRIMARY KEY,
                                camp_date text,
                                dorm_number integer,
                                category text,
                                gender text,
                                age integer);"""  

sql_create_band_table = """CREATE TABLE IF NOT EXISTS band(
                                camper_id text PRIMARY KEY,
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
	c.execute(sql_create_emergency_contact_table)
	c.execute(sql_create_legal_table)
	c.execute(sql_create_medical_table)
	c.execute(sql_create_notification_table)
	c.execute(sql_create_check_in_table)
	c.execute(sql_create_dorm_table)
	c.execute(sql_create_band_table)


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





