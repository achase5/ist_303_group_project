from pyfiglet import figlet_format
from sd_dorm_assign import *
from sqlite_dbv3 import *
import getpass 
import os 


"""
Main Menu contents 

"""
def main():

	print()
	print(figlet_format('Future Rock Stars!', font='starwars'))
	
	print('##################################################################\n')

	print("WELECOME TO THE REGISTRATION NETWORK\n")
	print(" (1) Enter 'q' to Quit")
	print(" (2) Enter 'c' to Check-In a Camper")
	print(" (3) Enter 'm' to Make Application Decision, Mail Application Decision, or Update Camper Info")
	print(" (4) Enter 'a' to Enter a New Application, or View Existing Camper Applicant Info")
	print(" (5) Enter 'x' to Go Into Maintence Mode")
	
	print('##################################################################\n')
	print()



"""			
Menu Option to 'Handle Applications', which means that the client could enter a 'New' 
application and view the most recent status of any application 

"""
def handle_applications():

	loop = 1
	while (loop):
		print('\n')
		print('##################################################################\n')
		print ("******* WELCOME TO THE CAMPER APPLICATION PAGE ********\n")
		print(" (1) Type 'Back' to return to main menu")
		print(" (2) Type 'New' to Enter a new Application into the Database")
		print(" (3) Type 'Look' to View the Status & Info of an Applicant")
		print('\n')

		print('##################################################################\n')	

		user_in = input("Enter Command : ")
		print('\n')

		if (user_in == 'back' or user_in == 'Back' or user_in == 'BACK'):
			loop = 0

		if (user_in == 'new' or user_in == 'New' or user_in == 'NEW'):

			print('\n')
			app_id = input(" (1) Enter Camper's ID: ")
			app_first_name = input(" (2) Enter Camper's First Name: ")
			app_last_name = input(" (3) Enter Camper's Last Name: ")
			app_address = input(" (4) Enter Camper's Address: ")
			app_gender = input(" (5) Enter Camper's Gender: ")
			app_age = input(" (6) Enter Camper's Age: ")
			print("\n*** Possible Band Roles: 'Singer', 'Guitarist', 'Drummer', 'Bassist', 'Keyboardist' and 'Instrumentalist' *** ")
			app_band_role = input(" (7) Enter Camper's Intended Band Role: ")
			app_email = input(" (8) Enter Camper's Email Address: ")
			app_camp_date = input(" (9) Enter Camper's Intended Camp Month (June, July, or August): ")

			#TODO create function to check if month is w/in specified range 

			app_roomate_pref = input(" (10) (Optional) Enter Camper's Roomate Preference (as an ID): ")
			print("\n*** Possible Bands: 'Band1', 'Band2', 'Band3', 'Band4', 'Band5', 'Band6', 'Band7' and 'Band8' *** ")
			app_band_pref = input(" (11) (Optional) Enter Camper's Band Preference: ")

			#SQL INSERT statement 

			c, conn = create_db()
			t = (app_id, app_first_name, app_last_name, app_address, app_gender, app_age, app_band_role, app_roomate_pref, app_band_pref, app_email, app_camp_date, 'TBD', 'TBD')
			c.execute("INSERT INTO application VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", t)
			
			save_db_changes(conn)


		if (user_in == 'look' or user_in == 'Look' or user_in == 'LOOK'):

			print('\n')
			app_id = input(" (1) Enter Camper's ID to Search: ")

			#SQL SELECT statement 
			c, conn = create_db()
			 
			c.execute("SELECT * FROM application WHERE camper_id = '"+ app_id + "'")
			r = c.fetchone()

			if (r):
				print("\n")
				print(" - Camper ID : ", r[0])
				print("\n")
				print(" - Camper Name : ", r[1] + " " + r[2])
				print(" - Camper Address : ", r[3])
				print(" - Camper Age : ", r[5])
				print(" - Camper Gender : ", r[4])
				print(" - Camper's Proposed Band Role : ", r[6])
				print(" - Camper Roomate Preference : ", r[7])
				print(" - Camper Band Preference : ", r[8])
				print(" - Camper Email : ", r[9])
				print(" - Camper's Proposed Camp Start Date : ", r[10])

				print("\n")
				if r[11] == "R" or r[11] == "r":
					print(" - Camper Application Status : REJECTED")
				elif r[11] == "A" or r[11] == "a":
					print(" - Camper Application Status : ACCEPTED")
				else:
					print(" - Camper Application Status : " + r[11])

				print(" - Camper's Deposit Has Cleared: " + r[12])

			else:
				print("\n")
				print("ERROR: CAMPER ID: "+ app_id+" IS NOT IN THE DATABASE.")
			
			
			save_db_changes(conn)
				
