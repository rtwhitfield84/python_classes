# Instructions

# Create a class that contains information about employees of a company and define methods to get employee name, job title, and start date.

class Company(object):

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = set()
        
    def getCompany(self):
    	return self.company_name

class Employee:

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def getName(self):
        return self.name

    def getJob(self):
        return self.title

    def startDate(self):
        return self.start_date

if __name__ == '__main__':

    Google = Company("Google")
    richard = Employee("Richard", "Developer", "April 1st, 2017")
    steven = Employee("Steven", "Developer", "April 1st, 2017")
    drew = Employee("Drew", "Developer", "April 1st, 2017")

    Google.employees.add(richard)
    Google.employees.add(steven)
    Google.employees.add(drew)

for employee in Google.employees:
    print('{} is a {} who works at {} and began on {}'.format(employee.name, employee.title, Google.company_name, employee.start_date))

# print('{employee.name} is a {employee.title} who works at {Google.company_name} and began working on {employee.start_date}' for employee in Google.employees)
