import time

# used to delay code running


def delay(num):
    """
    Delays python interpreter from executing the next line for a specified amount of seconds

    Parameters
    ------------
    num -- int 
        represents the amount of seconds to delay for
    """
    
    init = time.perf_counter()
    while True:
        now = time.perf_counter()
        if now - init >= num:
            break

# checks that usersname or password are in the database


def accountValidator(file, data, val, marker="."):
    """
    Checks if an admins username or password is in the database

    Parameters
    ------------
    file -- file 
        Serves as the data containing admin's information

    data -- string 
        Serves as an admins inputted username or password

    val -- string 
        serves as data to be replaced

    
    Optional Parameters
    ---------------
    marker -- string 
        Serves as a delimeter. That is, it tell the function when to stop extracting

    Returns
    ------------
    int
        0  If the data failed the validation test
        1  If the data passed the validation test
    """
    
    valid = 0
    for line in file.readlines():
        line = line.replace(f"{val}: ", "#")
        pd = line[line.find(
            "#") + 1: line.find(marker, line.find("#"))]

        if (data == pd):
            file.close()
            valid = 1
    return valid


# calculates day of the month


def findDayMonth(date):
    """
    Extracts a day and month from an admins query

    Parameters
    ------------
    data -- string 
        Serves as the admin's inputted query.  

        
    Returns
    ------------
    day -- int
        Serves as a day of the month
    month -- string
        Serves as a month
    """

    day = int(date[(date.find(",") - 2): date.find(",")])
    month = date[(date.find(f"{day}") - (4 if len(str(day))
                  == 2 else 5)): (date.find(f"{day}") - (1 if len(str(day)) == 2 else 2))]
    return day, month

# extracts date, month, and year from a user's data


def extractDateDetails(data):
    """
    Extracts the day, month, and year from a line of data in the form of a string

    Parameters
    ------------
    data -- string 
        Serves as a line of data from the database


    Returns
    ------------
    tuple
        The tuple contains 3 elements: an int serving as the day, a string serving as the month, and another string serving as the year.
    """

    #obtains day
    data = data.replace(f"DATE: ", "#")
    day = int(data[(
        data.find(",", data.find("#")) - 2): data.find(",", data.find("#"))])

    # obtains month
    month = data[(
        data.find(f"{day}", data.find("#")) - (4 if len(str(day)) == 2 else 5)): (data.find(f"{day}", data.find("#")) - (1 if len(str(day)) == 2 else 2))]

    # obtains year
    year = data[data.find('.', data.find(
        "#")) - 4: data.find('.', data.find("#"))]

    return (day, month, year)

# extracts weekday


def extractWeekday(data):
    """
    Extracts the day of the week that a trip was made from a line of data

    Parameters
    ------------
    data -- file 
        Serves as a line of data from the database

    Returns
    ------------
    day -- string
        Serves as the day of the week
    """

    data = data.replace(f"DATE: ", "#")
    day = data[data.find("#") + 1: data.find("#") + 4]
    return day