"""
	Menu Option to allow client to make and mail application status notifications 
	to the campers. Also, the client updates the camper's application on whether the 
	inital deposit payment has successfully processed. 

"""			
def make_decision():

	loop = 1
	while (loop):
		print('\n')
		print('##################################################################\n')
		print ("******* WELCOME TO THE CAMPER APPLICATION UPDATE PAGE ********\n")
		print(" (1) Type 'Back' to Return to the Main Menu")
		print(" (2) Type 'Mail' to Make & Email Decision to Camper")
		print (" (3) Type 'Pay' to Update Camper Applicant Payment Info")
		print('\n')

		print('##################################################################\n')	


		user_in = input("Enter Command : ")
		print('\n')

		# Back to Main Menu 
		if (user_in == 'back' or user_in == 'Back' or user_in == 'BACK'):
			loop = 0


		# Process Payment 
		if (user_in == "Pay" or user_in == "pay" or user_in == "PAY"):
			print('\n')
			camper_id = input("Enter Camper ID: ")

			# execute SQl search query 
			c, conn = create_db()
			c.execute("SELECT payment, email FROM application WHERE camper_id = '"+ camper_id + "'")
			r = c.fetchone()

			if (r):
				payment_status = r[0]
				email = r[1]
				if(payment_status == 'TBD'):
					successful = input(" (1) Has the Camper's Desposit Cleared? (Yes or No) : ")

					if (successful == "yes" or successful == "Yes" or successful == "YES"):
						t = ("Yes", camper_id)
						c.execute("UPDATE application SET payment = ? WHERE camper_id= ?", t)
					elif (successful == "no" or successful == "No" or successful == "NO"):
						t = ("No", camper_id)
						c.execute("UPDATE application SET payment = ? WHERE camper_id= ?", t)

						print(" \nNOTE: A payment that fails to process leads to an immediate rejection\n")
						default_comment = "Thank You for applying, but the selection was a highly competitve process and you didn't quite make the cut. Learning how to accept rejection is an important skill for an aspiring rocker."
						comment = input(" (2) Enter comment about rejection to be sent to: " + email + " : ")
						include_default = input(" (3) Would you like to include the default rejection comment? (y or n) ")
						if (include_default == 'y' or include_default == 'Y'):
							final_message = default_comment + " \n" + comment 
						if (include_default == 'n' or include_default == 'N'):
							final_message = comment 

						t = ("R", camper_id)
						c.execute("UPDATE application SET status = ? WHERE camper_id= ?", t)

					else:
						continue


			else:
				print("\n")
				print("ERROR: CAMPER ID: "+ camper_id+" DOES NOT EXIST IN THE DATABASE.")
			
			save_db_changes(conn)

		# Mail Camper Notification 	
		if (user_in == 'mail' or user_in == 'Mail' or user_in == 'MAIL'):
			print('\n')
			camper_id = input("Enter Camper ID: ")

			# execute SQl search query 
			c, conn = create_db()
			c.execute("SELECT email, status, camp_dates FROM application WHERE camper_id = '"+ camper_id + "'")
			r = c.fetchone()

			if(r):

				email = r[0]
				status = r[1]
				date = r[2]

				if(status == "TBD"):

					loop2 = 1
					while(loop2):
						print('\n')
						decision = input(" (1) Enter Decision ('A' for acceptance, 'R' for rejection, 'E' to go back to menu): ")

						if (decision == 'A' or decision == 'a'):
							loop2 = 0 
							comment = input(" (2) Enter congratulatory comment to be sent to: " + email + " : ")
							rank = input(" (3) Was there a Ranking made for this Camper by the Director? If so, please enter: ")
							
							# update status in 'application' table
							t = (decision, camper_id)
							c.execute("UPDATE application SET status = ? WHERE camper_id= ?", t)

							# put accepted camper into check-in table 
							t = (camper_id,date,0,1,0,0,0,0,0)
							c.execute("INSERT INTO check_in VALUES (?,?,?,?,?,?,?,?,?)", t)

							save_db_changes(conn)

							print('##################################################################\n')	
							print("\nACCEPTANCE NOTIFICATION SENT! \n")
							print('##################################################################\n')	


						elif (decision == 'R' or decision == "r"):
							loop2 = 0 
							default_comment = "Thank You for applying, but the selection was a highly competitve process and you didn't quite make the cut. Learning how to accept rejection is an important skill for an aspiring rocker."
							comment = input(" (2) Enter comment about rejection to be sent to: " + email + " : ")
							include_default = input(" (3) Would you like to include the default rejection comment? (y or n) ")
							if (include_default == 'y' or include_default == 'Y'):
								final_message = default_comment + " \n" + comment 
							if (include_default == 'n' or include_default == 'N'):
								final_message = comment 

							t = (decision, camper_id)
							c.execute("UPDATE application SET status = ? WHERE camper_id= ?", t)
							save_db_changes(conn)

							print('##################################################################\n')	
							print("\nREJECTION NOTIFICATION SENT! \n")

							print("\n*** Here is the final message that was sent:")
							print(final_message)
							print()
							print('##################################################################\n')
			
						elif (decision == "E" or decision == "e"):
							loop2 = 0
							save_db_changes(conn) 

						else:
							loop2 = 1

				else:
					print("\n")
					print("ERROR: CAMPER ID: "+ camper_id+" HAS ALREADY BEEN REVIEWED")
					save_db_changes(conn)

			else:
				print("\n")
				print("ERROR: CAMPER ID: "+ camper_id+" DOES NOT EXIST IN THE DATABASE.")
				save_db_changes(conn)



