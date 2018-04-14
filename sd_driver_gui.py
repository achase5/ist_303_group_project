import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QButtonGroup, QCheckBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout, QWidget)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenuBar, qApp, QLineEdit, QTextEdit)
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from sqlite_dbv3 import * 


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

		submit_btn = QPushButton("Check-In")
		self.v_layout.addWidget(submit_btn)

		submit_btn.clicked.connect(lambda: self.check_in_btn_clk(camper_id, equip_group, clothes_group))
	

	def check_in_btn_clk(self, camper_id, equip_group, clothes_group):
		equip_text = equip_group.checkedButton().text()
		clothes_text = clothes_group.checkedButton().text()

		# execute SQl search query 
		c, conn = create_db()
		c.execute("SELECT * FROM check_in WHERE camper_id = '"+ camper_id.text() + "'")
		r = c.fetchone()

		if(r):
			if(int(r[2])):
				self.check_in_ui()
				error_message = QLabel("ERROR: THIS CAMPER HAS ALREADY BEEN CHECKED IN.")
				self.v_layout.addWidget(error_message)
			else:
				
				if(int(r[3]) == 1 and int(r[4]) == 1 and int(r[5]) == 1 and int(r[6]) == 1 and equip_text == "Yes" and clothes_text == "Yes" ):
					camper_id_text = camper_id.text()
					t = (1, camper_id_text)
					c.execute("UPDATE check_in SET has_checked_in = ? WHERE camper_id= ?", t)
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

		save_db_changes(conn)




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
			c.execute("SELECT email, status, camp_dates FROM application WHERE camper_id = '"+ camper_id_search.text() + "'")
			r = c.fetchone()

			if(r):
				email = r[0]
				status = r[1]
				date = r[2]

				if status == 'TBD':
					decision = decision_group.checkedButton().text()
					camper_id_text = camper_id_search.text()

					if decision == "Accept Camper":
						self.make_decision_ui()
						self.v_layout.addWidget(QLabel("**CAMPER ID: " + camper_id_text + " WILL BE ACCEPTED TO FUTURE ROCK STARS CAMP"))
						self.v_layout.addWidget(QLabel("\n**Enter additional comments here to be mailed to: " + email))
						comments = QTextEdit("Congratulations, you have been selected to be a Camper at Future Rock Stars Camp.")
						self.v_layout.addWidget(comments)

						# put accepted camper into check-in table 
						t = (camper_id_text,date,0,1,0,0,0,0,0)
						c.execute("INSERT INTO check_in VALUES (?,?,?,?,?,?,?,?,?)", t)

					else:
						self.make_decision_ui()
						self.v_layout.addWidget(QLabel("**CAMPER ID: " + camper_id_text + " WILL BE REJECTED TO FUTURE ROCK STARS CAMP"))
						self.v_layout.addWidget(QLabel("\n**Enter additional comments here to be mailed to: " + email))
						comments = QTextEdit("Thank You for applying, but the selection was a highly competitve process and you didn't quite make the cut. Learning how to accept rejection is an important skill for an aspiring rocker.")
						self.v_layout.addWidget(comments)

					send_decision_btn = QPushButton("Send Decision")
					self.v_layout.addWidget(send_decision_btn)
					send_decision_btn.clicked.connect(lambda: self.send_decision_btn_clk(camper_id_text, decision))

				else:
					self.make_decision_ui()
					error_message = QLabel("ERROR: CAMPER ID: "+camper_id_search.text()+" HAS ALREADY BEEN REVIEWED.")
					self.v_layout.addWidget(error_message)
			else:
				self.make_decision_ui()
				error_message = QLabel("ERROR: ENTERED 'CAMPER ID' VALUE IS NOT IN THE DATABASE, PLEASE TRY AGAIN.")
				self.v_layout.addWidget(error_message)

			save_db_changes(conn)

	def send_decision_btn_clk(self, camper_id_text, decision):
		
		if decision == "Accept Camper": desc = "A"
		else: desc = "R"

		t = (desc, camper_id_text)
		c, conn = create_db()
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
				self.v_layout.addWidget(QLabel(" - Camper Roomate Preference : " + str(r[7])))
				self.v_layout.addWidget(QLabel(" - Camper Band Preference : " + r[8]))
				self.v_layout.addWidget(QLabel(" - Camper Email : " + r[9]))
				self.v_layout.addWidget(QLabel(" - Camper's Intented Camp Session : " + r[10] + "\n"))

				if r[11] == "R" or r[11] == "r":
					self.v_layout.addWidget(QLabel(" - Camper Application Status : REJECTED"))
				elif r[11] == "A" or r[11] == "a":
					self.v_layout.addWidget(QLabel(" - Camper Application Status : ACCEPTED"))
				else:
					self.v_layout.addWidget(QLabel(" - Camper Application Status : " + r[11]))

				self.v_layout.addWidget(QLabel(" - Camper's Deposit Has Cleared : " + r[12]))

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

		roomate_pref_box = QHBoxLayout()
		roomate_pref_label = QLabel("(Optional) Camper's Roomate Preference (as an ID) : #")
		roomate_pref = QLineEdit()
		roomate_pref_box.addWidget(roomate_pref_label)
		roomate_pref_box.addWidget(roomate_pref)
		self.v_layout.addLayout(roomate_pref_box)

		# Band Preference 
		band_pref_box = QHBoxLayout()
		band_pref_label = QLabel("(Optional) Camper's Band Preference (select 'None' if no preference) : ")
		band_pref_group = QButtonGroup(self)
		#Possible Bands: 'Band1', 'Band2', 'Band3', 'Band4', 'Band5', 'Band6', 'Band7' and 'Band8'
		none = QRadioButton("None")
		none.setChecked(True) 
		band1 = QRadioButton("Band1")
		band2 = QRadioButton("Band2")
		band3 = QRadioButton("Band3") 
		band4 = QRadioButton("Band4") 
		band5 = QRadioButton("Band5") 
		band6 = QRadioButton("Band6") 
		band7 = QRadioButton("Band7") 
		band8 = QRadioButton("Band8") 
		arr = [none, band1, band2, band3, band4, band5, band6, band7, band8]
		band_pref_box.addWidget(band_pref_label)
		for i in arr:
			band_pref_group.addButton(i)
			band_pref_box.addWidget(i)
		self.v_layout.addLayout(band_pref_box)


		btn1 = QPushButton("Submit")
		self.v_layout.addWidget(btn1)

		app_arr = [camper_id, first_name, last_name, address, age_text, email ]

		btn1.clicked.connect( lambda: self.app_btn_clk(app_arr, male.isChecked(), band_role_group, camp_date_group, band_pref_group, roomate_pref))

	# Function called when the 'slider' for the 'age' application parameter is changed
	def v_change(self, slider, text_box):
		my_age_value = str(slider.value()) 
		text_box.setText(my_age_value)

	# Function is called when the button on the applications page is pressed 
	def app_btn_clk(self, app_arr, male_checked, band_role_group, camp_date_group, band_pref_group, roomate_pref ):

		ready_for_db = 1 

		for i in app_arr:
			if (len(i.text()) == 0 or i.text() == "*Error: Required Field"):
				i.setText("*Error: Required Field")
				ready_for_db = 0

		if male_checked: gender = "Male"
		else: gender = "Female"
		
		
		band_role = band_role_group.checkedButton().text()
		camp_date = camp_date_group.checkedButton().text()
		band_pref = band_pref_group.checkedButton().text()
		if len(roomate_pref.text()) == 0: pref_roomate = "None"
		else: pref_roomate = roomate_pref.text()

		if(ready_for_db):
			#SQL INSERT statement 

			c, conn = create_db()
			t = (app_arr[0].text(),app_arr[1].text(), app_arr[2].text(), app_arr[3].text(), gender, app_arr[4].text(), band_role, pref_roomate, band_pref, app_arr[5].text(), camp_date, 'TBD', 'TBD')
			try:
				c.execute("INSERT INTO application VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", t)
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



