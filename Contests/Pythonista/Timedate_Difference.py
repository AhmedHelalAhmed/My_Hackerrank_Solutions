from datetime import datetime # To use datetime functions
for x in range(int(input())):
    a = input() # Timestamps are taken in as strings
    b = input()
    at = datetime.strptime(a,"%a %d %b %Y %H:%M:%S %z")# striptime function parses string and converts it into datetime object
    bt = datetime.strptime(b,"%a %d %b %Y %H:%M:%S %z")
	'''%a maps to abbrevation of day of week(WWW format)
	   %d maps to day (DD format)
	   %b maps to abbrevation of month (MMM format)
	   %Y maps to year(with century YYYY format)
	   %H maps to hour
	   %M maps to minute
	   %S maps to second (I think there is a general format %T for time %H:%M:%S)
	   %z maps to timezone(+/-HHMM format)'''
    di = abs(at - bt)
    print(di.days*24*3600 + di.seconds)
