from datetime import datetime, timedelta
current_date = datetime.now()
result_date = current_date - timedelta(days=5)
print(current_date.strftime("%Y-%m-%d"))
print(result_date.strftime("%Y-%m-%d"))