from datetime import datetime, timedelta
import re

def clndate(date,date_formats):
    try:
        
        result = re.search(r"^[A-Za-z]+\s\d{1,2},\s\d{4},\s\d{2}:\d{2}\s[A-Z]{2}", date).group()
        for date_format in date_formats:
            try:
                date_object = datetime.strptime(result, date_format)    
                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                # print(new_date_string)   # to remove date
                return new_date_string
            except:
                pass

    except:
        pass

def date_formating(date_string):
    date_formats = [ '%Y-%m-%d %H:%M:%S', '%Y-%m-%d','%m-%d-%Y', '%Y/%m/%d,%H:%M:%S', '%d-%m-%Y','%d-%m-%Y,%H:%M:%S','%m-%d-%Y,%H:%M:%S', '%d-%m-%Y %H:%M:%S', '%B %d, %Y, %I:%M %p', '%b %d, %Y, %I:%M %p', '%Y%m%dT%H%M%S.%fZ', '%Y%m%dT%H%M%S.%f%z', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%S.%f%z', '%Y-%m-%dT%H:%M:%S.%f', '%Y/%m/%d', '%d.%m.%Y', '%d.%m.%Y %H:%M:%S', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%y %H:%M:%S', '%d/%m/%y %H:%M', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %I:%M:%S %p', '%m/%d/%Y %I:%M %p', '%m/%d/%y %I:%M:%S %p', '%m/%d/%y %I:%M %p', '%d %B %Y', '%d %b %Y', '%d %B %y', '%d %b %y', '%d,%m,%Y,%I:%M %p', '%m,%d,%Y,%I:%M:%S %p', '%Y,%m,%d,%H:%M:%S', '%m,%d,%y,%I:%M:%S %p', '%d,%b,%Y,%I:%M %p', '%d/%m/%Y %H:%M:%S.%f', '%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%S.%f%z','%m-%d-%Y, %I:%M %p','%Y-%m-%dT%H:%M:%S+00:00','%Y-%m-%dT%H:%M:%S','%Y-%m-%dT%H:%MZ','%Y-%m-%dT%H:%M:%S+0000','%Y-%m-%dT%H:%M:%S+01:00','%Y-%m-%dT%H:%M:%S+0100','%Y-%m-%dT%H:%M:%S+0200','%Y-%m-%dT%H:%M:%S+0300','%Y-%m-%dT%H:%M:%S+0400','%Y-%m-%dT%H:%M:%S+0500','%Y-%m-%dT%H:%M:%S+0600','%Y-%m-%dT%H:%M:%S+0700','%Y-%m-%dT%H:%M:%S+0800','%Y-%m-%dT%H:%M:%S+0900','%Y-%m-%dT%H:%M:%S+01:00','%Y-%m-%dT%H:%M:%S+02:00','%Y-%m-%dT%H:%M:%S+03:00','%Y-%m-%dT%H:%M:%S+04:00','%Y-%m-%dT%H:%M:%S+05:00','%Y-%m-%dT%H:%M:%S+06:00','%Y-%m-%dT%H:%M:%S+07:00','%Y-%m-%dT%H:%M:%S+08:00','%Y-%m-%dT%H:%M:%S+09:00','%m-%d-%Y, %H:%M %p','%Y-%m-%dT%H:%M:%S-0100','%Y-%m-%dT%H:%M:%S-0200','%Y-%m-%dT%H:%M:%S-0300','%Y-%m-%dT%H:%M:%S-0400','%Y-%m-%dT%H:%M:%S-0500','%Y-%m-%dT%H:%M:%S-0600','%Y-%m-%dT%H:%M:%S-0700','%Y-%m-%dT%H:%M:%S-0800','%Y-%m-%dT%H:%M:%S-0900','%M/%d/%Y']


    for date_format in date_formats:
        try:
            date_object = datetime.strptime(date_string, date_format)
            new_format="%Y-%m-%d %H:%M:%S"
            new_date_string = date_object.strftime(new_format)
            return new_date_string
        except :
            try:
                new_date_string = clndate(date_string,date_formats)
                if new_date_string:
                    return new_date_string
            except:
                pass  
                        
            #Yesterday
            try:      
                match = re.search("(\d+) yesterday", date_string) or re.search("(\d+) Yesterday", date_string) or re.search("(\d+) yest", date_string) or re.search("(\d+) Yest", date_string) or re.search("yesterday", date_string) or re.search("Yes", date_string)or re.search("YES", date_string)or re.search("yes", date_string)
                if match:
                    day = 1
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(days=day)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
            # Today
            try:      
                match = re.search("(\d+) today", date_string) or re.search("(\d+) Today", date_string) or re.search("(\d+) tod", date_string) or re.search("(\d+) Tod", date_string) or re.search("today", date_string) or re.search("Tod", date_string)or re.search("TOD", date_string)or re.search("tod", date_string)
                if match:
                    day = 1
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass

            #Today with hrs
            try:      
                match = re.search("(\d+) hours", date_string) or re.search("(\d+) Hours", date_string) or re.search("(\d+) hrs", date_string) or re.search("(\d+) Hrs", date_string) or re.search("(\d+) hrs.", date_string) or re.search("(\d+) Hrs.", date_string) or re.search("Today,(\d+) hours", date_string) or re.search("Today,(\d+) Hours", date_string) or re.search("Today,(\d+) hrs", date_string) or re.search("Today,(\d+) Hrs", date_string) or re.search("Today,(\d+) hrs.", date_string) or re.search("Today,(\d+) Hrs.", date_string)  or re.search("today,(\d+) hours", date_string) or re.search("today,(\d+) Hours", date_string) or re.search("today,(\d+) hrs", date_string) or re.search("today,(\d+) Hrs", date_string) or re.search("today,(\d+) hrs.", date_string) or re.search("today,(\d+) Hrs.", date_string)
                if match:
                    hours = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(hours=hours)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass        

            # 1 HOURS AGO
            try:      
                match = re.search("(\d+) HOURS AGO", date_string) or  re.search("(\d+) HOUR AGO", date_string) or re.search("(\d+) Hours Ago", date_string) or re.search("(\d+) Hours", date_string) or re.search("(\d+) hrs ago", date_string) or re.search("(\d+) HRS AGO", date_string) or re.search("(\d+) hou", date_string) or re.search("(\d+) HO", date_string) or re.search("(\d+) Ho", date_string)
                if match:
                    hours = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(hours=hours)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
            #Days (25 Days ago)
            try:      
                match = re.search("(\d+) days", date_string) or re.search("(\d+) Days", date_string) or re.search("(\d+) DAY", date_string) or re.search("(\d+) day", date_string) or re.search("(\d+) Day", date_string) or re.search("(\d+) days ago", date_string) or re.search("(\d+) Days ago", date_string) or re.search("(\d+) DAY AGO", date_string) or re.search("(\d+) day ago", date_string) or re.search("(\d+) Day Ago", date_string) 
                if match:
                    days = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(days=days)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
            
            #Months (25 months ago)
            try:      
                match = re.search("(\d+) month", date_string) or re.search("(\d+) Month", date_string) or re.search("(\d+) months ago", date_string) or re.search("(\d+) Months", date_string) 
                if match:
                    months= int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(30*months)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
                               
            # today with minutes              
            try:      
                match = re.search("(\d+) minutes", date_string) or re.search("(\d+) Minutes", date_string) or re.search("(\d+) min", date_string) or re.search("(\d+) Min", date_string) or re.search("(\d+) min.", date_string) or re.search("(\d+) Min.", date_string) or re.search("Today,(\d+) minutes", date_string) or re.search("Today,(\d+) Minutes", date_string) or re.search("Today,(\d+) min", date_string) or re.search("Today,(\d+) Min", date_string) or re.search("Today,(\d+) min.", date_string) or re.search("Today,(\d+) Min.", date_string)  or re.search("today,(\d+) minutes", date_string) or re.search("today,(\d+) Minutes", date_string) or re.search("today,(\d+) min", date_string) or re.search("today,(\d+) Min", date_string) or re.search("today,(\d+) min.", date_string) or re.search("today,(\d+) Min.", date_string)
                if match:
                    minutes = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(minutes=minutes)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
            
            # Seconds ago
            try:      
                match = re.search("(\d+) seconds", date_string) or re.search("(\d+) Seconds", date_string) or re.search("(\d+) sec", date_string) or re.search("(\d+) Sec", date_string) or re.search("(\d+) sec.", date_string) or re.search("(\d+) Sec.", date_string)
                if match:
                    second = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(seconds=second)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
            
            # year ago
            try:      
                match = re.search("(\d+) year", date_string) or re.search("(\d+) Year", date_string) or re.search("(\d+) yrs", date_string) or re.search("(\d+) Yrs", date_string) or re.search("(\d+) yrs.", date_string) or re.search("(\d+) Yrs.", date_string)
                if match:
                    years = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(365*years)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
            
            # week ago
            try:      
                match = re.search("(\d+) week", date_string) or re.search("(\d+) Week", date_string) or re.search("(\d+) weeks", date_string) or re.search("(\d+) Weeks", date_string) 
                if match:
                    week = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(7*week)

                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
            
            # sunday, 11pm
            try: 
                day_pattern = r'(mon|tue|wed|thu|fri|sat|sun|Mon|Tue|Wed|Thu|Fri|Sat|Sun)day'  
                time_pattern = r'(\d{1,2})(am|pm)' 

                match = re.match(f'{day_pattern},{time_pattern}', date_string) or re.match(f'{day_pattern}, {time_pattern}', date_string) or re.match(f'{day_pattern} ,{time_pattern}', date_string)
                day_of_week = match.group(1)
                hour = int(match.group(2))
                if match.group(3) == 'pm':
                    hour += 12


                now = datetime.now()
                days_until_next_day_of_week = (7 - now.weekday() + ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun' ,'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ].index(day_of_week)) % -7
                next_day_of_week = now + timedelta(days=days_until_next_day_of_week)

                final_datetime = next_day_of_week.replace(hour=hour, minute=0, second=0)
                final_string = final_datetime.strftime('%Y-%m-%d %H:%M:%S')

                return final_string  
                
            except:
                pass   

            # "Sep 6,2022"
            try:
                date_pattern = r'(\w{3})\s+(\d{1,2}),(\d{4})'

                match = re.match(date_pattern, date_string)
                year = int(match.group(3))
                month = match.group(1)
                day = int(match.group(2))
                dt = datetime(year, datetime.strptime(month, '%b').month, day, 0, 0, 0)

                final_string = dt.strftime('%Y-%m-%d %H:%M:%S')
                return final_string

            except:
                pass  

            try:
                date_pattern =r'(\d+)(?:st|nd|rd|th)\s+(\w+)\s+(\d+),\s+(\d+):(\d+)\s+(AM|PM)'

                match = re.match(date_pattern, date_string)
                day_str, month_str, year_str, hour_str, minute_str, am_pm_str = match.groups()

                day_int = int(day_str)
                year_int = int(year_str)

                month_num = datetime.datetime.strptime(month_str, '%B').month

                if am_pm_str == 'PM' and hour_str != '12':
                    hour_int = int(hour_str) + 12
                elif am_pm_str == 'AM' and hour_str == '12':
                    hour_int = 0
                else:
                    hour_int = int(hour_str)

                datetime_obj = datetime.datetime(year_int, month_num, day_int, hour_int, int(minute_str))

                formatted_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
                return formatted_str
  

            except:
                pass    

            # January 29, 2023, 04:14
            try:
                if(date_pattern ==r'(\w+?)\s+(\d{1,2}),\s*(\d{4}),\s*(\d{2}):(\d{2})'):
                    
                    date_pattern =r'(\w+?)\s+(\d{1,2}),\s*(\d{4}),\s*(\d{2}):(\d{2})'

                    match = re.match(date_pattern, date_string)
                    year = int(match.group(3))
                    month = match.group(1)
                    day = int(match.group(2))
                    hour = int(match.group(4))
                    minute = int(match.group(5))
                    
                    dt = datetime(year, datetime.strptime(month, '%B').month, day, hour, minute, 0)

                    final_string = dt.strftime('%Y-%m-%d %H:%M:%S')
                    return final_string
                else:
                    date_pattern = r'(\w+?)\s+(\d{1,2})'

                    match = re.match(date_pattern, date_string)
                    month = match.group(1)
                    day = int(match.group(2))

                    year = datetime.now().year

                    dt = datetime(year, datetime.strptime(month, '%B').month, day, 0, 0, 0)

                    final_string = dt.strftime('%Y-%m-%d %H:%M:%S')
                    return final_string
            except:
                pass   
            
            try:
                input_regex = r'(\d{2})-(\d{2})-(\d{4}),\s+(\d{2}):(\d{2})\s+(AM|PM)'

                # input_str = '09-21-2009, 06:36 PM'
                match = re.match(input_regex, date_string)

                month_str, day_str, year_str, hour_str, minute_str, am_pm_str = match.groups()

                year_int = int(year_str)
                month_int = int(month_str)
                day_int = int(day_str)

                if am_pm_str == 'PM' and hour_str != '12':
                    hour_int = int(hour_str) + 12
                elif am_pm_str == 'AM' and hour_str == '12':
                    hour_int = 0
                else:
                    hour_int = int(hour_str)

                datetime_obj = datetime.datetime(year_int, month_int, day_int, hour_int, int(minute_str))
                formatted_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
                return formatted_str
            except:
                pass  
            # 27th May 2021, 05:23 AM    
            try:
                pattern = r"(\d+)(st|nd|rd|th) (\w+) (\d{4}), (\d{1,2}):(\d{2}) ([AP]M)"

                match = re.search(pattern, date_string)
                day = match.group(1)
                month = match.group(3)
                year = match.group(4)
                hour = int(match.group(5))
                minute = match.group(6)
                ampm = match.group(7)
                if ampm == "PM" and hour != 12:
                    hour += 12
                elif ampm == "AM" and hour == 12:
                    hour = 0

                date_obj = datetime.strptime(f"{day} {month} {year} {hour}:{minute}", "%d %B %Y %H:%M")

                formatted_date_str = datetime.strftime(date_obj, "%Y-%m-%d %H:%M:%S")
                return formatted_date_str
            except:
                pass
            #  25 May, 2020 - 10:43 AM
            try:
                pattern = r"(\d+) (\w+), (\d{4}) - (\d{1,2}):(\d{2}) ([AP]M)"

                match = re.search(pattern, date_string)
                day = match.group(1)
                month = match.group(2)
                year = match.group(3)
                hour = int(match.group(4))
                minute = match.group(5)
                ampm = match.group(6)

                if ampm == "PM" and hour != 12:
                    hour += 12
                elif ampm == "AM" and hour == 12:
                    hour = 0
                date_obj = datetime.strptime(f"{day} {month} {year} {hour}:{minute}", "%d %B %Y %H:%M")
                formatted_date_str = datetime.strftime(date_obj, "%Y-%m-%d %H:%M:%S")
                return formatted_date_str
            
            except:
                pass

            # Nov 7, 2021 at 11:25 PM
            try:
                datetime_pattern = r'(\w{3})\s+(\d{1,2}),\s*(\d{4})\s+at\s+(\d{1,2}):(\d{2})\s*(AM|PM)'

                match = re.match(datetime_pattern, date_string)
                year = int(match.group(3))
                month = match.group(1)
                day = int(match.group(2))
                hour = int(match.group(4))
                minute = int(match.group(5))
                ampm = match.group(6)
                if ampm == 'PM' and hour != 12:
                    hour += 12
                elif ampm == 'AM' and hour == 12:
                    hour = 0
                dt = datetime(year, datetime.strptime(month, '%b').month, day, hour, minute, 0)
                final_string = dt.strftime('%Y-%m-%d %H:%M:%S')
                return final_string

            except:
                pass  

            try:

                time_pattern = r'(\d{1,2}):(\d{2})\s*(AM|PM)'
                match = re.match(time_pattern,date_string)
                hour = int(match.group(1))
                minute = int(match.group(2))
                ampm = match.group(3)
                if ampm == 'PM' and hour != 12:
                    hour += 12
                elif ampm == 'AM' and hour == 12:
                    hour = 0
                now = datetime.now()
                dt = datetime(now.year, now.month, now.day, hour, minute, 0)
                final_string = dt.strftime('%Y-%m-%d %H:%M:%S')
                return final_string

            except:
                pass 
            
            # Sep 24 2021 21:53:04
            try:
                pattern = r'([a-zA-Z]{3}\s\d{1,2}\s\d{4})\s(\d{2}:\d{2}:\d{2})'
                match = re.match(pattern, date_string)
                date_str = match.group(1)
                time_str = match.group(2)
                dt = datetime.strptime(date_str + ' ' + time_str, '%b %d %Y %H:%M:%S')
                print(dt)
                final_string = dt.strftime('%Y-%m-%d %H:%M:%S')
                print(final_string)   
                
                return final_string
            except:
                pass    
                

