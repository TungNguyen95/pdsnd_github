import time
import pandas as pd
import numpy as np
import statistics

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
    city, month, day = "", "", ""
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        selectionCity = input("Would you like to see data for Chicago, New York City or Washington?\n")
        if selectionCity.lower() in ('chicago', 'new york city', 'washington'):
            city = selectionCity.lower()
            break
        else:
            print('Invalid input please try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        selectionMonth = input("Which month? January, February, March, April, May, June or All?\n")
        if selectionMonth.lower() in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            month = selectionMonth.lower()
            break
        else:
            print('Invalid input please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        selectionDay = input("Which day? Monday, Tuesday, ... Sunday, or All?\n")
        if selectionDay.lower() in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            day = selectionDay.lower()
            break
        else:
            print('Invalid input please try again')

    print('-'*60)
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

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

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_use_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_use_start_station)

    # TO DO: display most commonly used end station
    popular_used_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_combination'] = df['Start Station'] + ' -> ' + df['End Station']
    frequent_combination = df['frequent_combination'].mode()[0]
    print('Most frequent combination of start station and end station trip:', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = statistics.mean(df['Trip Duration'])
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = min(df['Birth Year'])
        print('Earliest year of birth', earliest_birth)
    except:
        pass
        
    try:
        most_recent_birth = max(df['Birth Year'])
        print('Most recent year of birth', most_recent_birth)
    except:
        pass

    try:
        most_common_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth', most_common_birth)
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)

def get_raw_data(df):
    """Display raw data upon request by the user."""

    index = 0
    while True:
        show_data = input("Do you want to see 5 lines of raw data?\n")
        if show_data.lower() == 'yes':
            print(df[index:index+5])
            index += 5
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
        get_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
