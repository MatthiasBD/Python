hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
face = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eyes = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

Eva = {"hair": "blonde", "face": "oval", "eyes": "blue", "gender": "female", "race": "white"}
Larisa = {"hair": "brown", "face": "oval", "eyes": "brown", "gender": "female", "race": "white"}
Matej = {"hair": "black", "face": "oval", "eyes": "blue", "gender": "male", "race": "white"}
Miha = {"hair": "brown", "face": "square", "eyes": "green", "gender": "male", "race": "white"}

with open("dna.txt", "r") as dnafile:
	dna = dnafile.read()

suspect = {}

for item in hair:
	if dna.find(hair[item]) != -1:
		suspect["hair"] = item

for item in face:
	if dna.find(face[item]) != -1:
		suspect["face"] = item

for item in eyes:
	if dna.find(eyes[item]) != -1:
		suspect["eyes"] = item

for item in gender:
	if dna.find(gender[item]) != -1:
		suspect["gender"] = item

for item in race:
	if dna.find(race[item]) != -1:
		suspect["race"] = item

for item in suspect:
	print item + " = " + suspect[item]

guilty = 0

for item in Eva:
	if Eva[item] == suspect[item]:
		guilty += 1

if guilty < 5:
	print "Eva is not guilty"
else:
	print "Eva is guilty"

guilty = 0

for item in Larisa:
	if Larisa[item] == suspect[item]:
		guilty += 1

if guilty < 5:
	print "Larisa is not guilty"
else:
	print "Larisa is guilty"

guilty = 0

for item in Matej:
	if Matej[item] == suspect[item]:
		guilty += 1

if guilty < 5:
	print "Matej is not guilty"
else:
	print "Matej is guilty"

guilty = 0

for item in Miha:
	if Miha[item] == suspect[item]:
		guilty += 1

if guilty < 5:
	print "Miha is not guilty"
else:
	print "Miha is guilty"
