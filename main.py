import time
from functions import delay, accountValidator, findDayMonth, extractDateDetails, extractWeekday



def errormessage():
    """
    Prints error message
    """
    print()
    print("Error. Incorrect date format. Try again.")


def extracLocationName(data, store_obj, val="CLOSEST SUPERMARKET: "):
    """
    Calculates how many times a location occurs in the database and stores that information in a dictionary

    Parameters
    ------------
    data -- file 
        serves as database

    Optional Parameters
    ---------------
    val -- string 
        Serves as a delimiter. That is, it tell the function where to start extracting

    store_obj -- dict 
        serves as storages for the function's derived information. Its keys are strings of places' names and its values are integers representing the location's number of occurrences.

    """

    data = data.replace(val, "#")
    val = data[data.find("#")+1:data.find('.', data.find("#"))]

    if val in store_obj:
        store_obj[val] += 1
    else:
        store_obj[val] = 1





def avgRateOfTrips(months_of_the_year):
    """
    Calculates the average rate(trips/day) of rides given between two periods and prints out information related to it

    Parameters
    ------------
    months_of_the_year -- dictionary 
        represents the months of the year as keys and their number of days as integer values

    Returns
    ------------
    int
        -1  If an error happenes because of wrong date input
         1  If no error happens
    """
    
    try:
        print()
        print("-------------------------------*")
        first_date = input(
            "Enter a start date:\nDate format: Mon Nov 27, 2023\n")
        second_date = input(
            "Enter an end date: ")

        first_date_day, first_date_month = findDayMonth(first_date)
        second_date_day, second_date_month = findDayMonth(second_date)

        trips_per_day_dict = {}
        day_month_year_array = []
        day_array = []

        data_filter_file = open("data.txt", "r")
        for line in data_filter_file:

            # extracts useful data
            day, month, year = extractDateDetails(line)

            #this branch only runs when it is processung data within the specified time interval 
            if (month == first_date_month and first_date_month != second_date_month and first_date_day <= day <= months_of_the_year[first_date_month]) or (second_date_month == first_date_month and first_date_day <= day <= second_date_day) or (month == second_date_month and 1 <= day <= second_date_day):

                if (month, day, year) not in day_month_year_array:
                    day_month_year_array.append((month, day, year))

                if day not in day_array:
                    day_array.append(day)

                if day in trips_per_day_dict:
                    trips_per_day_dict[day] += 1
                else:
                    trips_per_day_dict[day] = 0
                    trips_per_day_dict[day] += 1

        # calculates avg trips per day
        sum_trips = 0
        for t in trips_per_day_dict.values():
            sum_trips += t
        avg_trips_per_day = sum_trips / \
            len(trips_per_day_dict)

        #FINAL MESSAGE
        print()
        print(
            f"The average rate of trips from {first_date} to {second_date} is {avg_trips_per_day:.2f} trips/day.")
        day_num = 0
        for day_tuple in day_month_year_array:
            day_num += 1
            print(
                f" {day_num}. {day_tuple[0]} {day_tuple[1]}, {day_tuple[2]}: {trips_per_day_dict[day_array[day_num - 1]]} trip(s).")
        delay(0.5)

        return 1
    except:
        return -1


# calculates distance of over two periods

def distOverPeriod():
    """
    Calculates the total distance covered by the companies employees within a given time frame

    Parameters
    ------------
    none 
        

    Returns
    ------------
    sum_distance -- int
        Serves as the total distance covered in the specified period

    sum_rides -- int
        Serves as the total trips made in the specified period

    day_month_year_dist_obj -- dict
        Stores the total distance covered by employees in a particular day. Its keys are tuples of three elements(string, int, and string) and its values are floats that represent distance

    first_date -- string
        Serves as the first day of the time interval

    second_date -- string
        Serves as the last day of the time interval

    """

    try:

        print()
        print("-------------------------------*")
        first_date = input("Enter a start date:\nDate format: Mon Nov 27, 2023\n")
        second_date = input(
            "Enter an end date:\nDate format: Fri Dec  8, 2023\n")


        first_date_day, first_date_month = findDayMonth(
            first_date)
        second_date_day, second_date_month = findDayMonth(
            second_date)

        data_filter_file = open("data.txt", "r")

        sum_distance = 0
        sum_rides = 0
        day_month_year_dist_obj = {}
        for line in data_filter_file:

            day, month, year = extractDateDetails(line)

            # Extract distance
            line = line.replace("DISTANCE TRAVELED: ", "#")
            u_distance = line[(
                line.find('#') + 1):(line.find('. ', line.find('#')))]

            if (month == first_date_month and first_date_month != second_date_month and first_date_day <= day <= months_of_the_year[first_date_month]) or (second_date_month == first_date_month and first_date_day <= day <= second_date_day) or (month == second_date_month and 1 <= day <= second_date_day):

                if u_distance.find("CUSTOMER'S NAME") != -1:
                    u_distance = u_distance
                else:
                    u_distance = float(u_distance)

                if type(u_distance) == type(0.5):
                    #mutable elements cannot be the keys of a dictionary in python
                    if (month, day, year) in day_month_year_dist_obj:
                        day_month_year_dist_obj[(month, day, year)] += u_distance
                    else:
                        day_month_year_dist_obj[(month, day, year)] = u_distance

                    sum_rides += 1
                    sum_distance += u_distance

        return sum_distance, sum_rides, day_month_year_dist_obj, first_date, second_date
    except:
        return 0, 0, 0, 0, 0
    



