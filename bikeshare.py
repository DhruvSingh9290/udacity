import time
import pandas as pd
import numpy as np
import json

"""it means displaying 5 lines of the row from df.
As df.head() would print the first 5 lines of rows from df.

similarly,you should define a display_data function, which should ask the user, " do you want to see raw data?" if user input yes, then it should show 5 lines of raw data. and again it should ask the user "do you want to see more 5 lines of raw data?" if yes user yes then it should again show further 5 line of raw data and this should be continuously going until the user gives input "No".
Hint : use df.iloc()"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!, enter the corresponding number of the item you wish to filter')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    for i in range(len(cities)):
        print(str(i + 1) + ":", cities[i])

    while True:
        city = int(input("Enter a number corresponing to city: "))
        if city in range(1, 4):
            city = cities[city - 1]         
            break
        elif input == 'q':
            break
        else:
            print("Invalid input. Please Select a city.")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "june"]
    for i in range(len(months)):
        
        print(str(i + 1) + ":", months[i])
    while True:
        month = int(input("Enter a number corresponing to the month: "))
        if month in range(1,7):
            month = months[month - 1]         
            break
        elif input == 'q':
            break
        else:
            print("Invalid input. Please Select a valid month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    daysofweek = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for i in range(len(daysofweek)):
        print(str(i + 1) + ":", daysofweek[i])
    while True:
        day = int(input("Enter a number corresponing to day of the week: "))
        if day in range(1, 9):
            day = daysofweek[day - 1]         
            break
        elif input == 'q':
            break
        else:
            print("Invalid input. Please Select a city.")

    print(city,", ", month,", ", day)

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    #Display Line item = litm
    litm = 1

    print(litm,". ",'Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()    
    litm = newmethod909(litm)

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(litm,". ", 'The most common month is: ', common_month)
    litm = newmethod909(litm)

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]

    print(litm,".",'The most common day of week: ', common_day)
    #2
    litm = newmethod909(litm)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print(litm,".","The the most common start hour " + str(popular_hour) + "h")
    litm = newmethod909(litm)

    print(litm,".","This took %s seconds." % (time.time() - start_time))
    #3
    litm = newmethod909(litm)

    print('-'*40)

def newmethod909(litm):
    litm = newmethod550(litm)
    return litm

def newmethod550(litm):
    litm = litm + 1
    return litm
        
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    #Display Line item = litm
    litm = 1
    print(litm,".", 'Calculating The Most Popular Stations and Trip...\n')
    litm = newmethod909(litm)
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print(litm,".", 'The most commonly used start station is: ', popular_start)
    litm = newmethod909(litm)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print(litm,".", 'The commonly used end station is: ', popular_end)
    litm = newmethod909(litm)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + ' and ' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print(litm,".",'The most frequent combination of start station and end station trip is:' , popular_start_end)
    litm = newmethod909(litm)

    print(litm,".","This took %s seconds." % (time.time() - start_time))           
    print("No more station stats available")

    print('-'*40)
        
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    #Display Line item = litm
    litm = 1

    print(litm,".",'Calculating Trip Duration...\n')
    litm = newmethod909(litm)
    start_time = time.time()

    # TO DO: display total travel time
    trip_total = df['Trip Duration'].sum()
    print(litm,".",'The total travel time is: ', trip_total)
    litm = newmethod909(litm)
    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()
    print(litm,".",'The mean travel time is: ', trip_mean)
    litm = newmethod909(litm)

    print(litm,".","This took %s seconds." % (time.time() - start_time))
    litm = newmethod909(litm)
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    litm = 1
    print(litm,".",'Calculating User Stats...\n')
    start_time = time.time()
    litm = newmethod909(litm)

    # TO DO: Display counts of user types
    user_types = pd.value_counts(df['User Type'])
    print(litm,".","User Types: \n", user_types)
    litm = newmethod909(litm)

    try:
        df_Gender_Type = df['Gender'].value_counts()
        print(litm,".",'Gender:\n')
        litm = newmethod909(litm)

        # convert nl presentable
        print('\t' + df_Gender_Type.to_string().replace('\n', '\n\t'))
        litm = newmethod909(litm)

    # If no data provided
    except Exception:
        print("No gender data")
        pass 

    # TO DO: Display earliest, most recent, and most common year of birth
    try:            
        # Display earliest, most recent, and most common year of birth
        birth_earliest = int(df['Birth Year'].min())
        print(litm,".",'The earliest Birth Year is: ', birth_earliest)
        litm = newmethod909(litm)                                                                                                                                                 
        birth_mostrecent = int(df['Birth Year'].max())
        print(litm,".",'The most recent Birth Year is: ', birth_mostrecent)
        litm = newmethod909(litm)
        birth_mostcommon = int(df['Birth Year'].mode())
        print(litm,".",'The most common Birth Year is: ', birth_mostcommon)
        litm = newmethod909(litm)

        # If no data provided
    except Exception:
        print(litm,".","No date of birth data provided")
        litm = newmethod909(litm)
        pass # continue

    print('-'*40)


def display_rawdata(df):
    """Filters raw data."""
    row_depth = df.shape[0]

    # iterate 5 rows deep
    for i in range(0, row_depth, 5):    
        yn = input("Do you want to see raw data? y/n:  ")
        if yn.lower() != "y":
            break
        else:   
        # using df.iloc as suggested df.to_json(filename) | Write to a file in JSON format
            row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
            for row in row_data:                       
                loads_row = json.loads(row)
                dumps_row = json.dumps(loads_row)
                print(dumps_row)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rawdata(df)

        restart = input('\nWould you like to restart? Enter "yes".\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()    