from pyfiglet import figlet_format
from sd_dorm_assign import *

def main():

	print()
	
	print(figlet_format('Future Rock Stars!', font='starwars'))
	
	print('##################################################################\n')

	print("WELECOME TO THE REGISTRATION NETWORK\n")
	print(" (1) Enter 'q' to Quit")
	print(" (2) Enter 'c' to Check In a Camper")
	print(" (3) Enter 'm' to Mail Application Decision Notification")
	print(" (4) Enter 'a' to Handle Applications")
	print(" (5) Enter 'x' to go into Maintence Mode")
	

	print('##################################################################\n')

	
	print()


def handle_applications():

	loop = 1
	while (loop):
		print('\n')
		print('##################################################################\n')
		print ("******* WELCOME TO THE CAMPER APPLICATION PAGE ********\n")
		print(" (1) Type 'Back' to return to main menu\n")
		print(" (2) Type 'New' to Enter a new Application into the Database \n")
		print('\n')

		print('##################################################################\n')	


		user_in = input("Enter Command : ")
		print('\n')


		if (user_in == 'back' or user_in == 'Back' or user_in == 'BACK'):
			loop = 0


		if (user_in == 'new' or user_in == 'New' or user_in == 'NEW'):
			print('\n')
			app_first_name = input(" (1) Enter Camper's First Name: ")
			app_last_name = input(" (2) Enter Camper's Last Name: ")
			app_address = input(" (3) Enter Camper's Address: ")
			app_age = input(" (4) Enter Camper's Age: ")
			print("\n*** Possible Band Roles: 'Singer', 'Guitarist', 'Drummer', 'Bassist', 'Keyboardist' and 'Instrumentalist' *** ")
			app_band_role = input(" (5) Enter Camper's Intended Band Role: ")
			app_email = input(" (6) Enter Camper's Email Address: ")
			app_camp_date = input(" (7) Enter Camper's Intended Camp Dates: ")
			app_roomate_pref = input(" (8) (Optional) Enter Camper's Roomate Preference (as an ID): ")
			app_band_pref = input(" (9) (Optional) Enter Camper's Band Preference: ")

			#TODO INSERT all that data into the 'application' table in our DB


			

def make_decision():

	loop = 1
	while (loop):
		print('\n')
		print('##################################################################\n')
		print ("******* WELCOME TO THE CAMPER APPLICATION UPDATE PAGE ********\n")
		print(" (1) Type 'Back' to Return to the Main Menu\n")
		print(" (2) Type 'Mail' to Email Decision to Camper \n")
		print('\n')

		print('##################################################################\n')	


		user_in = input("Enter Command : ")
		print('\n')


		if (user_in == 'back' or user_in == 'Back' or user_in == 'BACK'):
			loop = 0

		if (user_in == 'mail' or user_in == 'Mail' or user_in == 'MAIL'):
			print('\n')
			camper_id = input("Enter Camper ID: ")

			# TODO:  Find the camper using 'camper_id' in the 'applications' table 
			# return camper_id, and email, acceptance value  
			email = "test@test.com"
			found = 1

			if(found):

				loop2 = 1
				while(loop2):
					print('\n')
					decision = input(" (1) Enter Decision ('A' for acceptance, 'R' for rejection, 'E' to go back to menu): ")
					if (decision == 'A' or decision == 'a'):
						loop2 = 0 
						comment = input(" (2) Enter congratulatory comment to be sent to: " + email + " : ")
						rank = input(" (3) Was there a Ranking made for this Camper by the Director? If so, please enter: ")
						print('##################################################################\n')	
						print("\nACCEPTANCE NOTIFICATION SENT! \n")
						print('##################################################################\n')	
						# TODO insert rank value & acceptance value into the 'application' table for campuer_id 
				

					elif (decision == 'R' or decision == "r"):
						loop2 = 0 
						default_comment = "Thank You for applying, but the selection was a highly competitve process and you didn't quite make the cut. Learning how to accept rejection is an important skill for an aspiring rocker."
						comment = input(" (2) Enter comment about rejection to be sent to: " + email + " : ")
						include_default = input(" (3) Would you like to include the default rejection comment? (y or n) ")
						if (include_default == 'y' or include_default == 'Y'):
							final_message = default_comment + " \n" + comment 
						if (include_default == 'n' or include_default == 'N'):
							final_message = comment 

						# TODO insert acceptance value as 'R' into the 'application' table for campuer_id 

						print('##################################################################\n')	
						print("\nREJECTION NOTIFICATION SENT! \n")

						print("\n*** Here is the final message that was sent:")
						print(final_message)
						print()
						print('##################################################################\n')	
						
					elif (decision == "E" or decision == "e"):
						loop2 = 0 

					else:
						loop2 = 1












def check_in_camper():

	loop = 1
	while (loop):
		print('\n')
		print('##################################################################\n')
		print ("******* WELCOME TO THE CAMPER CHECK-IN PAGE ********\n")
		print(" (1) Type 'Back' to return to main menu\n")
		print('\n')
		print(" (2) Type 'New' to Officially Check-In the New Camper \n")
		print(" (3) Type 'E' to enter Emergency Contact for Camper \n")
		print(" (4) Type 'M' to enter Medical Info for Camper \n")
		print(" (5) Type 'L' to enter Legal Info for Camper \n")
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

			# TODO: First, check if the camper ID is already in the 'emergency_contact' table. If not, continue on. 

			first_name_contact = input(" (2) Enter the First Name of Emergency Contact: ")
			last_name_contact = input(" (3) Enter the Last Name of Emergency Contact: ")

			# TODO: INSERT that data into the 'emergency_contact' table for that Camper ID


		if (user_in == 'm' or user_in == "M"):

			continue

		if (user_in == 'l' or user_in == "L"):

			continue


		if (user_in == 'new' or user_in == 'New' or user_in == 'NEW'):
			print('\n')
			camper_id = input(" (1) Enter Camper ID: ")

			# TODO: First, check if the camper ID is already in the 'check_in' table. If not, continue on. 

			# TODO: Enter SQL statement to search for camper in 'application', 
			# and select the camper_id, camp_dates and save them into variables. 

			# TODO: Search for camper in the 'emergency_contact', if the camper_id is there then move on. If not, print Error message
			# notifiying missing info. 

			# TODO: Search for camper in the 'legal', if the camper_id is there then move on. If not, print Error message
			# notifiying missing info 

			# TODO: Search for camper in the 'legal', if the camper_id is there then move on. If not, print Error message
			# notifiying missing info

			# TODO: If all those checks passed, then INSERT camper into 'check_in' table, and make dorm & band assignments 

			#make_dorm_assignment()
			#make_band_assignment()

			print("\n")
			print('##################################################################\n')
			print("CONGRATULATIONS: Camper: " + camper_id + " has officially checked in into Future Rock Stars Camp!!!!\n") 
			print('##################################################################\n')
			print('\n')










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
			


display_menu()	
