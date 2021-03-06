"""This app will show a graph of you spending in catagories"""
import csv
import array
import matplotlib.pyplot as plt
import numpy as np

#get bank statement data from CSV file
#Get the value of the first array item:  x = cars[0]
#Modify the value of the first array item: cars[0] = "Toyota"
#use google API Places to find a suitable location then store decription in a database. 
#database of the store name and the catagory. so we dont have to keep searching for it on google.
#when printing show a graph for month to month / show line graph of out the normal and suggest the break like tlm


#catagory common words
income = ["Salaries"]
eatingOut =["KFC", "Fish", "Lady","Malaysia","Britomart","Indian", "MCDONALDS", "Subway"]
shopping =[]
entertainment =["KFC", "Lula", "asb", "Cassette", "Liquor", "Convenience", "Rooftop"]
travel =[]
groceries =["Countdown"]
rent =["flat"]
transport =["Ola", "Z", "Transport"]
health =[]
education =[]
saving =["Holiday", "Education","funds", "Growth investments", "Education"]
utilities =["Spark","Laundromat"]

#setting the total amount to 0 for 
catagories = {
  "total Income": 0,
  "Eating Out": 0,
  "Shopping": 0,
  "Entertainment": 0,
  "Travel": 0,
  "Groceries": 0,
  "Rent": 0,
  "Transport": 0,
  "Health": 0,
  "Education": 0,
  "Utilities": 0,
  "Saving": 0,
  "Unallocated": 0  
}

def is_in_catagory(amount,other_party):
	print(type(amount))
	listLength = len(other_party)
	count = 0
	for key_word in other_party:
		print("teasting= key_word+" + str(key_word) +", amount="+ str(amount)+ ", other_p= " +str(key_word))
		if amount == "Amount":
			print("this was passed")
			count +=1
			break
		elif key_word in eatingOut:
			catagories["Eating Out"] += float(amount)
			print("catagories Eating Out added + " + str(amount))
			count +=1
			break
		elif key_word in entertainment:
			catagories["Shopping"] += float(amount)
			print("catagories Shopping added + " + str(amount))
			count +=1
			break
		elif key_word in groceries:
			catagories["Groceries"] += float(amount)
			print("catagories Groceries added + " + str(amount))
			count +=1
			break
		elif key_word in rent:
			catagories["Rent"] += float(amount)
			print("catagories rent added + " + str(amount))
			count +=1
			break
		elif key_word in transport:
			catagories["Transport"] += float(amount)
			print("catagories Transport added + " + str(amount))
			count +=1
			break
		elif key_word in saving:
			catagories["Saving"] += float(amount)
			print("catagories Saving added + " + str(amount))
			count +=1
			break
		elif key_word in utilities:
			catagories["Utilities"] += float(amount)
			print("catagories Utilities added + " + str(amount))
			count +=1
			break
		elif key_word in income:
			catagories["total Income"] += float(amount)
			print("catagories total Income added + " + str(amount))
			count +=1
			break
		else:
			if count != listLength:
				print("pass")
				count +=1
				pass
			else:
				catagories["Unallocated"] +=  float(amount)
				print("catagories Unallocated added + " + amount)


#extract inforamtion from CSV file 
with open('testJan20.csv', newline='') as bankStatement:
	reader = csv.reader(bankStatement)
	for row in reader:
		#us function to allocate transaction into the right bucket
		is_in_catagory(row[1],row[2].split())
		#print(row[2].split())

for x in catagories:
    print ("catagories = " +str(x)+str(catagories[x]))


#exp_val = list(abs(catagories.values()))
#exp_key = list(catagories.keys())
exp_val = []
exp_key = []
k, v = [], []
#split dectionary of category into two list so we can use the matplotlib
for key, value in catagories.items():
	if  key == "Unallocated":
		print("skipped unallocated")
	elif key == "total Income":
		print("skipped total income")
	else:	
		exp_key.append(key)
		exp_val.append(abs(value))
		print("added to list")
plt.pie(exp_val, labels = exp_key, radius=1.2, autopct='%0.2f%%', explode=[0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2])
plt.show()
