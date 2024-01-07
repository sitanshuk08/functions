# importing the required libraries
import datetime
from dateutil.relativedelta import relativedelta

# todays datetime
today = datetime.today()

# calculate the same period last year
start_date_lysp = today.replace(day = 1, year = today.year-1)
end_date_lysp = today.replace(day =1, month = (today.month %12 ) + 3, year = today.year - 1 + (today.month // 12)) - timedelta(days=1)

