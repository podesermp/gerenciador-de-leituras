from library.user.user import userAddReading
from datetime import datetime

# print(userAddReading())


date = datetime.today().strftime('%d-%m-%Y')
print(date.replace('-', '.'))