"""			
Menu Option to 'Check-In' a given Camper. The client could enter Emergency Contact Info, Medical Info, 
Legal Info, Search for the Camper given an 'ID' and Officially Check-In a given Camper

"""

def check_in_camper():

	loop = 1
	while (loop):
		print('\n')
		print('##################################################################\n')
		print ("******* WELCOME TO THE CAMPER CHECK-IN PAGE ********\n")
		print(" (1) Type 'Back' to return to main menu")
		print(" (2) Type 'New' to Officially Check-In the New Camper ")
		print(" (3) Type 'E' to enter Emergency Contact for Camper ")
		print(" (4) Type 'M' to enter Medical Info for Camper ")
		print(" (5) Type 'L' to enter Legal Info for Camper ")
		print(" (6) Type 'Look' to view Camper Info (Check if all forms were submitted)")
		print('##################################################################\n')
		print('\n')
		print('\n')
		user_in = input("Enter Command : ")
		print('\n')

		if (user_in == 'back' or user_in == 'Back' or user_in == 'BACK'):
			loop = 0

		if (user_in == 'e' or user_in == "E"):

			print('\n')
			camper_id = input(" (1) Enter Camper ID: ")

			# execute SQl search query 
			c, conn = create_db()
			c.execute("SELECT emergency_contact_form FROM check_in WHERE camper_id = '"+ camper_id + "'")
			r = c.fetchone()

			if(r):
				has_em = r[0]
				if (has_em):
					print("\n *** NOTE: Camper "+camper_id+" has already submitted the Emergency Contact Form \n")
				else:
					first_name_contact = input(" (2) Enter the First Name of Emergency Contact: ")
					last_name_contact = input(" (3) Enter the Last Name of Emergency Contact: ")
					phone_contact = input(" (4) Enter the Phone Number of Emergency Contact: ")

					# insert values into emergency_contact table
					t = (camper_id, first_name_contact, last_name_contact, phone_contact)
					c.execute("INSERT INTO emergency_contact VALUES (?,?,?,?)", t)

					# update values of check_in table 
					t = (1, camper_id)
					c.execute("UPDATE check_in SET emergency_contact_form = ? WHERE camper_id= ?", t)

			else:
				print("\n")
				print("ERROR: CAMPER ID: "+ camper_id+" DOES NOT EXIST IN THE DATABASE.")
			
			save_db_changes(conn)
			


		if (user_in == 'm' or user_in == "M"):

			print('\n')
			camper_id = input(" (1) Enter Camper ID: ")

			# execute SQl search query 
			c, conn = create_db()
			c.execute("SELECT medical_form FROM check_in WHERE camper_id = '"+ camper_id + "'")
			r = c.fetchone()

			if(r):
				has_em = r[0]
				if (has_em):
					print("\n *** NOTE: Camper "+camper_id+" has already submitted the Medical Form \n")
				else:
					insurance = input(" (2) Enter the Camper's Medical Insurance: ")
					doc_name = input(" (3) Enter the Camper's Doctor's Name : ")
					dent_name = input(" (4) Enter the Camper's Dentist's Name : ")
					allergies = input(" (5) List any allergies that the Camper has : ")
					medications = input(" (6) Enter any medications that the Camper is taking : ")

					# insert values into medical table
					t = (camper_id, insurance, doc_name, dent_name, allergies, medications)
					c.execute("INSERT INTO medical VALUES (?,?,?,?,?,?)", t)

					# update values of check_in table 
					t = (1, camper_id)
					c.execute("UPDATE check_in SET medical_form = ? WHERE camper_id= ?", t)

			else:
				print("\n")
				print("ERROR: CAMPER ID: "+ camper_id+" DOES NOT EXIST IN THE DATABASE.")
			
			save_db_changes(conn)

		if (user_in == 'l' or user_in == "L"):

			print('\n')
			camper_id = input(" (1) Enter Camper ID: ")

			# execute SQl search query 
			c, conn = create_db()
			c.execute("SELECT legal_form FROM check_in WHERE camper_id = '"+ camper_id + "'")
			r = c.fetchone()

			if(r):
				has_em = r[0]
				if (has_em):
					print("\n *** NOTE: Camper "+camper_id+" has already submitted the Legal Form \n")
				else:
					par_first_name = input(" (2) Enter the Camper's Gaurdian/Parent First Name: ")
					par_last_name = input(" (3) Enter the Camper's Gaurdian/Parent Last Name : ")
					par_age = input(" (4) Enter the Camper's Gaurdian/Parent Age : ")
					is_par = input(" (5) Is this person the Camper's Parents (Yes or No) : ")
					

					# insert values into legal table
					t = (camper_id, par_first_name, par_last_name, par_age, is_par)
					c.execute("INSERT INTO legal VALUES (?,?,?,?,?)", t)

					# update values of check_in table 
					t = (1, camper_id)
					c.execute("UPDATE check_in SET legal_form = ? WHERE camper_id= ?", t)

			else:
				print("\n")
				print("ERROR: CAMPER ID: "+ camper_id+" DOES NOT EXIST IN THE DATABASE.")
			
			save_db_changes(conn)

		if (user_in == "look" or user_in == "LOOK" or user_in == "Look"):

			print('\n')
			camper_id = input(" (1) Enter Camper's ID to Search: ")

			#SQL SELECT statement 
			c, conn = create_db()
			 
			c.execute("SELECT * FROM check_in WHERE camper_id = '"+ camper_id + "'")
			r = c.fetchone()

			if (r):
				print("\n")
				print(" - Camper ID :  ", r[0])
				print("\n")
				print(" - Camper Proposed Camp Session Date :  ", r[1])
				if (r[2]): print(" - Has Camper Checked-In :  Yes")
				else: print(" - Has Camper Checked-In :  No")
				if (r[3]): print(" - Do we have Camper's application?  :  Yes")
				else: print(" - Do we have Camper's application :  No")
				if (r[4]): print(" - Do we have Camper's Emergency Contact Form?  :  Yes")
				else: print(" - Do we have Camper's Emergency Contact Form :  No")
				if (r[5]): print(" - Do we have Camper's Legal Form?  :  Yes")
				else: print(" - Do we have Camper's Legal Form :  No")
				if (r[6]): print(" - Do we have Camper's Medical Form?  :  Yes")
				else: print(" - Do we have Camper's Medical Form :  No")



			else:
				print("\n")
				print("ERROR: CAMPER ID: "+ camper_id+" IS NOT IN THE DATABASE.")
			
			
			save_db_changes(conn)

		if (user_in == 'new' or user_in == 'New' or user_in == 'NEW'):
			print('\n')
			camper_id = input(" (1) Enter Camper ID: ")

			# TODO: First, check if the camper ID is already in the 'check_in' table. If not, continue on. 

			# execute SQl search query 
			c, conn = create_db()
			c.execute("SELECT * FROM check_in WHERE camper_id = '"+ camper_id + "'")
			r = c.fetchone()


			if (r):
				if(int(r[2])):
					print("\n")
					print("ERROR: CAMPER ID: "+camper_id+" HAS ALREADY BEEN CHECKED IN.\n")
				else:
					if(int(r[3]) == 1 and int(r[4]) == 1 and int(r[5]) == 1 and int(r[6]) == 1 ):


						#TODO ASSIGN dorm, band & update the database 

						#make_dorm_assignment()
						#make_band_assignment()


						# Then, we could check the camper in
						t = (1, camper_id)
						c.execute("UPDATE check_in SET has_checked_in = ? WHERE camper_id= ?", t) 

						print("\n")
						print('##################################################################\n')
						print("CONGRATULATIONS: Camper: " + camper_id + " has officially checked in into Future Rock Stars Camp!!!!\n") 
						print('##################################################################\n')
						print('\n')
					else:
						print("\n")
						print("ERROR: Camper ID: "+camper_id+" Has Not Turned In All Necessary Forms, and Could Not be Checked-In.\n")



			else: 
				print("\n")
				print("ERROR: CAMPER ID: "+ camper_id+" DOES NOT EXIST IN THE DATABASE.")

			save_db_changes(conn)


