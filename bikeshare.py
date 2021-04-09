import time
import pandas as pd
import numpy as np

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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
    print('*****INSTRUCTIONS!!!!******\nYou will be prompted to enter the city name , month and day for which you need the data to be extracted and calculated \nPlease give the needed inputs as requested ')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Please Enter the City Name CHI for Chicago , NY for New York and WA for Washington ")
    print( color.RED +"City:"+ color.END)
    x = False
    Input_city = input().upper()
    if Input_city not in ("NY" , "CHI" , "WA"):
        x = True
    while x: 
        print(" You have entered wrong city !!!\nPlease Enter the City Name CHI for Chicago , NY for New York and WA for Washington ")
        print( color.RED +"City:"+ color.END)
        Input_city = input().upper()
        if Input_city in ("NY" , "CHI" , "WA"):
            x=False
    # TO DO: get user input for month (all, january, february, ... , june)
    print(" Please Enter the Needed Month ...\n JAN for January \n FEB for February \n MAR for March \n APR for APRIL \n MAY for May \n JUN for JUNE \n ALL to select all 6 months ")
    x = False
    print( color.RED +"MONTH:"+ color.END)
    Input_month = input().upper()
    if Input_month not in ("JAN" , "FEB" , "MAR" , "APR" , "MAY" , "JUN" , "ALL"):
        x = True
    while x:
        print(" You have entered wrong Month !!!\n Please Enter JAN , FEB , MAR , APR , MAY , JUN or ALL")
        print( color.RED +"MONTH:"+ color.END)
        Input_month = input().upper()
        if Input_month in ("JAN" , "FEB" , "MAR" , "APR" , "MAY" , "JUN" , "ALL"):
            x = False    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print(" Please Enter the Needed Day ...\n SUN for Sunday \n MON for Monday \n TUE for Tuesday \n WED for Wednesday \n THU for Thursday \n FRI fror Friday \n SAT for Saturday \n ALL to select all weekdays")
    x = False
    print( color.RED +"DAY:"+ color.END)
    Input_day = input().upper()
    if Input_day not in ("SUN" , "MON" , "TUE" , "WED" , "THU" , "FRI" , "SAT" , "ALL"):
        x = True
    while x:
        print(" You have entered wrong Day !!!\n Please Enter SUN , MON , TUE , WED , THU , FRI , SAT or ALL")
        print( color.RED +"DAY:"+ color.END)
        Input_day = input().upper()
        if Input_day in ("SUN" , "MON" , "TUE" , "WED" , "THU" , "FRI" , "SAT" , "ALL"):
            x = False

    # City Mapping Part  
    if Input_city == "NY":
        city = "new york city"
    elif Input_city == "CHI":
        city = "chicago"
    else :
        city = "washington"
        
    # Month Mapping Part 
    if Input_month == "JAN":
        month = "january"
    elif Input_month == "FEB":
        month = "february"   
    elif Input_month == "MAR":
        month = "march"
    elif Input_month == "APR":
        month = "april"
    elif Input_month == "MAY":
        month = "may"
    elif Input_month == "JUN":
        month = "june"
    else :
        month = "all"
        
    # Week Day Mapping Part 
    if Input_day == "SUN":
        day = "sunday"
    elif Input_day == "MON":
        day = "monday"   
    elif Input_day == "TUE":
        day = "tuesday"
    elif Input_day == "WED":
        day = "wednesday"
    elif Input_day == "THU":
        day = "thursday"
    elif Input_day == "FRI":
        day = "friday"
    elif Input_day == "SAT":
        day = "saturday"
    else :
        day = "all"
	
    print('-'*40,"OUTPUT",'-'*40)
    print(color.BLUE +"Data will be collected for city:{} for month:{} and day:{}".format(city.upper(),month.upper(),day.upper()))
    print(color.END)
    print('-'*40)
    return city, month, day
 
