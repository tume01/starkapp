import datetime
import calendar

class DateManager():

    @classmethod
    def add_months(cls, sourcedate,months):
        
        month = sourcedate.month - 1 + months
        
        year = int(sourcedate.year + month / 12 )
        
        month = month % 12 + 1
        
        day = min(sourcedate.day,calendar.monthrange(year,month)[1])
        
        return datetime.date(year,month,day)
