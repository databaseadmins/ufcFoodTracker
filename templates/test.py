from datetime import datetime

date = '2017-05-28'
database_date = datetime.strptime(date, "%Y-%m-%d")
print(database_date)
print(type(database_date))
final_database_date = datetime.strftime(database_date, "%Y%m%d")
print(final_database_date)