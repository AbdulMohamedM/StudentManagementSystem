import os
import platform

global listStd #Making ListStd As Super Global Variable
listStd = [] #List Of Students

def manageStudent(): #Function For The Student Management System
	#Printing Welcome Message And options For This Program
	print(""" 
  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |============================BUILD BY ABDUL MOHAMED====|
  ------------------------------------------------------

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student
Enter 5 : To Rename Student Name """)

	try: #Using Exceptions For Validation
		userInput = int(input("\nPlease Select An Above Option: ")) #Will Take Input From User
	except ValueError:
		print("\noops! That's Not A Number Please enter a valid options \'(1-4)\'") #Error Message
	else:
		print("\n") #Print New Line

	#Checking Using Option	
	if(userInput == 1): #This Option Will Print List Of Students
		if(listStd==[]):
			print("No Student List added Not yet Please \"Enter 2 : To Add New Student\"")
		else:
			print("List Students\n")  
			for students in listStd:
				print("=> {}".format(students))

	elif(userInput == 2): #This Option Will Add New Student In The List
		newStd = input("Enter New Student: ")
		 
		if(newStd in listStd): #This Condition Checking The New Student Is Already In List Ur Not
			print("\nThis Student {} Already In The Database".format(newStd))  #Error Message
		else:					
			listStd.append(newStd)
			print("\n=> New Student {} Successfully Add \n".format(newStd))
			for students in listStd:
				print("=> {}".format(students))	

	elif(userInput == 3): #This Option Will Search Student From The List
		print("List Students\n")  
		print("=> {}".format(students))
		if(listStd==[]):
			print("No Student List added Not yet Please \"Enter 2 : To Add New Student\"")
		else:
			print("List Students\n")
			print("=> {}".format(students))
			srcStd = input("Enter Student Name To Search: ")
			if(srcStd in listStd): #This Condition Searching The Student
				print("\n=> Record Found Of Student {}".format(srcStd))
			else:
				print("\n=> No Record Found Of Student {}".format(srcStd)) #Error Message

	elif(userInput == 4): #This Option Will Remove Student From The List
		rmStd = input("Enter Student Name To Remove: ")
		if(rmStd in listStd): #This Condition Removing The Student From The List 
			listStd.remove(rmStd)
			print("\n=> Student {} Successfully Deleted \n".format(rmStd))
			for students in listStd:
				print("=> {}".format(students))
		else:
			print("\n=> No Record Found of This Student {}".format(rmStd)) #Error Message
	elif(userInput == 5):
		rnStd = input("Enter Student Name To Rename ")
		if(rnStd in listStd):
			listStd.rename(rnStd)
			print("\n=> Student Student {} Successfully Renamed \n".format(rnStd))
			for students in listStd:
				print("=> {}".format(students))
	elif(userInput < 1 or userInput > 5): #Validating User Option
		print("Please Enter Valid Option \'(1-4)\'")	#Error Message	
	else:
		print("Something went wrong")					
manageStudent()



def runAgain(): #Making Runable Problem1353
	runAgn = input("\nwant To Run Again Y/N: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageStudent()
		runAgain()
	else:
		quit(bye) #Print GoodBye Message And Exit The Program
runAgain()
if(platform.system() == "Windows"):
	store=open("C:\\Student\\students_name.txt",'w')
	store.write(ListStd)
	Print("DONE")
else:
	store=open("home\\Student\\students_name.txt",'w')
	store.write(ListStd)
	Print("DONE")		
res = dict(zip( range(1, len(listStd)+1)),listStd) 
  
# print result 
print("The Dictionary after index keys : " + str(res))
