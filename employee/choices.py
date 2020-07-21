import datetime

YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
EMAIL_SENDER = "duetInventory@duet.ac.bd"

GENDER = (
        ('m', 'Male'),
        ('f', 'Female')
    )

EMPLOYEE_CATEGORY = (
        ('t', 'Teacher'),
        ('o', 'Officer'),
        ('s', 'Stuff')
    )

DEPARTMENT_TYPE = (
        ('ac' , "Academic"),
        ('ad', 'Administrative')
    )
PAYMENT_TYPE = (
        ('y', 'Yearly'),
        ('hy', 'Half Yearly'),
        ('m', 'Monthly'),
        ('o', 'One Time')
    )

EMPLOYEE_CLASS = (
        ('fi', 'First Class'),
        ('se', 'Second Class'),
        ('th', 'Third Class'),
        ('fo', 'Fourth Class')
    )

REPORT_TYPE = (
    ('d', 'Details'),
    ('s', 'Summary'),
    )