"""			
Menu Option to Enter 'Maintenance Mode'
"""
def maintenance_mode():
	pswd = getpass.getpass('Enter Password :')
	if (pswd == "campers123"):
		loop = 1
		while (loop):
			print('\n')
			print('##################################################################\n')
			print ("******* WELCOME TO MAINTENANCE MODE ********\n")
			print(" (1) Type 'Back' to return to main menu")
			print(" (2) Type 'D' to Clear All Current Data From Database")
			print('##################################################################\n')
			print('\n')
			print('\n')
			user_in = input("Enter Command : ")
			print('\n')

			if (user_in == 'back' or user_in == 'Back' or user_in == 'BACK'):
				loop = 0

			if (user_in == "D" or user_in == "d"):
				remov = input("Are you sure you want to remove this database? (y or n): ")
				if (remov == "y" or remov == "Y"):
					
					try:
						os.remove("example.db")

					except FileNotFoundError:
						print("\n")
						print("*** ERROR: Database has already been cleared. ***")
	else:
		print('##################################################################\n')
		print("MAINTENANCE MODE: ACCESS DENIED \n")
		print('##################################################################')



"""
Displays the Main Menu Options to the client 
"""
def display_menu():
	loop = 1
	while(loop):
		main()
		user_in = input("Enter Command : ")
		
		if (user_in == 'q'):
			loop = 0
		elif (user_in == 'c'):
			check_in_camper()

		elif (user_in == 'a'):
			handle_applications()

		elif (user_in == 'm'):
			make_decision()

		elif(user_in == 'x'):
			maintenance_mode()
	

display_menu()	
