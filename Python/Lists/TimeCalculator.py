
from imaplib import ParseFlags


is_running=True

while is_running:
    print ('''Time Calculator:
   1 - Add 2 times
   2 - Find the difference between 2 times
   3 - Convert to Hours
   4 - Convert to Minutes
   5 - Convert Minutes to Time
   6 - Convert Hours to Time
   7 - Convert Days to Time
   8 - Exit''')
    user_input=input('Please select an input: ')
    if user_input=='1': # Add 2 times
        time_1=input('Please input time 1 (DD:HH:MM): ')
        time_2=input('Please input time 2 (DD:HH:MM): ')
        time_1=time_1.split(':')
        time_2=time_2.split(':')

        day_1,day_2=int(time_1[0]),int(time_2[0])
        hour_1,hour_2=int(time_1[1]),int(time_2[1])
        minute_1,minute_2=int(time_1[2]),int(time_2[2])

        total_minute=minute_1+minute_2
        new_minute=total_minute%60
        remaining_minute=total_minute//60

        total_hour=hour_1+hour_2+remaining_minute
        new_hour=total_hour%24
        remaining_hour=total_hour//24

        new_day=day_1+day_2+remaining_hour
        print (new_day,':',new_hour,':',new_minute)
    elif user_input=='2': # Find the difference between 2 times
        time_1=input('Please input time 1 (DD:HH:MM): ')
        time_2=input('Please input time 2 (DD:HH:MM): ')
        time_1=time_1.split(':')
        time_2=time_2.split(':')

        day_1,day_2=int(time_1[0]),int(time_2[0])
        hour_1,hour_2=int(time_1[1]),int(time_2[1])
        minute_1,minute_2=int(time_1[2]),int(time_2[2])

        day_diff=abs(day_1-day_2)
        hour_diff=abs(hour_1-hour_2)
        minute_diff=abs(minute_1-minute_2)

        minute_diff=minute_1+minute_2
        new_minute=minute_diff%60
        remaining_minute=minute_diff//60

        hour_diff=hour_1+hour_2+remaining_minute
        new_hour=hour_diff%24
        remaining_hour=hour_diff//24

        new_day=day_diff+remaining_hour
        print (new_day,':',new_hour,':',new_minute)

    elif user_input=='3': # Convert to Hours
        pass
    elif user_input=='4': # Convert to Minutes
        pass
    elif user_input=='5': # Convert to Minutes to Time
        pass
    elif user_input=='6': # Convert Hours to Time
        pass
    elif user_input=='7': #Convert Days to Time
        pass
    else:
        is_running=False