def date_coverter(input_date):
    try:
        d=int(input_date)
        return d
    except:
        if(input_date.find('post')):

            try:
                filter_input =input_date.split(' (')
                output = date_formating(filter_input[0])
                dt = datetime.strptime(output, "%Y-%m-%d %H:%M:%S")
                timestamp = int(dt.timestamp())
                return timestamp
            except:
                
                try:
                    
                
                    filter_input_1 =input_date.split(': ')
                    filter_input_2 =filter_input_1[1].split(' by')[0]
                    output = date_formating(filter_input_2)
                    # print(output)
                    dt = datetime.strptime(output, "%Y-%m-%d %H:%M:%S")
                    timestamp = int(dt.timestamp())
                    return timestamp
                except:
                    return input_date
                    #ct = datetime.datetime.now()
                    #ts = ct.timestamp()
                    #ts=int(ts)
                    #date=ts 
                    #return date              
        else: 
            try:

                output = date_formating(input_date)
                # print(output)
                dt = datetime.strptime(output, "%Y-%m-%d %H:%M:%S")
                print(dt)
                timestamp = int(dt.timestamp())
                return timestamp
            except:
                return input_date
                #ct = datetime.datetime.now()
                #ts = ct.timestamp()
                #ts=int(ts)
                #date=ts 
                #return date

# print(date_coverter("2/14/2023")) #add input
# print(date_coverter("May 20 2021 10:04:31")) #add input