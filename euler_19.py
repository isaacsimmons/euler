import sys
import math
import datetime

def listDays(start, end):
    numDays = (end - start).days
    dateList = [ start + datetime.timedelta(days=x) for x in range(0, numDays) ]
    return dateList

def countSunday1st(days):
    count = 0
    for day in days:
        if day.day == 1 and day.isoweekday() == 7:
            count += 1
    return count

def main(argv):
    print("RETURN ", countSunday1st(listDays(datetime.date(day=1, month=1, year=1901), datetime.date(day=1, month=1, year=2001))))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
