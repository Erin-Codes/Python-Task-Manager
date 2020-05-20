import csv

print("\t\t\t\t\t\t\t\t\tL O G I N")

fl = open("user.txt", "r+")

rfl = fl.read()

user = input("Enter your username:\n")

password = input("Enter your password (case sensitive):\n")

while user.lower() not in rfl:
    print("This username does not exist, please try again.")
    user = input("\n\nEnter your username:\n")
    password = input("Enter your password (case sensitive):\n")
    

fl.close()


def get_pair(line):
    key, sep, val = line.strip().partition(", ")
    return key, val
# Defining a function that takes one value as an argument(a line) and returns the key and the value for that line.


with open('user.txt') as ffl:
    d = dict(get_pair(line) for line in ffl)
# Returning the key and value for every line in 'user.txt' and using the dict() constructor to convert these lines to a
# dictionary.

try:
    while password != d[user]:
        print("The password entered is incorrect,check and try again.\n\n")
        # user = input("\n\nEnter your username:\n")
        password = input("Enter your password (case sensitive):\n")
        # A loop to check that each username can only login with its corresponding password in 'user.txt'
       
except KeyError:
    print("\nINVALID USERNAME / PASSWORD\n(CHECK THAT YOU HAVE NOT SWAPPED THE TWO)")
    exit(0)

print("\n\n Welcome! \n\n")

while True:
    choice_1 = "g"
