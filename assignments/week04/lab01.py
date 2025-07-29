"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Nawaphat", 19, "Chonburi", "Thailand")  # name, age, city, country
    hobbies = []
    
    while True :
        choiec(input("Please select (1.dissplay info 2.add hobbies 3.remove hobbies 4.edit age 5.exit)"))
        # Your code here
        if choice == "1":
         # dissplay info    
         print("Name: ", person(0))
         print("Age : ",person(1))
         print("City : ",person(2))
         print("Country :",person(3))
         print("Hobbies :",hobbies)

        elif choice == "2":
         # add hobies
         hobby = input("What is your hobby ? :")
         hobbies.append(hobby)
        elif choice == "3":
         # remove hobbies
         del hobbies(0)

        elif choice == "4":
         # edit age
         person_list = list(person)
         age = int(input("Hoe ole are you? :"))
         person_list[1] = 35
         person = tuple(person_list)
        
        elif choice == "5":
         break 

if __name__ == "__main__":
    personal_info_manager()
