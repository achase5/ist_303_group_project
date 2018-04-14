

import pickle
import os 
from collections import Counter




"""
Check if pickle files containing the saved Dorm dictionaries exist. If so, load the files.  

"""

if (os.path.exists("male_dorms.p")):
	
	male_dorms = pickle.load(open("male_dorms.p", "rb"))

else:
	
	"""
	
	Each Dorm is saved in dictionary according to gender
	For example, the male dorm 'A' is daved as: 'A' : [ (Camper_ID, Age), (Camper_ID, Age), .. ] 

	"""

	male_dorms = {
	
		'A' : [],
		'B': [],
		'C' : []

	} 



if (os.path.exists("female_dorms.p")):
	
	female_dorms = pickle.load(open("female_dorms.p", "rb"))

else:
	
	female_dorms = {
	
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

Assign male Camper to appropriate dorm 

id: Camper ID
age: Camper age
a,b : Camper age range (e.g. if the camper is 16 yrs old, then the age range will be a=15, b=16)

"""
def assign_male(id, age, a, b):

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

		if( len(arr) < 8 and sum_age_count < 3):
			# then, we could add this camper to our dorm
			male_dorms[key].append((id,age))
			pickle.dump( male_dorms, open( "male_dorms.p", "wb" ) )

			# TODO: add in SQL INSERT command to insert camper into DORM TABLE
			return 1



"""

Assign female Camper to appropriate dorm 

id : Camper ID
age : Camper age
a,b : Camper age range (e.g. if the camper is 16 yrs old, then the age range will be a=15, b=16)

"""
def assign_female(id, age, a, b):

	for key in female_dorms:
		arr = female_dorms[key]
		age_count = Counter(elt[1] for elt in arr)
		sum_age_count = 0
		if (age_count[str(a)]): sum_age_count += age_count[str(a)]
		if (age_count[str(b)]): sum_age_count += age_count[str(b)]

		if( len(arr) < 8 and sum_age_count < 3):
			# then, we could add this camper to our dorm
			female_dorms[key].append((id,int(age)))
			pickle.dump( female_dorms, open( "female_dorms.p", "wb" ) )

			# TODO: add in SQL INSERT command to insert camper into DORM TABLE
			return 1



"""
Assigns a Dorm room to a given Camper

id : Camper ID
gender : Camper's Gender
age : Camper age

"""
def assign_dorm(id, gender, age):

	a,b = get_age_range(int(age))
	#print("TEST: range: ", a, b)

	if (gender == "male" or gender == "m" or gender == "Male" or gender == "M"):
		assign_male(id, age, a, b)

	else:
		assign_female(id, age, a, b)



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
def dorm_insertion_check(id, gender, age, dorm_name):
	
	a,b = get_age_range(int(age))

	if gender == "male" and dorm_name in list(male_dorms.keys()):
		
		arr = male_dorms[dorm_name]
		age_count = Counter(elt[1] for elt in arr)
		sum_age_count = 0
		if (age_count[str(a)]): sum_age_count += age_count[str(a)]
		if (age_count[str(b)]): sum_age_count += age_count[str(b)]

		if ( len(arr) < 8 and sum_age_count < 3 ):
			return 1

		return 0 

	elif gender == "female" and dorm_name in list(female_dorms.keys()):

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




"""
assign_dorm("101","male","18")
print(male_dorms)
print(female_dorms)
"""

 









