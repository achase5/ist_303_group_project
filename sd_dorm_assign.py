
from sqlite_dbv3 import * 
import pickle
import os 
from collections import Counter



"""
Check if pickle files containing the saved Dorm dictionaries exist. If so, load the files.  

"""

if (os.path.exists("June_male_dorms.p")):
	
	June_male_dorms = pickle.load(open("June_male_dorms.p", "rb"))

else:
	
	"""
	
	Each Dorm is saved in dictionary according to gender
	For example, the male dorm 'A' is daved as: 'A' : [ (Camper_ID, Age), (Camper_ID, Age), .. ] 

	"""

	June_male_dorms = {
	
		'A' : [],
		'B': [],
		'C' : []

	} 



if (os.path.exists("June_female_dorms.p")):
	
	June_female_dorms = pickle.load(open("June_female_dorms.p", "rb"))

else:
	
	June_female_dorms = {
	
		'D' : [],
		'E': [],
		'F' : []

	} 

if (os.path.exists("July_male_dorms.p")):
	
	July_male_dorms = pickle.load(open("July_male_dorms.p", "rb"))

else:
	
	"""
	
	Each Dorm is saved in dictionary according to gender
	For example, the male dorm 'A' is daved as: 'A' : [ (Camper_ID, Age), (Camper_ID, Age), .. ] 

	"""

	July_male_dorms = {
	
		'A' : [],
		'B': [],
		'C' : []

	} 



if (os.path.exists("July_female_dorms.p")):
	
	July_female_dorms = pickle.load(open("July_female_dorms.p", "rb"))

else:
	
	July_female_dorms = {
	
		'D' : [],
		'E': [],
		'F' : []

	} 

if (os.path.exists("August_male_dorms.p")):
	
	August_male_dorms = pickle.load(open("August_male_dorms.p", "rb"))

else:
	
	"""
	
	Each Dorm is saved in dictionary according to gender
	For example, the male dorm 'A' is daved as: 'A' : [ (Camper_ID, Age), (Camper_ID, Age), .. ] 

	"""

	August_male_dorms = {
	
		'A' : [],
		'B': [],
		'C' : []

	} 



if (os.path.exists("August_female_dorms.p")):
	
	August_female_dorms = pickle.load(open("August_female_dorms.p", "rb"))

else:
	
	August_female_dorms = {
	
		'D' : [],
		'E': [],
		'F' : []

	} 

"""
Given a age (13-18), the approrpiate 'range' is calculated

age : given 'age' value of a camper 
"""
def get_age_range(age):

	if age == 17 or age == 18:
		a = 17 
		b = 18

	elif age == 15 or age == 16:
		a = 15
		b = 16

	else:
		a = 13
		b = 14

	return a,b 

"""
Obtain the Dorm Number of a given ID

"""
def get_dorm_num(id, gender, session):

	if gender == 'Male':

		if (session == "June"):
			male_dorms = June_male_dorms
		elif (session == "July"):
			male_dorms = July_male_dorms
		else:
			male_dorms = August_male_dorms


		for i in male_dorms:
			for (j,k) in male_dorms[i]:
				if str(j) == str(id):
					return i
		return "None"

	else:

		if (session == "June"):
			female_dorms = June_female_dorms
		elif (session == "July"):
			female_dorms = July_female_dorms
		else:
			female_dorms = August_female_dorms


		for i in female_dorms:
			for (j,k) in female_dorms[i]:
				if str(j) == str(id):
					return i
		return "None"

"""
Manually insert Camper into a Dorm (after checking if ok, hopefully)

"""
def insert_into_dorm(id, gender, age, session, dorm_name):

	
	if gender == "Male":

		filename = session + "_male_dorms.p"

		if (session == "June"):
			male_dorms = June_male_dorms
		elif (session == "July"):
			male_dorms = July_male_dorms
		else:
			male_dorms = August_male_dorms

		male_dorms[dorm_name].append((id,age))
		pickle.dump( male_dorms, open( filename, "wb" ) )

	else:

		filename = session + "_female_dorms.p"

		if (session == "June"):
			female_dorms = June_female_dorms
		elif (session == "July"):
			female_dorms = July_female_dorms
		else:
			female_dorms = August_female_dorms

		female_dorms[dorm_name].append((id,age))
		pickle.dump( female_dorms, open( filename, "wb" ) )



