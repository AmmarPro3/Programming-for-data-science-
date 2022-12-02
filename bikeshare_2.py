import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': "C:/Users/ammar/OneDrive/سطح المكتب/programming for data scince/projects/udacity - project2/csv files/chicago.csv",
              'new york city': 'C:/Users/ammar/OneDrive/سطح المكتب/programming for data scince/projects/udacity - project2/csv files/new_york_city.csv',
              'washington': 'C:/Users/ammar/OneDrive/سطح المكتب/programming for data scince/projects/udacity - project2/csv files/washington.csv' }

def input_checker(string_input,inputType):
    """
    check the validity of user input.
    input_str: is the input of the user
    input_type: is the type of input: 1 = city, 2 = month, 3 = day
    """



    while True:
        userInput = input(string_input)
        try:
            if userInput.strip(' ').lower() in ['chicago','new york city','washington'] and inputType == 1:
                break
            elif userInput.strip(' ').lower() in ['january', 'february', 'march', 'april', 'may', 'june','all'] and inputType == 2:
                break
            elif userInput.strip(' ').lower() in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and inputType == 3:
                break
            else:
                if inputType == 1:
                    print("Sorry, your input should be: chicago new york city or washington")
                if inputType == 2:
                    print("Sorry, your input should be: (january, february, march, april, may, june) or all")
                if inputType == 3:
                    print("Sorry, your input should be: sunday, ... friday, saturday or all")
        except ValueError:
            print("Sorry, your input is wrong")

    return userInput.strip(' ').lower()


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    city = input_checker('please enter a city, (chicago, new york city, washington)\n',1)
    month = input_checker('please enter a month (january, february, march, april, may, june), or enter all to filter by all months\n',2)
    day = input_checker('please enter a day (sunday, monday, tuesday, wednesday, thursday, friday, saturday), or enter all to filter by all days\n',3)

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

    # extract month, day and hour of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['hour'] = df['Start Time'].dt.hour


    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month is ', df['month'].mode()[0])

    # display the most common day of week
    print('most common day of week is ', df['day_of_week'].mode()[0])

    # display the most common start hour
    print('the most common start hour is ', df['hour'].mode()[0])

    # display the most common time of the day to start
    time_of_day = pd.cut(df['Start Time'], bins=4, labels=('Morning', 'Noon', 'Evening', 'Night'))
    print('the most common time of the day to start is ', df['Start Time'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most commonly used start station is ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('the most commonly used end station is ', df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    col_group = df.groupby(['Start Station', 'End Station'])
    print('most frequent combination of start station and end station trip is \n', col_group.size().sort_values(ascending=False))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('the total travel time is ', df['Trip Duration'].sum())

    # display mean travel time
    print('the mean travel time is ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('the counts of user types are \n', df['User Type'].value_counts())

    # Display counts of gender
    if city != 'washington':

        print('\nthe counts of user types are \n', df['Gender'].value_counts())

        # Display earliest, most recent, and most and least common years of birth
        print('\nthe most recent year of birth is \n',df['Birth Year'].max())
        print('the earliest year of birth is \n', df['Birth Year'].min())
        print('the most common year of berth is \n', df['Birth Year'].mode()[0])
        print('the least common year of berth is \n', df['Birth Year'].value_counts().index[-1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)




        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.strip(' ').lower() != 'yes':
            break


if __name__ == "__main__":
	main()
