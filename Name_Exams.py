# Names and Exams 
print("Student exam Averages")
print("\n")
i = input("Would you like to Start the program? (yes/no): ").lower()
usr = 0
while i == "yes":
 name = input("Please enter your last name: ")
 test_1 = float(input("Enter test score 1: "))
 test_2 = float(input("Enter test score 2: "))
 avg_test = (test_1 + test_2) / 2
 print(f"Name: {name} Average Score: {avg_test}")
 if i != "no":
  usr += 1
  print(f"User count: {usr}")
  again = input("would you like to run program again? (yes/no)").lower()
  if again == "no":
    exit()

    #User enters name and test scores
    #Average score is then calculated from test score