# A loop containing most of the programs code that breaks out of the loop if the user does not want to return
# to the main menu.

    if user == "admin":
        # Provides only 'admin' with the stats and register option in the menu.
        print("Please select one of the following options:\n "
              "r - register user\n "
              "a - add task\n "
              "va - view all tasks\n "
              "vm - view my tasks\n "
              "ds - display statistics\n "
              "gr - generate reports\n "
              "e - exit\n")

    else:
        print("Please select one of the following options:\n "
              "a - add task\n "
              "va - view all tasks\n "
              "vm - view my tasks\n "
              "e - exit\n")

    option = input(":\t")

    if option.lower() == "r":
        register = input("Enter new username:\n")
        # Prompts user for a new username.

        while register.lower() in rfl:
            print("A user with this username already exists ,please try a different username.")
            register = input("Enter new username:\n")
        # Prints out an error and prompts user again.

        if register.lower() not in rfl:
            def reg_user(new_user):
                fl = open('user.txt', 'r+')
                rfl = fl.read()                
                new_pass1 = input("Enter a password for this user:\n")
                new_pass2 = input("Confirm the above password:\n")

                while new_pass2 != new_pass1:
                    print("\n\n Your passwords do not match, please check and try again. \n")       
                    new_pass2 = input("Confirm the above password:\n")

                fl.write('\n' + str(new_user.lower()) + ", " + new_pass2)

                user_count = 0

                for line in fl:
                    user_count += line
            
            fl.close()     
            # Defining a function that registers a user,writes the users details to a file and
            # adds one to the user count.

        reg_user(register)

    elif option.lower() == "a":
        def add_task(add):
            title = input("Enter the title of this task:\n")       
            desc = input("Enter a task description:\n")        
            from datetime import date                                  
            today = str(date.today())                                  
            due = input("Enter the tasks due date:\n")
            fl = open('tasks.txt', 'r+')
            rfl = fl.read()

            task_num = 0
            for line in rfl.split("\n")[::8]:  # Converting 'rfl' to a list of lines using '.split()' and
                                               # iterating over every every 8th line by slicing (list[start:stop:step]).
                task_num += 1
                # Counting the amount of tasks by iterating every 8 lines.

            import pandas as pd

            dictt = {'Assigned to': task_user,
                     'Task number': str(task_num),
                     'Task': title,
                     'Description of task': desc,
                     'Task Due date': str(due),
                     'Date assigned': today,
                     'Complete': "No"}
            
            with open('mycsv.csv', 'a') as fd:
                w = csv.writer(fd)
                w.writerow(dictt.values())

            fl.write("\nAssigned to:\t\t" + task_user+   ""
                     "\nTask Number:\t\t" + str(task_num) +
                     "\nTask:\t\t\t" + title +
                     "\nDescription of task:\t"+desc +
                     "\nDate assigned:\t\t" + today +
                     "\nTASK"+str(task_num) +
                     "\nDue date:\t" + str(due) +
                     "\nTask" + str(task_num) +
                     "\nComplete?:\t"+"No" + "\n\n")
            fl.close()
        # Defining a function that adds a task to a specific user by writing it to the 'tasks.txt' file.

        task_user = input("Enter the user that this task will be assigned to:\n")
        task = add_task(task_user)
                                            
    elif option.lower() == "va":                            
        def view_all():
            fl = open("tasks.txt", "r+")
            rfl = fl.read()    
            print(rfl)   
            fl.close()
        # Defining a function that prints all tasks.

        view_all()

    elif option.lower() == "e":                             
        exit(0)

    elif option.lower() == "gr": # For option 'gr'
        def gr():
            if user != "admin":
                print("Invalid option.")
            # Checks that only admin users have access to 'gr'
                
            def counter(text):
                with open('tasks.txt', 'r') as fl:
                    rfl = fl.read()
                    count = rfl.count(text)

                    if count > 0:
                        return count
                    else:
                        return float("0.1")
                # Defining a function that takes a str as an argument and returns the amount of
                # occurrences of that string in 'tasks.txt'.

            def count1(text):
                count = not_com().count(text)
                if count > 0:
                    return count
                else:
                    return 0
            # Defining a function that takes a str as an argument and returns the amount of
            # occurrences of that string in 'not_com()'.

            def count2(text):
                count = com().count(text)
                if count > 0 :
                    return count
                else:
                    return 0
            # Defining a function that takes a str as an argument and returns the amount of
            # occurrences of that string in 'com()'.

            def count3(text):
                count =  sub().count(text)
                if count > 0 :
                    return count
                else:
                    return 0
            # Defining a function that takes a str as an argument and returns the amount of
            # occurrences of that string in 'sub()'.
            
            compl = counter("Yes")
            uncomp = counter("No")
            total = compl + uncomp

            percent = (uncomp/total) * 100
            # Percentage of incomplete tasks.
           
            from datetime import datetime
            from datetime import date
            
            def sub():
                
                with open('mycsv.csv') as pfl:
                    myData = csv.reader(pfl)
                    result = ""
                    for row in myData:
                        if "No" in row:
                            d = datetime.strptime(row[4], '%Y-%m-%d')
                            datelist = [d]
                            for j in datelist:
                                d1 = datetime.strptime(str(date.today()), '%Y-%m-%d')
                                if d < d1:
                                    result += row[0]+'\n'
                    
                return result
            # Defining a function that returns the user names if that users task is incomplete and overdue.
            # sub()

            def sub2():
                with open('mycsv.csv') as pfl:
                    myData = csv.reader(pfl)
                    result = 0
                    for row in myData:
                        if "No" in row:
                            d = datetime.strptime(row[4], '%Y-%m-%d')
                            datelist = [d]
                            for j in datelist:
                                d1 = datetime.strptime(str(date.today()), '%Y-%m-%d')
                                if d < d1:
                                    result += 1
                    
                return result
            # Defines a function that counts the amount of incomplete and overdue tasks.

            with open('task_overview.txt', 'w') as fl:
                fl.write("Total tasks generated:\t" + str(compl+uncomp)
                         + "\nNumber of completed tasks:\t"+str(compl)
                         + "\nNumber of incomplete tasks:\t"+str(uncomp)
                         + "\nNot completed and overdue:\t"+str(sub2())
                         + "\ntasks that are incomplete and overdue:\t"+str(sub2()/total * 100))
            # Writes information to 'task_overview'
                
            def user_amount():   
                with open('user.txt') as fl:
                    u_count = 0
                    for line in fl:
                        u_count += 1
                return u_count
            # Counts the amount of registered users.

            def not_com():
                with open("mycsv.csv") as pfl:
                    myData = csv.reader(pfl)
                    jet = ""
                    for row in myData:
                        if "No" in row:
                            jet += str(row[0]+'\n')
                return jet
            # Returns users with incomplete tasks.
            
            def com():
                with open("mycsv.csv") as pfl:
                    myData = csv.reader(pfl)
                    jet = ""
                    for row in myData:
                        if "Yes" in row:
                            jet += str(row[0] + '\n')
                return jet
            # Returns users with completed tasks.
            
            def up():
                with open('user_overview.txt', 'w') as tl:
                    tl.write("Total number of users:\t"+str(user_amount())+"\nTotal tasks generated:\t"+str(compl+uncomp) +'\n')

                with open('user.txt') as ufl:
                        names = ""
                        taskss = ""
                        for line in ufl:
                            names += str(line).split(", ", 1)[0]+'\n'

                        with open('user_names.txt', 'w') as nfl:                
                            nfl.write(names)

                        with open('user_names.txt', 'r') as fl, open('user_overview.txt', 'a') as zfl:
                            for line in fl:
                                val = line
                                zfl.write('\n'+val.replace('\n', '')+":\t" + str(counter(val)).replace('0.1', '0')
                                          + " tasks in total\n" + "\t"+str(counter(val)/total * 100).replace('0.1', '0') + "% of total tasks\n"
                                          + "\tPercentage of users incomplete tasks\t" + str(count1(val)/counter(val) * 100) + '%'
                                          + '\n'"\tPercentage of users complete tasks\t"+str((count2(val)/counter(val) * 100))+ '%'
                                          + '\n' + "\tUsers incomplete and overdue tasks:\t"+str(count3(val)/counter(val))+"%\n")

            # Writes data to 'user_overview.txt'
            up()
     
        gr()

    elif option.lower() == "ds":         # For 's'.
        def gr():
            if user != "admin":
                print("Invalid option.")
            # Checks that only admin users have access to 'gr'
                
            def counter(text):
                with open('tasks.txt', 'r') as fl:
                    rfl = fl.read()
                    count = rfl.count(text)

                    if count > 0:
                        return count
                    else:
                        return float("0.1")
                # Defining a function that takes a str as an argument and returns the amount of
                # occurrences of that string in 'tasks.txt'.

            def count1(text):
                count = not_com().count(text)
                if count > 0:
                    return count
                else:
                    return 0
            # Defining a function that takes a str as an argument and returns the amount of
            # occurrences of that string in 'not_com()'.

            def count2(text):
                count = com().count(text)
                if count > 0:
                    return count
                else:
                    return 0
            # Defining a function that takes a str as an argument and returns the amount of
            # occurrences of that string in 'com()'.

            def count3(text):
                count = sub().count(text)
                if count > 0:
                    return count
                else:
                    return 0
            # Defining a function that takes a str as an argument and returns the amount of
            # occurrences of that string in 'sub()'.

            compl = counter("Yes")
            uncomp = counter("No")
            total = compl + uncomp

            percent = (uncomp/total) * 100
            # Percentage of incomplete tasks.

            from datetime import datetime
            from datetime import date
            
            def sub():
                
                with open('mycsv.csv') as pfl:
                    myData = csv.reader(pfl)
                    result=""
                    for row in myData:
                        if "No" in row:
                            d = datetime.strptime(row[4], '%Y-%m-%d')
                            datelist = [d]
                            for j in datelist:
                                d1 = datetime.strptime(str(date.today()), '%Y-%m-%d')
                                if d < d1:
                                    result += row[0]+'\n'
                    
                return result
            # Defining a function that returns the usernames if that users task is incomplete and overdue.
            # sub()

            def sub2():
                with open('mycsv.csv') as pfl:
                    myData = csv.reader(pfl)
                    result = 0
                    for row in myData:
                        if "No" in row:
                            d = datetime.strptime(row[4], '%Y-%m-%d')
                            datelist = [d]
                            for j in datelist:
                                d1 = datetime.strptime(str(date.today()), '%Y-%m-%d')
                                if d < d1:
                                    result += 1
                    
                return result
            # Defines a function that counts the amount of incomplete and overdue tasks.

            with open('task_overview.txt', 'w') as fl:
                fl.write("Total tasks generated:\t" + str(compl+uncomp)
                         + "\nNumber of completed tasks:\t" + str(compl)
                         + "\nNumber of incomplete tasks:\t" + str(uncomp)
                         + "\nNot completed and overdue:\t" + str(sub2())
                         + "\ntasks that are incomplete and overdue:\t" + str(sub2()/total * 100))
            # Writes information to 'task_overview'
                
            def user_amount():   
                with open('user.txt') as fl:
                    u_count = 0
                    for line in fl:
                        u_count += 1
                return u_count
            # Counts the amount of registered users.

            def not_com():
                with open("mycsv.csv") as pfl:
                    myData = csv.reader(pfl)
                    jet = ""
                    for row in myData:
                        if "No" in row:
                            jet += str(row[0]+'\n')
                return jet
            # Returns users with incomplete tasks.
            
            def com():
                with open("mycsv.csv") as pfl:
                    myData = csv.reader(pfl)
                    jet = ""
                    for row in myData:
                        if "Yes" in row:
                            jet += str(row[0] + '\n')
                return jet
            # Returns users with completed tasks.
            
            def up():
                with open('user_overview.txt', 'w') as tl:
                    tl.write("Total number of users:\t"+str(user_amount())
                             + "\nTotal tasks generated:\t"+str(compl+uncomp)
                             + "\n")

                with open('user.txt') as ufl:
                        names = ""
                        taskss = ""
                        for line in ufl:
                            names += str(line).split(", ", 1)[0]+'\n'

                        with open('user_names.txt', 'w') as nfl:                
                            nfl.write(names)

                        with open('user_names.txt', 'r') as fl, open('user_overview.txt', 'a') as zfl:
                            for line in fl:
                                val = line
                                zfl.write('\n'+val.replace('\n', '')+":\t" + str(counter(val)).replace('0.1', '0')+" tasks in total\n"
                                          + "\t"+str(counter(val)/total * 100).replace('0.1', '0')+"% of total tasks\n"
                                          + "\tPercentage of users incomplete tasks\t"+str(count1(val)/counter(val) * 100)+'%'
                                          + '\n'"\tPercentage of users complete tasks\t"+str((count2(val)/counter(val) * 100))+'%'
                                          + '\n'+"\tUsers incomplete and overdue tasks:\t"+str(count3(val)/counter(val))+"%\n")

            # Writes data to 'user_overview.txt'
            up()
     
        gr()
        
        if user == 'admin':
        
            with open('user.txt') as fl:
        
                line_count = 0
        
                for i in fl:
        
                    line_count += 1
        
                    users = line_count -1
        
            print("Total number of registered users:\t" ,users)
        
            fl.close()
         # Since each user in "user.txt" is on a new line the for loop counts each line then
         # subtracts 1 (to exclude empty lines),ultimately counting the amount of users.

            with open('tasks.txt', 'r+') as fl:
        
                task_count = 0
        
                for line in fl:
        
                    if "Task:" in line:
        
                        task_count += 1
        
            print("Total number of tasks:\t", task_count, "\n\n")
        
            fl.close()                
        # Since each task contains the string "Task:"  the for loop counts every line that contains
        # the specified string,ultimately counting each task.

            with open("task_overview.txt", "r") as fl,open('user_overview.txt', 'r') as ffl:
                rfl =  fl.read()
                rrfl = ffl.read()
                print('\n\n')
                print('TASK OVERVIEW:\n\n')
                print(rfl)
                print('\n\n\n')
                print('USER OVERVIEW')
                print(rrfl)

    elif option.lower() == "vm":                           
        
        with open('tasks.txt') as fl:                       
            for line in fl:

                if user.lower() in line:                

                    for i in range(7):
                        after_line = next(fl)
                        print(after_line.strip('\n'))
        fl.close()

        print("\n\n\n")
        print("Choose an option:\n  "
              "s - Select Task\n \n  "
              "-1 - Return to main menu\n\n")

        choice_1 = input(":")
        # Displays available options and prompts user for input.

        if choice_1.lower() == "s":
            print("Select task by its Task Number ONLY:\t\n")
            task_num = input("")
            # Prints an instruction and propmts user for input.
                
            fl = open('tasks.txt')
                # Opens file.
                
            for line in fl:
                if "Task Number:\t\t" + task_num in line:
                    for i in range(6):
                        after_line = next(fl)
                        print(after_line.strip("\n"))
                    # Searches through the file for a line containing the specific string and prints
                    # the next 6 lines thereafter, ultimately displaying the task info.
            fl.close()

                
                
            print("\n\n\n")
            print("Choose an option:\n"
                  "m - Mark task as complete\n \n"
                  "e - Edit the task\n\n")
            choice_2 = input(":")
                # Displays options.

            if choice_2.lower() != "m" and choice_2.lower() != "e":
                while choice_2.lower() != "m" and choice_2.lower() != "e":
                    print("You have not entered a valid option,try again.")
                    print("Choose an option:\nm - Mark task as complete\n \ne - Edit the task\n\n")
                    choice_2 = input(":")
                    # Prints error and displays menu again.9

            if choice_2.lower() == "m":
                import pandas as pd

                with open('tasks.txt','r') as fl:
                    old_data = fl.read()
                    get_lines = fl.readlines()
                    # Opens file in read mode and converts file into a string.

                if str(task_num) in old_data or "No" in old_data:
                    old_data = old_data.replace("\nTask" + str(task_num) +" Complete?:\tNo","\nTask" + str(task_num) +" Complete?:\tYes")
                    # Searches for specific characters in the string and replaces the given characters in that same line.

                with open('tasks.txt','w') as fl:
                    fl.write(old_data)
                    # Writes the variable 'old data' to the same file.
                    # Ultimately changing "No" to "Yes".

                import pandas as pd

                df = pd.read_csv('mycsv.csv')
                # Reading the csv file into pandas dataframe.
                
                df.iloc[int(task_num)-1,6] = "Yes"
                # Finding the row/column index and changing it to "Yes"

                df.to_csv('mycsv.csv',index=False)
                # Exporting the changed dataframe to the csv file.

            elif choice_2.lower() == "e":
                with open('tasks.txt', 'r') as fl:
                    old_data = fl.read()
                    
                    if "\nTask" + str(task_num) + " Complete?:\tNo" in old_data:     # Statement for if task is not been marked as complete.
                        print("This task has not been completed.\n\tUNABLE TO EDIT\n\n")
                        edit = "none"

                    elif "\nTask" + str(task_num) +" Complete?:\tYes" in old_data:    # Statement for if task has been marked as complete.
                        print("\n\n\te - Edit to who the task is assigned to.\n\n\td - Edit the tasks  due date.\n\n")
                        edit = input("\n:")

                    else:
                        edit = "none"
                    # Printing options and propting user for input.

                        
                with open('tasks.txt') as fl:
                    for num, line in enumerate(fl, 1):
                        if "TASK"+str(task_num) in line:
                            line_num = num
                # Returning the line number for the specified line.

                line_num = line_num

                if edit.lower() == "none":
                    print()

                if edit.lower() != "e" and edit.lower() != "d" and edit.lower() != "none":
                    while edit.lower() != "e" and edit.lower() != "d":
                        print("Invaild option,try again.")
                        edit = input("\n:")
                # Displaying an error and prompting user again.

                if edit.lower() == "e":
                    new_name = input("\nEnter to who this task must be assigned to:\n\t")
                    old_data = old_data.replace("\nAssigned to:\t\t" + user,"\nAssigned to:\t\t" + new_name)
                    with open('tasks.txt','w') as fl:
                        fl.write(old_data)
                # Replacing the user that the task is assigned to with 'new_name'.

                with open('tasks.txt','r') as fl:
                    data = fl.readlines()
                if edit.lower() == "d":
                    print("PLEASE ENTER THE DATE IN THE FOLLOWING FORMAT:\n2020-03-16\n\n")
                    new_assign = input("\nEnter the due date for this task:\n\t")
                    data[line_num-1] =  "TASK"+str(task_num) + ", Due date:\t" + new_assign+"\n"
                    
                    with open('tasks.txt', 'w') as fl:
                        fl.writelines(data)
                    # Replacing the due date of the task with 'new_assign'
                
            else:
                print()
    else:
        exit(0)

    if choice_1.lower() != "-1":
        break
    # A condition that breaks the menu loop if 'choice_1.lower() != "-1".