class MenuBar(QMainWindow):

	def __init__(self):

		super().__init__()

		self.main_widget = Window()
		self.setCentralWidget(self.main_widget)

		self.init_ui()

	def init_ui(self):

		bar = self.menuBar()
		app_menu_btn1 = bar.addMenu('Handle Applications')
		app_menu_btn2 = bar.addMenu('Update Applications')
		app_menu_btn3 = bar.addMenu('Check-In Camper')
		app_menu_btn4 = bar.addMenu('Maintenance')

		new_action = QAction('New Application', self)
		new_action.setShortcut('Ctrl+N')
		app_menu_btn1.addAction(new_action)
		new_action.triggered.connect(self.create_new_app)

		search_action = QAction("Search Applicant", self)
		search_action.setShortcut('Ctrl+S')
		app_menu_btn1.addAction(search_action)
		search_action.triggered.connect(self.search_app)

		payment_action = QAction('Process Payment', self)
		payment_action.setShortcut('Ctrl+P')
		app_menu_btn2.addAction(payment_action)
		payment_action.triggered.connect(self.pay_app)

		decision_action = QAction('Make Decision', self)
		decision_action.setShortcut('Ctrl+D')
		app_menu_btn2.addAction(decision_action)
		decision_action.triggered.connect(self.make_decision_app)



		offical_check_in_action = QAction('Official Check-In', self)
		offical_check_in_action.setShortcut('Ctrl+O')
		app_menu_btn3.addAction(offical_check_in_action)
		offical_check_in_action.triggered.connect(self.check_in_app)

		check_in_search_action = QAction('Search Camper', self)
		check_in_search_action.setShortcut('Ctrl+X')
		app_menu_btn3.addAction(check_in_search_action)
		check_in_search_action.triggered.connect(self.check_in_search_app)

		emergency_form_action = QAction('Emergency Form', self)
		app_menu_btn3.addAction(emergency_form_action)
		emergency_form_action.triggered.connect(self.emerg_form_app)

		medical_form_action = QAction('Medical Form', self)
		app_menu_btn3.addAction(medical_form_action)
		medical_form_action.triggered.connect(self.med_form_app)

		legal_form_action = QAction('Legal Form', self)
		app_menu_btn3.addAction(legal_form_action)
		legal_form_action.triggered.connect(self.legal_form_app)

		maintenance_action = QAction('Enter Maintenance Mode', self)
		maintenance_action.setShortcut('Ctrl+M')
		app_menu_btn4.addAction(maintenance_action)
		maintenance_action.triggered.connect(self.maintenance_app)

		


		oImage = QImage("concert-png.jpg")
		sImage = oImage.scaled(QtCore.QSize(1000,700))                   
		palette = QPalette()
		palette.setBrush(10, QBrush(sImage))                     
		self.setPalette(palette)

		self.setWindowTitle("FRoST Registration System")
		self.resize(800, 495)

		self.show()


	def create_new_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 400, 150)
		self.main_widget.new_app_ui()

	def search_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.search_app_ui()

	def pay_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.process_payment_ui()

	def make_decision_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.make_decision_ui()

	def emerg_form_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.emergency_form_ui()

	def med_form_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.medical_form_ui()

	def legal_form_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.legal_form_ui()

	def check_in_search_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.check_in_search_ui()

	def check_in_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.check_in_ui()

	def maintenance_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.maintenance_mode_ui()


	


# Run the Application..
app = QApplication(sys.argv)
window = MenuBar()
sys.exit(app.exec_())

