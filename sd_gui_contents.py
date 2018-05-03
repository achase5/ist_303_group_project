import os.path
import pickle
import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QButtonGroup, QCheckBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenuBar, qApp, QLineEdit, QTextEdit)
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from sqlite_dbv3 import * 
from sd_dorm_assign import *
from sd_band_assign import *
from sd_2nd_band_assign import *



class Window(QWidget):

	def __init__(self):

		super().__init__()

		self.v_layout = QVBoxLayout()

		self.init_ui()

	def init_ui(self):

		#self.setStyleSheet("background-image: url(http://jdrachel.com/wp-content/uploads/2016/01/rock-concert.jpg);")
		welcome_label = QLabel("Welcome to the Future Rock Stars Camp\n Registration System")
		#self.welcome_label.setFont(QFont('Comic Sans', 30))
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)

		self.v_layout.addWidget(welcome_label)
		self.setLayout(self.v_layout)
		
		self.show()

	def maintenance_mode_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Enter Maintenance Mode")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		password_box = QHBoxLayout()
		pw_label = QLabel("Enter Maintenance Mode Password: ")
		pw = QLineEdit()
		pw.setEchoMode(QLineEdit.Password)
		submit_btn = QPushButton('Enter')
		password_box.addWidget(pw_label)
		password_box.addWidget(pw)
		password_box.addWidget(submit_btn)

		self.v_layout.addLayout(password_box)
		submit_btn.clicked.connect(lambda: self.maintenance_mode_btn_clk(pw))


	def maintenance_mode_btn_clk(self, pw):
		if pw.text() == "campers123":
			self.clearLayout(self.v_layout)
			clear_db_box = QHBoxLayout()
			clear_db = QPushButton("Clear the Entire Camper Database")
			warning_label = QLabel("**Warning: This Action Cannot Be Undone")
			clear_db_box.addWidget(clear_db)
			clear_db_box.addWidget(warning_label)
			self.v_layout.addLayout(clear_db_box)

			clear_db.clicked.connect(self.clear_database)
		else:
			self.maintenance_mode_ui()
			self.v_layout.addWidget(QLabel("ACCESS DENIED."))


	def clear_database(self):
		try:
			os.remove("example.db")
		except FileNotFoundError:
			print("*** ERROR: Database has already been cleared. ***")

		pickle_dorm_files = ["June_male_dorms.p", "July_male_dorms.p", "August_male_dorms.p", "June_female_dorms.p", "July_female_dorms.p", "August_female_dorms.p"]
		pickle_band_files = ["band_assignments_June.p", "band_assignments_July.p", "band_assignments_August.p", "band_rankings.p"]
		
		for i in pickle_dorm_files:
			if(os.path.exists(i)):
				os.remove(i)

		for i in pickle_band_files:
			if(os.path.exists(i)):
				os.remove(i)

		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Database Has Been Successfully Cleared.")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)




	def check_in_ui(self):

		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Welcome to the Offical Check-In Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		camper_id_box = QHBoxLayout()
		camper_id_label = QLabel("Please Enter Camper's ID: ")
		camper_id = QLineEdit()
		camper_id_box.addWidget(camper_id_label)
		camper_id_box.addWidget(camper_id)
		self.v_layout.addLayout(camper_id_box)

		equip_box = QHBoxLayout()
		equip_label = QLabel("Does the Camper has his/her Equipment/Supplies Ready? ")
		equip_group = QButtonGroup()
		yes = QRadioButton("Yes")
		no = QRadioButton("No")
		yes.setChecked(True) 
		equip_box.addWidget(equip_label)
		equip_box.addWidget(yes)
		equip_group.addButton(yes)
		equip_box.addWidget(no)
		equip_group.addButton(no)
		self.v_layout.addLayout(equip_box)

		clothes_box = QHBoxLayout()
		clothes_label = QLabel("Does the Camper have Clothes Sufficient for 7 days? ")
		clothes_group = QButtonGroup()
		yes = QRadioButton("Yes")
		no = QRadioButton("No")
		yes.setChecked(True) 
		clothes_box.addWidget(clothes_label)
		clothes_box.addWidget(yes)
		clothes_group.addButton(yes)
		clothes_box.addWidget(no)
		clothes_group.addButton(no)
		self.v_layout.addLayout(clothes_box)

		roomate_pref_box = QHBoxLayout()
		roomate_pref_label = QLabel("(Optional) Camper's Roomate Preference (as an ID) : #")
		roomate_pref = QLineEdit()
		roomate_pref_box.addWidget(roomate_pref_label)
		roomate_pref_box.addWidget(roomate_pref)
		self.v_layout.addLayout(roomate_pref_box)

		roomate_avoid_box = QHBoxLayout()
		roomate_avoid_label = QLabel("(Optional) Enter a Camper that the Camper wants to avoid being roomates with. (as an ID) : #")
		roomate_avoid = QLineEdit()
		roomate_avoid_box.addWidget(roomate_avoid_label)
		roomate_avoid_box.addWidget(roomate_avoid)
		self.v_layout.addLayout(roomate_avoid_box)

		band_pref_box = QHBoxLayout()
		band_pref_label = QLabel("(Optional) Camper's Band Mate Preference (as an ID) : #")
		band_pref = QLineEdit()
		band_pref_box.addWidget(band_pref_label)
		band_pref_box.addWidget(band_pref)
		self.v_layout.addLayout(band_pref_box)

		band_avoid_box = QHBoxLayout()
		band_avoid_label = QLabel("(Optional) Enter a Camper the Camper does not want to be Band Mates with. (as an ID) : #")
		band_avoid = QLineEdit()
		band_avoid_box.addWidget(band_avoid_label)
		band_avoid_box.addWidget(band_avoid)
		self.v_layout.addLayout(band_avoid_box)

		preferences = [roomate_pref, roomate_avoid, band_pref, band_avoid]

		submit_btn = QPushButton("Check-In")
		self.v_layout.addWidget(submit_btn)

		submit_btn.clicked.connect(lambda: self.check_in_btn_clk(camper_id, equip_group, clothes_group, preferences))
	

	def check_in_btn_clk(self, camper_id, equip_group, clothes_group, preferences):
		equip_text = equip_group.checkedButton().text()
		clothes_text = clothes_group.checkedButton().text()

		# execute SQl search query 
		c, conn = create_db()
		c.execute("SELECT * FROM check_in WHERE camper_id = '"+ camper_id.text() + "'")
		r = c.fetchone()
		save_db_changes(conn)

		if(r):
			if(int(r[2])):
				self.check_in_ui()
				error_message = QLabel("ERROR: THIS CAMPER HAS ALREADY BEEN CHECKED IN.")
				self.v_layout.addWidget(error_message)
			else:
				
				if(int(r[3]) == 1 and int(r[4]) == 1 and int(r[5]) == 1 and int(r[6]) == 1 and equip_text == "Yes" and clothes_text == "Yes" ):
					
					camper_id_text = camper_id.text()
					c, conn = create_db()
					t = (1, camper_id_text)
					c.execute("UPDATE check_in SET has_checked_in = ? WHERE camper_id= ?", t)

					pref_names = ["roommate_pref", "roommate_avoid", "band_member_pref", "band_member_avoid"]
					for i in range(len(preferences)):
						if len(preferences[i].text()) == 0: pref = "None"
						else: pref = preferences[i].text()
						t = (pref, camper_id_text)
						c.execute("UPDATE check_in SET " +pref_names[i]+" = ? WHERE camper_id= ?", t)

					save_db_changes(conn)

					# Assign Dorm to Camper
					dorm_assignment_driver(camper_id_text, preferences)

					# Assign Band to Camper
					band_assignment_driver(camper_id_text, preferences)

					# Assign 2nd Band to Camper
					sec_band_assignment_driver(camper_id_text, preferences)


					self.check_in_ui()
					self.v_layout.addWidget(QLabel("**CONGRATULATIONS! CAMPER ID: " + camper_id_text+ " HAS BEEN OFFICIALLY CHECKED-IN."))
				
				else:
					self.check_in_ui()
					error_message = QLabel("ERROR: THIS CAMPER HAS NOT TURN IN ALL NECESSARY FORMS \nAND/OR DOES NOT HAVE THE NECESSARY SUPPLIES, AND COULD NOT BE CHECKED-IN.")
					self.v_layout.addWidget(error_message)

		else:
			self.check_in_ui()
			error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
			self.v_layout.addWidget(error_message)


		




	def check_in_search_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Welcome to the Camper Search Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		camper_id_box = QHBoxLayout()
		camper_id_label = QLabel("Please Enter Camper's ID: ")
		camper_id = QLineEdit()
		search_btn = QPushButton("Search")
		camper_id_box.addWidget(camper_id_label)
		camper_id_box.addWidget(camper_id)
		camper_id_box.addWidget(search_btn)
		self.v_layout.addLayout(camper_id_box)

		search_btn.clicked.connect(lambda: self.check_in_search_btn_clk(camper_id))

	def check_in_search_btn_clk(self, camper_id):
		#SQL SELECT statement 
		c, conn = create_db()
		c.execute("SELECT * FROM check_in WHERE camper_id = '"+ camper_id.text() + "'")
		r = c.fetchone()

		if(r):
			self.check_in_search_ui()
			self.v_layout.addWidget(QLabel("- Camper ID : " + r[0]))
			self.v_layout.addWidget(QLabel("- Camper Proposed Camp Session Date :  " + r[1]))
			if (r[2]): self.v_layout.addWidget(QLabel("- Has Camper Checked-In :  Yes"))
			else: self.v_layout.addWidget(QLabel("- Has Camper Checked-In :  No"))
			if (r[3]): self.v_layout.addWidget(QLabel("- Do We Have Camper's Application?  :  Yes"))
			else: self.v_layout.addWidget(QLabel("- Do We Have Camper's Application?  :  No"))
			if (r[4]): self.v_layout.addWidget(QLabel("- Do We Have Camper's Emergency Contact Form?  :  Yes"))
			else: self.v_layout.addWidget(QLabel("- Do We Have Camper's Emergency Contact Form?  :  No"))
			if (r[5]): self.v_layout.addWidget(QLabel("- Do We Have Camper's Legal Form?  :  Yes"))
			else: self.v_layout.addWidget(QLabel("- Do We Have Camper's Legal Form?  :  No"))
			if (r[6]): self.v_layout.addWidget(QLabel("- Do We Have Camper's Medical Form?  :  Yes"))
			else: self.v_layout.addWidget(QLabel("- Do We Have Camper's Medical Form?  :  No"))

			#r[9] = rank 
			c.execute("SELECT * FROM application WHERE camper_id = '"+ camper_id.text() + "'")
			q = c.fetchone()

			self.v_layout.addWidget(QLabel("\nCamper Information: "))
			self.v_layout.addWidget(QLabel("- Camper's Name : " + q[1]+ " "+ q[2]))
			self.v_layout.addWidget(QLabel("- Camper's Gender : " + q[4]))
			self.v_layout.addWidget(QLabel("- Camper's Age : " + str(q[5])))
			self.v_layout.addWidget(QLabel("- Camper's Band Role : " + q[6]))
			self.v_layout.addWidget(QLabel("- Camper's Rank : " + r[9]))
			self.v_layout.addWidget(QLabel("- Camper's Preferred Roomate's ID : #" + r[10]))
			self.v_layout.addWidget(QLabel("- Does NOT want this Camper as Roomate : #" + r[11]))
			self.v_layout.addWidget(QLabel("- Camper's Preferred Band Mate's ID : #" + r[12]))
			self.v_layout.addWidget(QLabel("- Does NOT want this Camper as a Band Mate : #" + r[13]))

			c.execute("SELECT dorm_number FROM dorm WHERE camper_id = '"+ camper_id.text() + "'")
			q = c.fetchone()
			if (q): self.v_layout.addWidget(QLabel("\n- Assigned Dorm Room  :  "+q[0]))
			else: self.v_layout.addWidget(QLabel("\n- Assigned Dorm Room  :  TBD"))

			c.execute("SELECT band FROM band WHERE camper_id = '"+ camper_id.text() + "'")
			q = c.fetchone()
			if (q): self.v_layout.addWidget(QLabel("- Assigned 1st Band  :  "+q[0]))
			else: self.v_layout.addWidget(QLabel("- Assigned 1st Band  :  TBD"))

			c.execute("SELECT band FROM second_band WHERE camper_id = '"+ camper_id.text() + "'")
			q = c.fetchone()
			if (q): self.v_layout.addWidget(QLabel("- Assigned 2nd Band  :  "+q[0]))
			else: self.v_layout.addWidget(QLabel("- Assigned 2nd Band  :  TBD"))


		else:
			self.check_in_search_ui()
			error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
			self.v_layout.addWidget(error_message)

		save_db_changes(conn)



	def legal_form_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Welcome to the Legal Information Form Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		camper_id_box = QHBoxLayout()
		camper_id_label = QLabel("Please Enter Camper's ID: ")
		camper_id = QLineEdit()
		camper_id_box.addWidget(camper_id_label)
		camper_id_box.addWidget(camper_id)
		self.v_layout.addLayout(camper_id_box)

		par_first_name_box = QHBoxLayout()
		par_first_name_label = QLabel("Please Enter the Camper's Gaurdian/Parent First Name: ")
		par_first_name = QLineEdit()
		par_first_name_box.addWidget(par_first_name_label)
		par_first_name_box.addWidget(par_first_name)
		self.v_layout.addLayout(par_first_name_box)

		par_last_name_box = QHBoxLayout()
		par_last_name_label = QLabel("Please Enter the Camper's Gaurdian/Parent Last Name: ")
		par_last_name = QLineEdit()
		par_last_name_box.addWidget(par_last_name_label)
		par_last_name_box.addWidget(par_last_name)
		self.v_layout.addLayout(par_last_name_box)

		par_age_box = QHBoxLayout()
		par_age_label = QLabel("Please Enter the Camper's Gaurdian/Parent Age: ")
		par_age = QLineEdit()
		par_age_box.addWidget(par_age_label)
		par_age_box.addWidget(par_age)
		self.v_layout.addLayout(par_age_box)

		is_par_box = QHBoxLayout()
		is_par_label = QLabel("Is this person the Camper's Parents (Yes or No): ")
		is_par = QLineEdit()
		is_par_box.addWidget(is_par_label)
		is_par_box.addWidget(is_par)
		self.v_layout.addLayout(is_par_box)

		

		submit_btn = QPushButton("Submit")
		self.v_layout.addWidget(submit_btn)
		
		submit_btn.clicked.connect(lambda: self.legal_form_btn_clk(camper_id, par_first_name, par_last_name, par_age, is_par))


	def legal_form_btn_clk(self, camper_id, par_first_name, par_last_name, par_age, is_par):

		# execute SQl search query 
		c, conn = create_db()
		c.execute("SELECT legal_form FROM check_in WHERE camper_id = '"+ camper_id.text() + "'")
		r = c.fetchone()

		if(r):
			has_legal = r[0]

			if(has_legal):
				self.legal_form_ui()
				error_message = QLabel("ERROR: ENTERED 'CAMPER ID' HAS ALREADY SUBMITTED THE LEGAL FORM.")
				self.v_layout.addWidget(error_message)
			else:
				# insert values into medical table
				t = (camper_id.text(), par_first_name.text(), par_last_name.text(), par_age.text(), is_par.text())
				c.execute("INSERT INTO legal VALUES (?,?,?,?,?)", t)

				# update values of check_in table 
				t = (1, camper_id.text())
				c.execute("UPDATE check_in SET legal_form = ? WHERE camper_id= ?", t)

				self.legal_form_ui()
				self.v_layout.addWidget(QLabel("**Legal Form Submitted."))

		else:
			self.legal_form_ui()
			error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
			self.v_layout.addWidget(error_message)

		save_db_changes(conn)

	def medical_form_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Welcome to the Medical Form Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		camper_id_box = QHBoxLayout()
		camper_id_label = QLabel("Please Enter Camper's ID: ")
		camper_id = QLineEdit()
		camper_id_box.addWidget(camper_id_label)
		camper_id_box.addWidget(camper_id)
		self.v_layout.addLayout(camper_id_box)

		med_insurance_name_box = QHBoxLayout()
		med_insurance_name_label = QLabel("Please Enter the Camper's Medical Insurance: ")
		med_insurance_name = QLineEdit()
		med_insurance_name_box.addWidget(med_insurance_name_label)
		med_insurance_name_box.addWidget(med_insurance_name)
		self.v_layout.addLayout(med_insurance_name_box)

		doctor_name_box = QHBoxLayout()
		doctor_name_label = QLabel("Please Enter the Camper's Doctor's Name: ")
		doctor_name = QLineEdit()
		doctor_name_box.addWidget(doctor_name_label)
		doctor_name_box.addWidget(doctor_name)
		self.v_layout.addLayout(doctor_name_box)

		dentist_box = QHBoxLayout()
		dentist_label = QLabel("Please Enter the Camper's Dentist's Name: ")
		dentist = QLineEdit()
		dentist_box.addWidget(dentist_label)
		dentist_box.addWidget(dentist)
		self.v_layout.addLayout(dentist_box)

		allergies_box = QHBoxLayout()
		allergies_label = QLabel("Please List any Allergies that the Camper has: ")
		allergies = QLineEdit()
		allergies_box.addWidget(allergies_label)
		allergies_box.addWidget(allergies)
		self.v_layout.addLayout(allergies_box)

		medications_box = QHBoxLayout()
		medications_label = QLabel("Please Enter any Medications that the Camper is taking: ")
		medications = QLineEdit()
		medications_box.addWidget(medications_label)
		medications_box.addWidget(medications)
		self.v_layout.addLayout(medications_box)


		submit_btn = QPushButton("Submit")
		self.v_layout.addWidget(submit_btn)
		
		submit_btn.clicked.connect(lambda: self.medical_form_btn_clk(camper_id, med_insurance_name, doctor_name, dentist, allergies, medications))


	def medical_form_btn_clk(self, camper_id, med_insurance_name, doctor_name, dentist, allergies, medications):

		# execute SQl search query 
		c, conn = create_db()
		c.execute("SELECT medical_form FROM check_in WHERE camper_id = '"+ camper_id.text() + "'")
		r = c.fetchone()

		if(r):
			has_med = r[0]

			if(has_med):
				self.medical_form_ui()
				error_message = QLabel("ERROR: ENTERED 'CAMPER ID' HAS ALREADY SUBMITTED THE MEDICAL FORM.")
				self.v_layout.addWidget(error_message)
			else:
				# insert values into medical table
				t = (camper_id.text(), med_insurance_name.text(), doctor_name.text(), dentist.text(), allergies.text(), medications.text())
				c.execute("INSERT INTO medical VALUES (?,?,?,?,?,?)", t)

				# update values of check_in table 
				t = (1, camper_id.text())
				c.execute("UPDATE check_in SET medical_form = ? WHERE camper_id= ?", t)

				self.medical_form_ui()
				self.v_layout.addWidget(QLabel("**Medical Form Submitted."))

		else:
			self.medical_form_ui()
			error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
			self.v_layout.addWidget(error_message)

		save_db_changes(conn)


	def emergency_form_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Welcome to the Emergency Contact Form Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		camper_id_box = QHBoxLayout()
		camper_id_label = QLabel("Please Enter Camper's ID: ")
		camper_id = QLineEdit()
		camper_id_box.addWidget(camper_id_label)
		camper_id_box.addWidget(camper_id)
		self.v_layout.addLayout(camper_id_box)

		emerg_first_name_box = QHBoxLayout()
		emerg_first_name_label = QLabel("Please Enter the First Name of Camper's Emergency Contact: ")
		emerg_first_name = QLineEdit()
		emerg_first_name_box.addWidget(emerg_first_name_label)
		emerg_first_name_box.addWidget(emerg_first_name)
		self.v_layout.addLayout(emerg_first_name_box)

		emerg_last_name_box = QHBoxLayout()
		emerg_last_name_label = QLabel("Please Enter the Last Name of Camper's Emergency Contact: ")
		emerg_last_name = QLineEdit()
		emerg_last_name_box.addWidget(emerg_last_name_label)
		emerg_last_name_box.addWidget(emerg_last_name)
		self.v_layout.addLayout(emerg_last_name_box)

		emerg_phone_num_box = QHBoxLayout()
		emerg_phone_num_label = QLabel("Please Enter the Phone Number of Camper's Emergency Contact: ")
		emerg_phone_num = QLineEdit()
		emerg_phone_num_box.addWidget(emerg_phone_num_label)
		emerg_phone_num_box.addWidget(emerg_phone_num)
		self.v_layout.addLayout(emerg_phone_num_box)


		submit_btn = QPushButton("Submit")
		self.v_layout.addWidget(submit_btn)
		
		submit_btn.clicked.connect(lambda: self.emerg_form_btn_clk(camper_id, emerg_first_name, emerg_last_name, emerg_phone_num))


	def emerg_form_btn_clk(self, camper_id, emerg_first_name, emerg_last_name, emerg_phone_num):

		# execute SQl search query 
		c, conn = create_db()
		c.execute("SELECT emergency_contact_form FROM check_in WHERE camper_id = '"+ camper_id.text() + "'")
		r = c.fetchone()

		if(r):
			has_em = r[0]
			if(has_em):
				self.emergency_form_ui()
				error_message = QLabel("ERROR: ENTERED 'CAMPER ID' HAS ALREADY SUBMITTED THE EMERGENCY CONTACT FORM.")
				self.v_layout.addWidget(error_message)
			else:
				# insert values into emergency_contact table
				t = (camper_id.text(),emerg_first_name.text(), emerg_last_name.text(), emerg_phone_num.text())
				c.execute("INSERT INTO emergency_contact VALUES (?,?,?,?)", t)

				# update values of check_in table 
				t = (1, camper_id.text())
				c.execute("UPDATE check_in SET emergency_contact_form = ? WHERE camper_id= ?", t)

				self.emergency_form_ui()
				self.v_layout.addWidget(QLabel("**Emergency Form Submitted."))

		else:
			self.emergency_form_ui()
			error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
			self.v_layout.addWidget(error_message)

		save_db_changes(conn)




	def make_decision_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Welcome to the Application Decision Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		decision_search_box = QHBoxLayout()
		decision_search_label = QLabel("Please Enter Camper's ID: ")
		camper_id_search = QLineEdit()
		decision_group = QButtonGroup()
		accept = QRadioButton("Accept Camper")
		reject = QRadioButton("Reject Camper")
		accept.setChecked(True) 
		select_btn = QPushButton("Select")

		decision_search_box.addWidget(decision_search_label)
		decision_search_box.addWidget(camper_id_search)
		decision_search_box.addWidget(accept)
		decision_group.addButton(accept)
		decision_search_box.addWidget(reject)
		decision_group.addButton(reject)
		decision_search_box.addWidget(select_btn)

		self.v_layout.addLayout(decision_search_box)

		select_btn.clicked.connect(lambda: self.decision_btn_clk(camper_id_search, decision_group))



	def decision_btn_clk(self, camper_id_search, decision_group):
		ready_for_db = 0 

		if (len(camper_id_search.text()) == 0 or camper_id_search.text() == "Please Enter a Valid ID"):
			camper_id_search.setText("Please Enter a Valid ID")
			ready_for_db = 0 

		else:
			c, conn = create_db()
			c.execute("SELECT email, status, camp_dates, band_role, gender FROM application WHERE camper_id = '"+ camper_id_search.text() + "'")
			r = c.fetchone()

			if(r):
				email = r[0]
				status = r[1]
				date = r[2]
				band_role = r[3]
				gender = r[4]

				if status == 'TBD':
					decision = decision_group.checkedButton().text()
					camper_id_text = camper_id_search.text()
					rank_group = None

					if decision == "Accept Camper":
						self.make_decision_ui()
						self.v_layout.addWidget(QLabel("CAMPER ID: " + camper_id_text + " WILL BE ACCEPTED TO FUTURE ROCK STARS CAMP\n"))
						
						#Give the Camper a Rank 
						rank_box = QHBoxLayout()
						band_role_label = QLabel("**NOTE: Camper's Band Role is: '"+ band_role+"' and Gender is: '"+gender+"'")
						rank_label = QLabel("Camper's Rank (1 = 'Most Talented') : ")
						rank_group = QButtonGroup(self)
						none_rk = QRadioButton("None")
						none_rk.setChecked(True) 
						one = QRadioButton("1")
						two = QRadioButton("2")
						three = QRadioButton("3")
						four = QRadioButton("4")
						arr = [none_rk, one, two, three, four]
						self.v_layout.addWidget(band_role_label)
						rank_box.addWidget(rank_label)
						for i in arr:
							rank_group.addButton(i)
							rank_box.addWidget(i)
						self.v_layout.addLayout(rank_box)


						self.v_layout.addWidget(QLabel("\n**Enter additional comments here to be mailed to: " + email))
						comments = QTextEdit("Congratulations, you have been selected to be a Camper at Future Rock Stars Camp.")
						self.v_layout.addWidget(comments)



					else:
						self.make_decision_ui()
						self.v_layout.addWidget(QLabel("**CAMPER ID: " + camper_id_text + " WILL BE REJECTED TO FUTURE ROCK STARS CAMP"))
						self.v_layout.addWidget(QLabel("\n**Enter additional comments here to be mailed to: " + email))
						comments = QTextEdit("Thank You for applying, but the selection was a highly competitve process and you didn't quite make the cut. Learning how to accept rejection is an important skill for an aspiring rocker.")
						self.v_layout.addWidget(comments)

					send_decision_btn = QPushButton("Send Decision")
					self.v_layout.addWidget(send_decision_btn)

					if(rank_group):
						send_decision_btn.clicked.connect(lambda: self.send_decision_btn_clk(camper_id_text, decision, gender, date, band_role, rank_group))	
					else:
						send_decision_btn.clicked.connect(lambda: self.send_decision_btn_clk(camper_id_text, decision, gender, date, band_role, None))

				else:
					self.make_decision_ui()
					error_message = QLabel("ERROR: CAMPER ID: "+camper_id_search.text()+" HAS ALREADY BEEN REVIEWED.")
					self.v_layout.addWidget(error_message)
			else:
				self.make_decision_ui()
				error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
				self.v_layout.addWidget(error_message)

			save_db_changes(conn)


	def send_decision_btn_clk(self, camper_id_text, decision, gender, date, band_role, rank_group):
		
		c, conn = create_db()

		if decision == "Accept Camper": 
			desc = "A"
			rank = rank_group.checkedButton().text()

			if rank != 'None':
				t = (rank, date, gender, band_role)
				c.execute("SELECT * FROM check_in AS c, application AS a WHERE c.camper_id = a.camper_id AND c.rank = ? AND c.check_in_date  = ? AND a.gender = ? AND a.band_role = ?", t)
				r = c.fetchone()
				if (r):
					self.v_layout.addWidget(QLabel("*Error: There is already a Camper with Rank: " +rank+" who is a '"+gender+"' and a '"+band_role+"'.\n*Please try a different Ranking." ))
				else:
					# put accepted camper into check-in table 
					t = (camper_id_text,date,0,1,0,0,0,0,0,rank,"N/A","N/A","N/A","N/A")
					c.execute("INSERT INTO check_in VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", t)
					t = (desc, camper_id_text)
					c.execute("UPDATE application SET status = ? WHERE camper_id= ?", t)
					save_db_changes(conn)
					self.make_decision_ui()
					self.v_layout.addWidget(QLabel("**NOTE: Decision has been sent for Camper ID: " + camper_id_text))
			else:
				# put accepted camper into check-in table 
				t = (camper_id_text,date,0,1,0,0,0,0,0,rank,"N/A","N/A","N/A","N/A")
				c.execute("INSERT INTO check_in VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", t)
				t = (desc, camper_id_text)
				c.execute("UPDATE application SET status = ? WHERE camper_id= ?", t)
				save_db_changes(conn)
				self.make_decision_ui()
				self.v_layout.addWidget(QLabel("**NOTE: Decision has been sent for Camper ID: " + camper_id_text))


		else: 
			desc = "R"
			t = (desc, camper_id_text)
			c.execute("UPDATE application SET status = ? WHERE camper_id= ?", t)
			save_db_changes(conn)
			self.make_decision_ui()
			self.v_layout.addWidget(QLabel("**NOTE: Decision has been sent for Camper ID: " + camper_id_text))

		



	def search_app_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Welcome to the Application Search Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		app_search_box = QHBoxLayout()
		app_search_label = QLabel("Please Enter Camper's ID: ")
		camper_id_search = QLineEdit()
		app_search_box.addWidget(app_search_label)
		app_search_box.addWidget(camper_id_search)
		search_btn = QPushButton("Search")
		app_search_box.addWidget(search_btn)
		self.v_layout.addLayout(app_search_box)

		search_btn.clicked.connect( lambda: self.search_btn_clk(camper_id_search) )


	def search_btn_clk(self, camper_id_search):
		ready_for_db = 0 
		if (len(camper_id_search.text()) == 0 or camper_id_search.text() == "Please Enter a Valid ID"):
			camper_id_search.setText("Please Enter a Valid ID")
			ready_for_db = 0  
		else:
			#SQL SELECT statement 
			c, conn = create_db()
			c.execute("SELECT * FROM application WHERE camper_id = '"+ camper_id_search.text() + "'")
			r = c.fetchone()

			if (r):
				self.search_app_ui()
				self.v_layout.addWidget(QLabel(" - Camper ID : " + r[0]))
				self.v_layout.addWidget(QLabel(" - Camper Name : " + r[1] + " " + r[2]))
				self.v_layout.addWidget(QLabel(" - Camper Address : " + r[3]))
				self.v_layout.addWidget(QLabel(" - Camper Age : " + str(r[5])))
				self.v_layout.addWidget(QLabel(" - Camper Gender : " + r[4]))
				self.v_layout.addWidget(QLabel(" - Camper's Proposed Band Role : " + r[6]))
				self.v_layout.addWidget(QLabel(" - Camper Email : " + r[7]))
				self.v_layout.addWidget(QLabel(" - Camper's Intented Camp Session : " + r[8] + "\n"))

				if r[9] == "R" or r[9] == "r":
					self.v_layout.addWidget(QLabel(" - Camper Application Status : REJECTED"))
				elif r[9] == "A" or r[9] == "a":
					self.v_layout.addWidget(QLabel(" - Camper Application Status : ACCEPTED"))
				else:
					self.v_layout.addWidget(QLabel(" - Camper Application Status : " + r[9]))

				self.v_layout.addWidget(QLabel(" - Camper's Deposit Has Cleared : " + r[10]))

			else:
				self.search_app_ui()
				error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
				self.v_layout.addWidget(error_message)

			save_db_changes(conn)


	def process_payment_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Payment Processing Update Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		app_search_box = QHBoxLayout()
		app_search_label = QLabel("Please Enter Camper's ID: ")
		camper_id_search = QLineEdit()
		app_search_box.addWidget(app_search_label)
		app_search_box.addWidget(camper_id_search)
		search_btn = QPushButton("Select")
		app_search_box.addWidget(search_btn)
		self.v_layout.addLayout(app_search_box)

		search_btn.clicked.connect( lambda: self.payment_btn_clk(camper_id_search) )

	def payment_btn_clk(self, camper_id_search):

		# execute SQl search query 
		c, conn = create_db()
		c.execute("SELECT payment, email FROM application WHERE camper_id = '"+ camper_id_search.text() + "'")
		camper_id_search_text = camper_id_search.text()
		r = c.fetchone()

		if(r):
			self.process_payment_ui()
			payment_status = r[0]
			email = r[1]

			if payment_status == 'TBD':
				pay_box = QHBoxLayout()
				payment_group = QButtonGroup(self)
				pay_label = QLabel("Has the Camper's Desposit Cleared? : ")
				yes = QRadioButton("Yes")
				no = QRadioButton("No")
				yes.setChecked(True) 
				submit_btn = QPushButton("Submit")
				pay_box.addWidget(pay_label)
				pay_box.addWidget(yes)
				payment_group.addButton(yes)
				pay_box.addWidget(no)
				payment_group.addButton(no)
				pay_box.addWidget(submit_btn)
				self.v_layout.addLayout(pay_box)

				warning_label = QLabel("**Warning: Selecting 'No' Results in an Automatic Rejection")
				self.v_layout.addWidget(warning_label)

				#payment_success = payment_group.checkedButton().text()
				
				submit_btn.clicked.connect( lambda: self.payment_btn_clk_2(camper_id_search_text, payment_group))

			else:
				error_message = QLabel("PAYMENT STATUS HAS ALREADY BEEN UPDATED FOR THIS CAMPER.")
				self.v_layout.addWidget(error_message)

		else:
			self.process_payment_ui()
			error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
			self.v_layout.addWidget(error_message)

		save_db_changes(conn)

	def payment_btn_clk_2(self, camper_id_search_text, payment_group):
		payment_success = payment_group.checkedButton().text()
		t = (payment_success, camper_id_search_text)
		c, conn = create_db()
		c.execute("UPDATE application SET payment = ? WHERE camper_id= ?", t)
		self.process_payment_ui()
		if payment_success == "No":
			self.v_layout.addWidget(QLabel("NOTE: CAMPER ID: " + camper_id_search_text+ " HAS BEEN REJECTED.\n(A REJECTION EMAIL HAS BEEN SENT)"))
			t = ("R", camper_id_search_text)
			c.execute("UPDATE application SET status = ? WHERE camper_id= ?", t)
		else:
			self.v_layout.addWidget(QLabel("Payment Process Successful."))


		save_db_changes(conn)


	def new_app_ui(self):
		
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Welcome to the Application Form Page")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)
			

		app_label = QLabel("Please Fill Out the Application Form:")
		self.v_layout.addWidget(app_label)

		camper_id_box = QHBoxLayout()
		camper_id_label = QLabel("Camper ID : #")
		camper_id = QLineEdit()
		camper_id_box.addWidget(camper_id_label)
		camper_id_box.addWidget(camper_id)
		self.v_layout.addLayout(camper_id_box)

		first_name_box = QHBoxLayout()
		first_name_label = QLabel("Camper First Name : ")
		first_name = QLineEdit()
		first_name_box.addWidget(first_name_label)
		first_name_box.addWidget(first_name)
		self.v_layout.addLayout(first_name_box)

		last_name_box = QHBoxLayout()
		last_name_label = QLabel("Camper Last Name : ")
		last_name = QLineEdit()
		last_name_box.addWidget(last_name_label)
		last_name_box.addWidget(last_name)
		self.v_layout.addLayout(last_name_box)

		address_box = QHBoxLayout()
		address_label = QLabel("Camper Address : ")
		address = QLineEdit()
		address_box.addWidget(address_label)
		address_box.addWidget(address)
		self.v_layout.addLayout(address_box)

		gender_box = QHBoxLayout()
		gender_label = QLabel("Camper Gender : ")
		male = QRadioButton("Male")
		female = QRadioButton("Female")
		male.setChecked(True) 
		gender_box.addWidget(gender_label)
		gender_box.addWidget(male)
		gender_box.addWidget(female)
		self.v_layout.addLayout(gender_box)

		age_box = QHBoxLayout()
		age_label = QLabel("Camper Age : ")
		age_text = QLineEdit("15")
		slider = QSlider(QtCore.Qt.Horizontal)
		slider.setMinimum(13)
		slider.setMaximum(18)
		slider.setValue(15)
		slider.setTickInterval(1)
		slider.setTickPosition(QSlider.TicksBelow)
		age_box.addWidget(age_label)
		age_box.addWidget(age_text)
		age_box.addWidget(slider)
		self.v_layout.addLayout(age_box)
		slider.valueChanged.connect( lambda: self.v_change(slider, age_text) )

		band_role_box = QHBoxLayout()
		band_role_label = QLabel("Camper's Intended Band Role : ")
		band_role_group = QButtonGroup(self)
		#Band Roles: 'Singer', 'Guitarist', 'Drummer', 'Bassist', 'Keyboardist' and 'Instrumentalist
		singer = QRadioButton("Singer")
		singer.setChecked(True) 
		guitarist = QRadioButton("Guitarist")
		drummer = QRadioButton("Drummer") 
		bassist = QRadioButton("Bassist") 
		keyboardist = QRadioButton("Keyboardist") 
		instrumentalist = QRadioButton("Instrumentalist") 
		arr = [singer, guitarist, drummer, bassist, keyboardist, instrumentalist]
		band_role_box.addWidget(band_role_label)
		for i in arr:
			band_role_group.addButton(i)
			band_role_box.addWidget(i)

		self.v_layout.addLayout(band_role_box)

		email_box = QHBoxLayout()
		email_label = QLabel("Camper's Email : ")
		email = QLineEdit()
		email_box.addWidget(email_label)
		email_box.addWidget(email)
		self.v_layout.addLayout(email_box)

		camp_date_box = QHBoxLayout()
		camp_date_label = QLabel("Camper's Intended Camp Session : ")
		camp_date_group = QButtonGroup(self)
		june = QRadioButton("June")
		june.setChecked(True) 
		july = QRadioButton("July")
		august = QRadioButton("August")
		arr = [june, july, august]
		camp_date_box.addWidget(camp_date_label)
		for i in arr:
			camp_date_group.addButton(i)
			camp_date_box.addWidget(i)
		self.v_layout.addLayout(camp_date_box)

		


		btn1 = QPushButton("Submit")
		self.v_layout.addWidget(btn1)

		app_arr = [camper_id, first_name, last_name, address, age_text, email ]

		btn1.clicked.connect( lambda: self.app_btn_clk(app_arr, male.isChecked(), band_role_group, camp_date_group))

	# Function called when the 'slider' for the 'age' application parameter is changed
	def v_change(self, slider, text_box):
		my_age_value = str(slider.value()) 
		text_box.setText(my_age_value)

	# Function is called when the button on the applications page is pressed 
	def app_btn_clk(self, app_arr, male_checked, band_role_group, camp_date_group):

		ready_for_db = 1 

		for i in app_arr:
			if (len(i.text()) == 0 or i.text() == "*Error: Required Field"):
				i.setText("*Error: Required Field")
				ready_for_db = 0

		if male_checked: gender = "Male"
		else: gender = "Female"
		
		
		band_role = band_role_group.checkedButton().text()
		camp_date = camp_date_group.checkedButton().text()
		
		"""
		band_pref = band_pref_group.checkedButton().text()
		if len(roomate_pref.text()) == 0: pref_roomate = "None"
		else: pref_roomate = roomate_pref.text()
		"""

		if(ready_for_db):
			#SQL INSERT statement 

			c, conn = create_db()
			t = (app_arr[0].text(), app_arr[1].text(), app_arr[2].text(), app_arr[3].text(), gender, app_arr[4].text(), band_role, app_arr[5].text(), camp_date, 'TBD', 'TBD')
			try:
				c.execute("INSERT INTO application VALUES (?,?,?,?,?,?,?,?,?,?,?)", t)
			except sqlite3.IntegrityError:
				app_arr[0].setText("****Error: Camper ID Already Exists*****")
				ready_for_db = 0 
			
			save_db_changes(conn)

			if (ready_for_db):
				self.clearLayout(self.v_layout)
				welcome_label = QLabel("Application Submitted.\n\nTo enter another application: 'Control+N'\n or go to:\n 'Handle Applications' > 'New'")
				welcome_label.setStyleSheet("font: 30pt Century Gothic; text-align: center; color: #232322")
				welcome_label.setAlignment(QtCore.Qt.AlignCenter)
				self.v_layout.addWidget(welcome_label)

	
	def band_ranking_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Claremont Has Talent!")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		self.v_layout.addWidget(QLabel("\nBand 1: The bank ranked best for the summer (each camp has eight bands) in terms of talent"))
		self.v_layout.addWidget(QLabel("Band 2: The all-girl band ranked best for the summer"))	
		self.v_layout.addWidget(QLabel("Band 3: The all-boy band ranked best for the summer"))	
		self.v_layout.addWidget(QLabel("Band 4: A band formed with the most talented campers in each category, for the summer"))						

		self.v_layout.addWidget(QLabel("\nCurrent Band Rankings: "))	
		
		if (os.path.exists("band_rankings.p")):
			bands = pickle.load(open("band_rankings.p", "rb"))	
		else:
			bands = ["TBD", "TBD", "TBD", "TBD"]

		for i in range(len(bands)):
			cnt = i+1
			self.v_layout.addWidget(QLabel(" - Band"+str(cnt)+": '"+bands[i]+"'"))


		best_band1_box = QHBoxLayout()
		best_band1_label = QLabel("Band1 choice : ")
		best_band1 = QLineEdit()
		best_band1_box.addWidget(best_band1_label)
		best_band1_box.addWidget(best_band1)
		self.v_layout.addLayout(best_band1_box)

		best_band2_box = QHBoxLayout()
		best_band2_label = QLabel("Band2 choice : ")
		best_band2 = QLineEdit()
		best_band2_box.addWidget(best_band2_label)
		best_band2_box.addWidget(best_band2)
		self.v_layout.addLayout(best_band2_box)

		best_band3_box = QHBoxLayout()
		best_band3_label = QLabel("Band3 choice : ")
		best_band3 = QLineEdit()
		best_band3_box.addWidget(best_band3_label)
		best_band3_box.addWidget(best_band3)
		self.v_layout.addLayout(best_band3_box)

		best_band4_box = QHBoxLayout()
		best_band4_label = QLabel("Band4 choice : ")
		best_band4 = QLineEdit()
		best_band4_box.addWidget(best_band4_label)
		best_band4_box.addWidget(best_band4)
		self.v_layout.addLayout(best_band4_box)

		btn1 = QPushButton("Submit")
		self.v_layout.addWidget(btn1)

		arr = [best_band1, best_band2, best_band3, best_band4]
		btn1.clicked.connect( lambda: self.band_btn_clk(arr, bands))



	def band_btn_clk(self, arr, bands):
		
		for i in range(len(arr)):
			if (arr[i].text() != ''):
				bands[i] = arr[i].text()

		pickle.dump( bands, open( "band_rankings.p", "wb" ) )

		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Talent Show Update Made.")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)



	def talent_show_ui(self):
		self.clearLayout(self.v_layout)
		welcome_label = QLabel("Claremont Has Talent!")
		welcome_label.setStyleSheet("font: 30pt Century Gothic; font-weight: bold; text-align: center; color: #232322")
		welcome_label.setAlignment(QtCore.Qt.AlignCenter)
		self.v_layout.addWidget(welcome_label)

		c, conn = create_db()

		categories = ["Singer", "Guitarist", "Drummer", "Bassist", "Keyboardist", "Instrumentalist"]
		
		for i in categories:
			lab = QLabel("Top "+i+":")
			lab.setStyleSheet("font-weight: bold;  color: #232322")
			self.v_layout.addWidget(lab)
			t = (i, "Male")
			c.execute("SELECT MAX(rank), A.camper_id, A.name_first, A.name_last FROM check_in C, application A WHERE C.camper_id = A.camper_id AND A.band_role = ? AND A.gender = ?", t) 
			r = c.fetchone()
			if (r and r[0] != None):
				self.v_layout.addWidget(QLabel("- Best Male: ID:"+r[1]+", Name: "+r[2]+" "+r[3]))
			else:
				self.v_layout.addWidget(QLabel("- Best Male: TBD"))
			
			t = (i, "Female")
			c.execute("SELECT MAX(rank), A.camper_id, A.name_first, A.name_last FROM check_in C, application A WHERE C.camper_id = A.camper_id AND A.band_role = ? AND A.gender = ?", t) 
			r = c.fetchone()
			if (r and r[0] != None):
				self.v_layout.addWidget(QLabel("- Best Female: ID:"+r[1]+", Name: "+r[2]+" "+r[3]))
			else:
				self.v_layout.addWidget(QLabel("- Best Female: TBD"))


	
	# Function clears the entire current layout/window  
	def clearLayout(self, layout):
		if layout is not None:
			while layout.count():
			    item = layout.takeAt(0)
			    widget = item.widget()
			    if widget is not None:
			    	widget.deleteLater()
			    else:
			        self.clearLayout(item.layout())