# //////////////////////////////////////////////////--end


# ///////////////// Main Code
print("Welcome to MappE🗺️")
# delyas for 0.5 seconds
delay(0.5)


admin_tries = 0 #keeps track of login attempts
admin_event_loop = True  # creatws a condition for event loop for logging admins in
print("LOGIN:")

#creates an event loop
while admin_event_loop == True:
    #asks for admins login details
    admins_name = input("username: ").strip()
    admins_password = input("password: ").strip()

    users_login_data = open("admin_login.txt", 'r')
    op = accountValidator(
        users_login_data, admins_password, "PASSWORD")

    users_login_data = open("admin_login.txt", 'r')
    ou = accountValidator(
        users_login_data, admins_name, "USERNAME")
    delay(0.2)

    if (op == 1) and (ou == 1):  #if true, admin is logged in
        print()
        print("-------------------------------*")
        print(f"Welcome, {admins_name if admins_name.find(' ') == -1 else admins_name[: admins_name.find(' ')]}.")

        op = 0
        while True:
            months_of_the_year = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31,
                                "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}
            if op == 0:
                a = ""
            else:
                print()
                print("-------------------------------*")
            choice = input(
                f"What {'else ' if op == 1 else ''}would you like to do today?\nOptions:\n (1)View all travel data stored in our database. (2)Estimate the total number of rides given by our company between two periods.\n (3)View all rides given by our company on a certain date. (4)Estimate the average rate(trips/day) of rides given between two periods.\n (5)Obtain the total distance covered by our drivers between two periods. (6)Obtain the avg distance covered by our drivers between two periods.\n (7)View all trips in our database made on a particular weekday. (8)View all rides made on a particular weekday in a particular month.\n (9)Most visited place. (10)Sort database.\n (11)See top 3 customers. (12)Log out.\n")
            op = 1

            if choice == "1":
                try:
                    print()
                    print("-------------------------------*")
                    v_counter = 0 #serves as numbering. It is used to customise the information displayed to admins
                    print("DATA:")
                    data_base = open("data.txt", 'r')

                    
                    for line in data_base: #loops through file(database)
                        v_counter += 1
                        line = line.replace(line[:line.find(". ") + 2], "#") #customises output
                        line = line.replace(line[:line.find(". ") + 2], "#")

                        print(f"{v_counter}. {line[1:]}", end="")
                    delay(1.1)
                except:
                    errormessage()
                    delay(1)

            elif choice == "2":
                try:
                    print()
                    print("-------------------------------*")
                    first_date = input(
                        "Enter start date:\nDate format: Mon Nov 27, 2023\n")
                    second_date = input(
                        "Enter end date:\nDate format: Fri Dec  8, 2023\n")

                    first_date_day, first_date_month = findDayMonth(
                        first_date)
                    second_date_day, second_date_month = findDayMonth(
                        second_date)

                    data_filter_file = open("data.txt", "r")

                    total_trips = 0
                    for line in data_filter_file:

                        day, month, year = extractDateDetails(line)

                        if (month == first_date_month and first_date_month != second_date_month and first_date_day <= day <= months_of_the_year[first_date_month]) or (second_date_month == first_date_month and first_date_day <= day <= second_date_day) or (month == second_date_month and 1 <= day <= second_date_day):
                            total_trips += 1

                    print()
                    print(
                        f"We gave {total_trips} rides from {first_date} to {second_date}.")
                    
                                       
                    if total_trips > 0:
                        data_filter_file = open("data.txt", "r")
                        v_counter = 0
                        for output_line in data_filter_file:

                            day, month, year = extractDateDetails(output_line)

                            if (month == first_date_month and first_date_month != second_date_month and first_date_day <= day <= months_of_the_year[first_date_month]) or (second_date_month == first_date_month and first_date_day <= day <= second_date_day) or (month == second_date_month and 1 <= day <= second_date_day):

                                v_counter += 1
                                output_line = output_line.replace(output_line[:output_line.find(". ") + 2], "#")
                                output_line = output_line.replace(output_line[:output_line.find(". ") + 2], "#")
                                print(f"{v_counter}. {output_line[1:]}", end="")

                        
                            
                    data_filter_file.close()
                    delay(1.1)

                except:
                    errormessage()
                    delay(1)

            elif choice == "3":
                try:
                    print()
                    print("-------------------------------*")
                    filter_date = input(
                        "Select a date to filter by:\nDate format: Mon Nov 27, 2023\n")

                    data_filter_file = open("data.txt", "r")
                    c_days = 0
                    
                    print()
                    print("DATA:")
                    v_counter = 0
                    for line in data_filter_file:
                        if filter_date in line:
                            c_days = 1
                            v_counter += 1
                            line = line.replace(line[:line.find(". ") + 2], "#")
                            line = line.replace(line[:line.find(". ") + 2], "#")
                            print(f"{v_counter}. {line[1:]}", end="")

                    if c_days == 0:
                        print(f"We gave 0 rides on {filter_date}")

                    data_filter_file.close()
                    
                    delay(1.1)
                except:
                    errormessage()
                    delay(1)

            elif choice == "4":
                errhandler = avgRateOfTrips(months_of_the_year)
                if errhandler == -1:
                    errormessage()

                delay(1)

            elif choice == "5":
                sum_distance, sum_rides, useful_obj, first_date, second_date = distOverPeriod()
                if sum_distance == 0:
                    errormessage()
                    delay(1)
                    continue

                print()
                print(
                    f"The total distance covered from {first_date} to {second_date} is {sum_distance:.4f}KM")
                counter = 0
                for key in useful_obj:
                    counter +=1
                    print(f"{counter}. {key[0]} {key[1]}, {key[2]}: {useful_obj[key]}km")
                delay(1)

            elif choice == "6":
                sum_distance, sum_rides, useful_obj, first_date, second_date = distOverPeriod()
                if sum_distance == 0:
                    errormessage()
                    delay(1)
                    continue
                avg_sum_dist = sum_distance/sum_rides
                print()
                print(
                    f"The distance covered from {first_date} to {second_date} is {avg_sum_dist:.4f}KM")
                counter = 0
                for key in useful_obj:
                    counter +=1
                    print(f"{counter}. {key[0]} {key[1]}, {key[2]}: {(useful_obj[key]):.4f}km")
                delay(1)
            
            elif choice == "7":
                try:
                    print()
                    print("-------------------------------*")

                    d_count = 0
                    f_day = input("Enter a day:\nformat: Monday or Mon\n")

                    ab_day = f_day[:3]

                    data_filter_file = open("data.txt", "r")

                    print()
                    print("RIDES:")
                    for line in data_filter_file:
                        day, month, year = extractDateDetails(line)
                        weekday = extractWeekday(line)

                        if ab_day.lower() == weekday.lower():
                            d_count += 1
            

                    print(
                        f"{d_count}trip(s) were/was made on {f_day.lower()}.")
                    
                    data_filter_file = open("data.txt", "r")
                    v_counter = 0
                    for line in data_filter_file:
                            day, month, year = extractDateDetails(line)
                            weekday = extractWeekday(line)

                            if ab_day.lower() == weekday.lower():
                                v_counter += 1
                                line = line.replace(line[:line.find(". ") + 2], "#")
                                line = line.replace(line[:line.find(". ") + 2], "#")
                                print(f"{v_counter}. {line[1:]}", end="")
                    
                    data_filter_file.close()

                    delay(1.1)
                except:
                    errormessage()
                    delay(1)


            elif choice == "8":
                try:
                    print()
                    print("-------------------------------*")

                    d_count = 0
                    f_month = input("Enter a month:\nMonth format: January or Jan\n")

                    f_day = input("Enter a day:\nDay format: Monday or Mon\n")

                    ab_month = f_month[:3]
                    ab_day = f_day[:3]

                    data_filter_file = open("data.txt", "r")

                    print()
                    print("TRIPS:")
                    for line in data_filter_file:
                        day, month, year = extractDateDetails(line)
                        weekday = extractWeekday(line)

                        if ab_month.lower() == month.lower() and ab_day.lower() == weekday.lower():
                            d_count += 1
            

                    print(
                        f"{d_count}trip(s) were/was made on {f_day.lower()} in {f_month.lower()}.")
                    
                    data_filter_file = open("data.txt", "r")
                    v_counter = 0
                    for line in data_filter_file:
                            day, month, year = extractDateDetails(line)
                            weekday = extractWeekday(line)

                            if ab_month.lower() == month.lower() and ab_day.lower() == weekday.lower():
                                v_counter += 1
                                line = line.replace(line[:line.find(". ") + 2], "#")
                                line = line.replace(line[:line.find(". ") + 2], "#")
                                print(f"{v_counter}. {line[1:]}", end="")
                    
                    data_filter_file.close()
                    delay(1.1)

                except:
                    errormessage()
                    delay(1)
                
            elif choice == "9":
                try: 
                    print()
                    print("-------------------------------*")
                    data_filter_file = open("data.txt", "r")

                    store_obj = {}
                    mv_store = 0
                    mv_store_value = 0

                    for line in data_filter_file:
                        extracLocationName(line, store_obj)

                    for key, val in store_obj.items():
                        if val > mv_store_value:
                            mv_store_value = val
                            mv_store = key

                    print("INFO:")
                    print(
                        f"The most frequented place is {mv_store}. It was visited {mv_store_value} times.")
                    delay(1.1)
                except:
                    errormessage()
                    delay(1)
                
            elif choice == "10":
                try: 
                    print("-------------------------------*")
                    print()
                    data_output = ""
                    out_arr = []
                    sort_coice = input(
                        "Enter A to sort database's content in an ascending order of dates.\nEnter D to sort database's content in a descending order of dates.\n").lower()
                    print()
                    print("DATABASE:")
                    if sort_coice == "a":
                        num_i = 0
                        f = open("data.txt", "r")
                        for el in f:
                            num_i += 1
                            el = el.replace(el[:el.find(". ") + 2], "#")
                            el = el.replace(el[:el.find(". ") + 2], "#")
                            print(f"{num_i}: {el[1:]}", end="")

                    else:
                        f = open("data.txt", "r")
                        for line in f:
                            out_arr.append(line)

                        out_arr.reverse()

                        for index, el in enumerate(out_arr):
                            el = el.replace(el[:el.find(". ") + 2], "#")
                            el = el.replace(el[:el.find(". ") + 2], "#")

                            data_output += f"{index+1}: {el[1:]}"
                        print(data_output)
                    delay(1.1)
                except:
                    errormessage()
                    delay(1)
            elif choice == "11":
                try: 
                    print()
                    print("-------------------------------*")
                    data_filter_file = open("data.txt", "r")

                    customers_obj = {}
                    customer_trips_array = []
                    for line in data_filter_file:
                        extracLocationName(line, customers_obj, "CUSTOMER'S NAME: ")

                    for key in customers_obj:
                        if customers_obj[key] not in customer_trips_array:
                            customer_trips_array.append(customers_obj[key])
                    customer_trips_array.sort()

                    first_place_val = customer_trips_array.pop()
                    if len(customer_trips_array) > 0:
                        second_place_val= customer_trips_array.pop()
                    if len(customer_trips_array) > 0:
                        third_place_val= customer_trips_array.pop()

                    first_place = []
                    second_place= []
                    third_place= []
                    for key in customers_obj:
                        if customers_obj[key] == first_place_val:
                            first_place.append(key)
                        elif customers_obj[key] == second_place_val:
                            second_place.append(key)
                        elif customers_obj[key] == third_place_val:
                            second_place.append(key)
                    
                    print()
                    print("TOP CUSTOMERS:")
                    fp_names = ""
                    if len(first_place) > 0:
                        fp_names = "(1) "
                        for name in first_place:
                            if name == first_place[-1]:
                                fp_names += f"{name}.\n"
                            else:
                                fp_names += f"{name}, "
                    else:
                        print("We have no data in our database")

                    sp_names = ""
                    if len(second_place) > 0:
                        sp_names = "(2) "
                        for name in second_place:
                            if name == second_place[-1]:
                                sp_names += f"{name}.\n"
                            else:
                                sp_names += f"{name}, "

                    tp_names = ""
                    if len(third_place) > 0:
                        tp_names = "(3) "
                        for name in third_place:
                            if name == third_place[-1]:
                                tp_names += f"{name}.\n"
                            else:
                                tp_names += f"{name}, "

                    print(fp_names,sp_names, tp_names)
                    delay(1.1)

                except:
                    errormessage()
                    delay(1)

            elif choice == "12":
                print(f"See you later, {admins_name if admins_name.find(' ') == -1 else admins_name[: admins_name.find(' ')]}.")
                admin_event_loop = False
                delay(0.5)
                

                break
            else:
                print(f"We have no operation for {choice}.")
                delay(1)
                

    # Break cannot be used in functions
    else:
        admin_tries += 1
        #terminates program after 5 failed attempts to login
        if admin_tries == 5:
            
            print(
                f"You've tried the maximum number({admin_tries}) of times.\nPlease, re-run our application to try again.")
            break
        print("Incorrect username or password. Try again.")

