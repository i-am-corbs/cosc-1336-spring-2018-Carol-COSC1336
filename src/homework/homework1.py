def get_hours_since_midnight(seconds):
    '''
    Type the code to calculate total hours given n(number) of seconds
    For example, given 3800 seconds the total hours is 1
    '''
    return
#get a number of seconds since midnight from the user
get_hours_since_midnight = float(input('Enter total number of seconds since midnight: '))
#determine the number of hours
hours = get_hours_since_midnight // 3600
print('Hours:', hours)

'''
IF YOU ARE OK WITH A GRADE OF 70 FOR THIS ASSIGNMENT STOP HERE.
'''

def get_minutes(seconds):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 3
    '''
    return
#determine the number of minutes
mins = (get_hours_since_midnight % 3600) // 60
print('Minutes:', mins)

def get_seconds(seconds):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 20
    '''
    return
#determine the number of seconds
secs = (get_hours_since_midnight % 3600) % 60
print('Seconds:', secs)
