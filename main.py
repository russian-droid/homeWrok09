#from hackerrank.com
#https://www.hackerrank.com/challenges/30-nested-logic/problem

dueDay=int(input("Enter Scheduled DAY (format from 01 to 31):\n\t"))
dueMonth=int(input("Enter Scheduled MONTH (format from 01 to 12):\n\t"))
dueYear=int(input("Enter Scheduled YEAR (format from 1900 to 3000):\n\t"))

actualDay=int(input("Enter Actual DAY (format from 01 to 31):\n\t"))
actualMonth=int(input("Enter Actual MONTH (format from 01 to 12):\n\t"))
actualYear=int(input("Enter Actual YEAR (format from 1900 to 3000):\n\t"))

print('THE DUE DATE:', dueDay,dueMonth,dueYear)
print('RETURNED ON:', actualDay,actualMonth,actualYear)

if actualYear > dueYear:
    fine = 10000
    print('Your calculated fine is:', fine, 'hackos')
else:
    if actualMonth > dueMonth:
        fine = (actualMonth - dueMonth) * 500
        print('Your calculated fine is:', fine, 'hackos')
    else:
        if actualDay > dueDay:
            fine = (actualDay - dueDay) * 15
            print('Your calculated fine is:', fine, 'hackos')
        else:
            fine = 0
            print('Thanks for returning your books on time')
            
