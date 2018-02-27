import pickle
import os 
from collections import Counter




"""
Check if dorm pickle files exists. If so, load the file 

"""

if (os.path.exists("band_assignments.p")):
	
	band_assignments = pickle.load(open("band_assignments.p", "rb"))

else:
	
	band_assignments = {
	
		'Band1' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band2' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band3' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band4' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band5' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band6' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band7' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band8' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		}

	} 


def get_gender_distribution(gender, temp_dict):

	male_count = 0 
	female_count = 0

	for k in temp_dict:
		if len(temp_dict[k]) != 0:
			if( temp_dict[k][0][1] == "male"):
				male_count += 1
			else:
				female_count += 1

	if gender == "female" and female_count < 3:
		return 1
	elif gender == "male" and male_count < 3:
		return 1
	else: 
		return 0 




def assign_band(id, band_role, gender):

	for key in band_assignments:
		if (len(band_assignments[key][band_role]) == 0):

			temp_dict = band_assignments[key]
			if(get_gender_distribution(gender, temp_dict)):
				band_assignments[key][band_role].append((id, gender))
				pickle.dump( band_assignments, open( "band_assignments.p", "wb" ) )
				#TODO : add in SQL statement to update/insert the band assignment

				return 1 



def swap_request(id1, band_role1, id2, band_role2):

	if band_role1 == band_role2: return 0 


	# find the bands for id1 and id2 
	for key in band_assignments:

		if( band_assignments[key][band_role1][0][0] == id1):
			id1_band = key

		if( band_assignments[key][band_role2][0][0] == id2):
			id2_band = key

	if id1_band == id2_band: return 0 







"""
assign_band("102", "Singer", "male")
print(band_assignments)

"""