"""

Assign male Camper to appropriate dorm 

id: Camper ID
age: Camper age
a,b : Camper age range (e.g. if the camper is 16 yrs old, then the age range will be a=15, b=16)

"""
def assign_male(id, age, a, b, session, dorm_avoid=None):

	filename = session + "_male_dorms.p"
	
	if (session == "June"):
		male_dorms = June_male_dorms
	elif (session == "July"):
		male_dorms = July_male_dorms
	else:
		male_dorms = August_male_dorms


	for key in male_dorms:
		arr = male_dorms[key]
		age_count = Counter(elt[1] for elt in arr)
		sum_age_count = 0
		if (age_count[str(a)]): sum_age_count += age_count[str(a)]
		if (age_count[str(b)]): sum_age_count += age_count[str(b)]

		"""
		print("TEST: key: ", key)
		print("TEST: arr: ", arr)
		print("")
		print("TEST: age_count dict: ", age_count)
		print("TEST: a is: ", a)
		print('TEST: age_count[a] ', age_count[str(a)])
		print("TEST: sum ", sum_age_count)
		print("TEST: length", len(arr))
		"""

		if( len(arr) < 8 and sum_age_count < 3 and key != dorm_avoid ):
			# then, we could add this camper to our dorm
			male_dorms[key].append((id,age))
			pickle.dump( male_dorms, open( filename, "wb" ) )

			# TODO: add in SQL INSERT command to insert camper into DORM TABLE
			return key 



"""

Assign female Camper to appropriate dorm 

id : Camper ID
age : Camper age
a,b : Camper age range (e.g. if the camper is 16 yrs old, then the age range will be a=15, b=16)

"""
def assign_female(id, age, a, b, session, dorm_avoid=None):

	filename = session + "_female_dorms.p"
	
	if (session == "June"):
		female_dorms = June_female_dorms
	elif (session == "July"):
		female_dorms = July_female_dorms
	else:
		female_dorms = August_female_dorms

	for key in female_dorms:
		arr = female_dorms[key]
		age_count = Counter(elt[1] for elt in arr)
		sum_age_count = 0
		if (age_count[str(a)]): sum_age_count += age_count[str(a)]
		if (age_count[str(b)]): sum_age_count += age_count[str(b)]

		if( len(arr) < 8 and sum_age_count < 3 and key != dorm_avoid):
			# then, we could add this camper to our dorm
			female_dorms[key].append((id,int(age)))
			pickle.dump( female_dorms, open( filename, "wb" ) )

			# TODO: add in SQL INSERT command to insert camper into DORM TABLE
			return key 



"""
Assigns a Dorm room to a given Camper

id : Camper ID
gender : Camper's Gender
age : Camper age

"""
def assign_dorm(id, gender, age, session, dorm_avoid=None):

	a,b = get_age_range(int(age))
	#print("TEST: range: ", a, b)

	if (gender == "Male"):
		if dorm_avoid:
			dorm = assign_male(id, age, a, b, session, dorm_avoid=dorm_avoid)
		else:
			dorm = assign_male(id, age, a, b, session)

	else:
		if dorm_avoid:
			dorm = assign_female(id, age, a, b, session, dorm_avoid=dorm_avoid)
		else:
			dorm = assign_female(id, age, a, b, session)

	return dorm 


"""

Check if a Camper of an indicated ID, gender, and age could be inserted 
into a specfic Dorm Name (dorm_name). 

id : Camper ID
gender : Camper's Gender
age : Camper age
dorm_name : dorm name 

Returns 1 if it is ok to insert that Camper into the indicated Dorm
Returns 0 if not

"""
def dorm_insertion_check(id, gender, age, session, dorm_name):
	
	a,b = get_age_range(int(age))

	if gender == "Male":

		if (session == "June"):
			male_dorms = June_male_dorms
		elif (session == "July"):
			male_dorms = July_male_dorms
		else:
			male_dorms = August_male_dorms	
				

		if dorm_name in list(male_dorms.keys()):
			
			arr = male_dorms[dorm_name]
			age_count = Counter(elt[1] for elt in arr)
			sum_age_count = 0
			if (age_count[str(a)]): sum_age_count += age_count[str(a)]
			if (age_count[str(b)]): sum_age_count += age_count[str(b)]

			if ( len(arr) < 8 and sum_age_count < 3 ):
				return 1

		return 0 

	elif gender == "Female":

		if (session == "June"):
			female_dorms = June_female_dorms
		elif (session == "July"):
			female_dorms = July_female_dorms
		else:
			female_dorms = August_female_dorms	


		if dorm_name in list(female_dorms.keys()):

			arr = female_dorms[dorm_name]
			age_count = Counter(elt[1] for elt in arr)
			sum_age_count = 0
			if (age_count[str(a)]): sum_age_count += age_count[str(a)]
			if (age_count[str(b)]): sum_age_count += age_count[str(b)]

			if ( len(arr) < 8 and sum_age_count < 3 ):
				return 1

		return 0

	else:

		return 0 


