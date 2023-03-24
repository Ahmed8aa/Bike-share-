import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES=['chicago','washington','new york city']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
   
    while True :
        city=input('Please select city (chicago, new york city, washington) : \n').lower().strip()
        if city in CITIES:
           break
        else:
           print('wrong choice! please choose one of the cities between brackets\n') 

    # get user input for month (all, january, february, ... , june)
    month=input('Please select month(all, january, february, ... , june) :\n').lower().strip()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Please select day of the week(all, monday, tuesday, ... sunday) : \n").lower().strip()


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
    #creating panda DataFrame from the selected city
    df=pd.read_csv(CITY_DATA[city])
    
    #convert the Start Time column to datetime format
    df['Start Time']=pd.to_datetime(df['Start Time']) 

    #extracting month and day of the week from Start Time
    df['month']=df['Start Time'].dt.month             
    df['day']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour

    #filter by month
    if month !="all":
        MONTHS=['january', 'february', 'march', 'april', 'may', 'june']
        month=MONTHS.index(month) + 1

        df = df[ df['month'] == month ]


    #filter by day
    if day!="all":
        df=df[df['day']==day.title()]    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month 
    print('Most Frequent Month Of Travel Is : \n',df['month'].mode()[0])


    # display the most common day of week
    print('Most Frequent day Of Travel Is : \n',df['day'].mode()[0])


    # display the most common start hour
    print('Most Frequent hour Of Travel Is : \n',df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most Common Start Station IS : \n",df['Start Station'].mode()[0])


    # display most commonly used end station
    print("Most Common End Station IS : \n",df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    print('Most Frequent Combination Of Start Station And End Station Is:\n',df.groupby(['Start Station','End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time Is :\n',df['Trip Duration'].sum())


    # display mean travel time
    print('Mean Travel Time Is :\n',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts OF Users Type Is:\n',df['User Type'].value_counts())


    # Display counts of gender
    if 'Gender' in df.columns:
        print('Counts OF Gender Type Is:\n',df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest Year Of Birth Is :\n',df["Birth Year"].min())
        print('Most Recent Of Birth Is :\n',df["Birth Year"].max())
        print('Most Common Year Of Birth Is :\n',df["Birth Year"].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
