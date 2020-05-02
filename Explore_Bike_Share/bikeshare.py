import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = None
    while True:
        city = input("Choose city between Chicago, New York City, Washington: ").lower()
        if city in cities:
            break
        else:
            print("Not a valid city\n")
            continue
            
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = None
    while True:
        month = input("Choose a month from January to June or 'all': ").lower()
        if month in months:
            break
        else:
            print("Not a valid month\n")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = None
    while True:
        day = input("Choose a day or 'all': ").lower()
        if day in days:
            break
        else:
            print("Not a valid day\n")
            continue

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
#load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
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
        df = df[df['day_of_week'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print("Most common month: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    print("Most popular day of week: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour 
    print("Most common start hour: ", df['hour'].mode()[0]) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    print("Most common start station: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most common end station: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Common Trip'] = df['Start Station'] + ' - ' + df['End Station']
    print("Most common trip: ", df['Common Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Average travel time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types:\n", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns: 
        print("Gender types:\n", df['Gender'].value_counts())
    else: 
        print("There's no information about gender\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of birth: {}'.format(df['Birth Year'].min()))
        print("Most recent year of birth: ", df['Birth Year'].max())
        print("Most common year of birth: ", df['Birth Year'].mode()[0])
    else:
        print("There's no information about birth year\n")
 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """

    count = 0

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        # Check if response is yes, print the raw data and increment count by 5
        if answer == 'yes':
            #print(df.head(count))
            print(df[count:count+5])
            count += 5
        # otherwise break    
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


        
if __name__ == "__main__":
	main()
