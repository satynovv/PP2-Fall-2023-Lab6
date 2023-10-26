from datetime import datetime
date1 = input()
date2 = input()
date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date1, date_format)
date2 = datetime.strptime(date2, date_format)
time_difference = (date2 - date1).total_seconds()
print(time_difference)
