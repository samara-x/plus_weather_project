import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

#use function challenge also 

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    #use unicode for degree symbol
    #DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"
    
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """   
#https://www.geeksforgeeks.org/python/python-strftime-function/
#from datetime import datetime << This is already imported at the top
    dt = datetime.fromisoformat(iso_string)
    convert_date = dt.strftime("%A %d %B %Y")
    return convert_date



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(celsius,1)
#print(convert_f_to_c(77)) #USE THIS FOR TESTING PURPOSES



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    #for the variable name in weather data list

#sum function help from here: https://www.programiz.com/python-programming/methods/built-in/sum
    total = 0
    for each_number in weather_data:
        #print(each_number)
        total = total + float(each_number)
    #get mean by dividing sum by length of list
    mean = total/len(weather_data)
    return mean
#weather_data = [51,50.1,49.5,48.2,47.8]
#print(f"mean temp {calculate_mean(weather_data)}")
#GOOGLE HOW TO SUM EVERYTHING IN LIST


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    # Opening the file to read from
    with open(csv_file) as file: #load the data and go to the csv file csv_file in a function
        reader = csv.reader(file)  # 2. Set up our reader
        next(reader) # 3. ignore the header line and just look at data
        for row in reader: # 4. for each row in our file...
            if row: # 5 skip empty rows
            # update the types of our data turning numbers into int.
                updated_row = [row[0],int(row[1]),int(row[2])]
                data.append(updated_row)
    return data
#csv help from here: https://docs.python.org/3/library/csv.html
#use CSV reader as used in todays class 


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

#get list of numbers 
    if not weather_data:
        return ()
    min_value = float(weather_data[0])
    min_position = 0

    for i in range (1, len(weather_data)):
        value = float(weather_data[i])
        if value <= min_value:
            min_value = value
            min_position = i

    return (min_value, min_position)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:       #if somehting is not a number or empty then skip by returning ()
        return ()
    max_value = float(weather_data[0])
    max_position = 0

    for i in range (1, len(weather_data)):
        value = float(weather_data[i])
        if value >= max_value:
            max_value = value
            max_position = i
            
    return (max_value, max_position)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
#look at generate summary
#how to handle multiple lines f string: use. /n"
#5 Day Overview.   << number of days in weather data "Day Overview" use len
#  The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#  The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#  The average low this week is 12.2°C.
#  The average high this week is 17.8°C.
    
    #if not weather_data: #if len of weather_date is. 0 return
        #return "0 Day Overview"
    #for weather_data

    if len(weather_data) == 0:
        return

    num_days = len(weather_data)
    dates = [row[0] for row in weather_data]
    min_temps = [row[1] for row in weather_data] 
    max_temps = [row[2] for row in weather_data]

    # Get min and max results
    min_result = find_min(min_temps)
    max_result = find_max(max_temps)
    if not min_result or not max_result:
        return

    min_temp, min_index = min_result #data that we can work with
    max_temp, max_index = max_result #data that we can work with

    min_date = convert_date(dates[min_index])
    max_date = convert_date(dates[max_index])
    avg_low = calculate_mean(min_temps)
    avg_high = calculate_mean(max_temps)
    #put everything into a list the use for loop 
    #then convert using for loop

#    celcius_temps = []
#    all_temps = [min_temp, max_temp, avg_high, avg_low]
#    for i in all_temps:
#        celcius = convert_f_to_c(i)
#        celcius_temps.append(celcius)
#4,43,29,7

#[0]
#use index number to format        
#need to format above results

#    summary = (
#        f"{num_days} Day Overview\n"
#        f"  The lowest temperature will be {celcius_temps[0]:}, and will occur on {min_date}.\n"
#        f"  The highest temperature will be {celcius_temps[1]:}, and will occur on {max_date}.\n"
#        f"  The average low this week is {celcius_temps[3]:}.\n"
#        f"  The average high this week is {celcius_temps[2]:}."
#    )

    summary = (cl
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {min_temp:}, and will occur on {min_date}.\n"
        f"  The highest temperature will be {max_temp:}, and will occur on {max_date}.\n"
        f"  The average low this week is {avg_low:}.\n"
        f"  The average high this week is {avg_high:}."
    )
    print(summary)
    #return summary



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
#---- Friday 02 July 2021 ----
#Minimum Temperature: 9.4°C
#Maximum Temperature: 19.4°C