def dorm_assignment_driver(camper_id_text, preferences):
	# Assign Camper a Dorm 
	
	c, conn = create_db()	
	# get params from camper
	c.execute("SELECT gender, age, camp_dates FROM application WHERE camper_id = '"+ camper_id_text + "'")
	r0 = c.fetchone() 

	# Check if roomate_pref has checked in
	c.execute("SELECT has_checked_in FROM check_in WHERE camper_id = '"+ preferences[0].text() + "'")
	r1 = c.fetchone()

	# Check if roomate_avoid has checked in 
	c.execute("SELECT has_checked_in FROM check_in WHERE camper_id = '"+ preferences[1].text() + "'")
	r2 = c.fetchone()

	if(r1 and r1[0] == 0 and r2 and r2[0] == 0):
		dorm = assign_dorm(camper_id_text, r0[0], r0[1], r0[2])
		
		# INSERT INTO dorm table
		t = (camper_id_text, r0[2], dorm, r0[0], int(r0[1]))
		c.execute("INSERT INTO dorm VALUES (?,?,?,?,?)", t)
 

	# if the pref roomate has checked in, but not roomate_avoid
	elif(r1 and r1[0] == 1 and r2 and r2[0] == 0):

		c.execute("SELECT dorm_number FROM dorm WHERE camper_id = '"+ preferences[0].text() + "'")
		r4 = c.fetchone()
		pref_dorm = r4[0]

		if(dorm_insertion_check(camper_id_text, r0[0], r0[1], r0[2], pref_dorm)):
			insert_into_dorm(camper_id_text, r0[0], r0[1], r0[2], pref_dorm)
			
			# INSERT INTO dorm table
			t = (camper_id_text, r0[2], pref_dorm, r0[0], int(r0[1]))
			c.execute("INSERT INTO dorm VALUES (?,?,?,?,?)", t)

		else:
			dorm = assign_dorm(camper_id_text, r0[0], r0[1], r0[2])
			# INSERT INTO dorm table 
			t = (camper_id_text, r0[2], dorm, r0[0], int(r0[1]))
			c.execute("INSERT INTO dorm VALUES (?,?,?,?,?)", t)

	# if the roomate_avoid has checked in, but not roomate_pref	
	elif(r2 and r2[0] == 1 and r1 and r1[0] == 0 ):
		c.execute("SELECT dorm_number FROM dorm WHERE camper_id = '"+ preferences[1].text() + "'")
		r4 = c.fetchone()
		dorm_avoid = r4[0]

		dorm = assign_dorm(camper_id_text, r0[0], r0[1], r0[2], dorm_avoid=dorm_avoid)
		# INSERT INTO dorm table
		t = (camper_id_text, r0[2], dorm, r0[0], int(r0[1]))
		c.execute("INSERT INTO dorm VALUES (?,?,?,?,?)", t) 

	elif(r2 and r2[0] == 1 and r1 and r1[0] == 1):
		c.execute("SELECT dorm_number FROM dorm WHERE camper_id = '"+ preferences[0].text() + "'")
		r4 = c.fetchone()
		pref_dorm = r4[0]

		c.execute("SELECT dorm_number FROM dorm WHERE camper_id = '"+ preferences[1].text() + "'")
		r5 = c.fetchone()
		dorm_avoid = r5[0]

		if(dorm_insertion_check(camper_id_text, r0[0], r0[1], r0[2], pref_dorm)):
			insert_into_dorm(camper_id_text, r0[0], r0[1], r0[2], pref_dorm)
			# INSERT INTO dorm table
			t = (camper_id_text, r0[2], pref_dorm, r0[0], int(r0[1]))
			c.execute("INSERT INTO dorm VALUES (?,?,?,?,?)", t)
		else:
			dorm = assign_dorm(camper_id_text, r0[0], r0[1], r0[2], dorm_avoid=dorm_avoid)
			# INSERT INTO dorm table
			t = (camper_id_text, r0[2], dorm, r0[0], int(r0[1]))
			c.execute("INSERT INTO dorm VALUES (?,?,?,?,?)", t) 

	else:
		#do regular assignement
		dorm = assign_dorm(camper_id_text, r0[0], r0[1], r0[2])
		# INSERT INTO dorm table
		t = (camper_id_text, r0[2], dorm, r0[0], int(r0[1]))
		c.execute("INSERT INTO dorm VALUES (?,?,?,?,?)", t)

	save_db_changes(conn)  




"""
assign_dorm("101","Male","18","July")
print(July_male_dorms)
print(July_female_dorms)
"""

 