def load_data(city, month, day):
    
    filename = CITY_DATA[city]
    #print (filename)
    #print(city)
    df = pd.read_csv(filename)
    
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
        #print(df.count())

      # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    
        #print(df.tail())
       

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print(color.BOLD +'1.Time Statistics'+ color.END)
    print('Calculating The Most Frequent Times of Travel...')
    print('-'*40)
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print(color.GREEN +'Most Popular Start Month:'+ color.END, popular_month)

    # TO DO: display the most common day of week
    
    popular_day = df['day_of_week'].mode()[0]
    print(color.BLUE +'Most Popular Day:'+ color.END, popular_day)

    # TO DO: display the most common start hour

    popular_state_time = df['Start Time'].dt.hour.mode()[0]
    print(color.RED +'Most Popular State hour :'+ color.END , popular_state_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print(color.BOLD +'2.Station/Trip Statistics'+ color.END)
    print('Calculating The Most Popular Stations and Trip...')
    print('-'*40)
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    print(color.GREEN +'Most Popular Start Station and its count \n'+ color.END , df['Start Station'].value_counts().head(1)
         )

    # TO DO: display most commonly used end station
    
    
    print(color.BLUE +'Most Popular End Station and its count \n'+ color.END ,df['End Station'].value_counts().head(1))
    
    # TO DO: display most frequent combination of start station and end station trip

    print(color.RED +'Most Popular Start_End Stations and its count \n'+ color.END, df.groupby(['Start Station'])['End Station'].value_counts().head(1))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print(color.BOLD +'3.Trip Durtaion Statistics in seconds '+ color.END)
    print('Calculating Trip Duration...')
    print('-'*40)
    
    start_time = time.time()

    # TO DO: display total travel time

    print(color.BLUE +"Total Travel Time :"+ color.END , df['Trip Duration'].sum())
    

    # TO DO: display mean travel time

    print(color.RED +"Average Travel Time :"+ color.END ,df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print(color.BOLD +'4.User Statistics'+ color.END)
    print('Calculating User Stats...')
    print('-'*40)
    
    start_time = time.time()

    # TO DO: Display counts of user types

    
    print (color.RED +"User Types count :\n"+ color.END , df['User Type'].value_counts())

    if city != "washington":
        # TO DO: Display counts of gender
        print (color.BLUE +"User Gender count :\n"+ color.END , df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print (color.GREEN +"Oldest Birth Year :"+ color.END, df['Birth Year'].min())
        print (color.PURPLE +"Youngest Birth Year :"+ color.END , df['Birth Year'].max())
        print (color.YELLOW +"Common Birth Year : "+ color.END, df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(city):
    
    '''
    This function will be showing the raw data as extracted from the csv file for the selected city regardless the selected day
    and month by iterating on the data frame with chunksize = 10 , so end user will be shown 5 columns per time till he selects to
    exit the function 
    '''
    try:
        for chunk in pd.read_csv(CITY_DATA[city], chunksize = 10):
            print(chunk)
            show_raw = input('Press any key to show the next 5 results and to stop Press (s)top:\n').lower()
            if show_raw == 's' or show_raw == 'stop':
                break
    except KeyboardInterrupt:
        print ("")   


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if month == "all" and day == "all":
            time_stats(df)
        else :
            print (color.RED+"N.B. Time Statistics are meaningless for the requested month/day combination ... Skipping it"+ color.END)
            
        station_stats(df)
        trip_duration_stats(df)
        
        if city == "washington":
            print( color.RED +"N.B. : Gender and Birth Year Statistics are not avaiable for washington "+ color.END)
        user_stats(df,city)
        
        print(color.PURPLE +"Do you need to check the raw data for {} city... Press y or Y".format(city))
        print(color.END)
        answer = input()
        if answer == 'y' or answer == 'Y':
            print ('*****{} RAW DATA *******'.format(city.upper()))
            display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks .... Have a great Day !!')
            break


if __name__ == "__main__":
	main()
