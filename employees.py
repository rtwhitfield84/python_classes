# Instructions

# Create a class that contains information about employees of a company and define methods to get employee name, job title, and start date.

class Company(object):

    def __init__(self, name, title, company_name, start_date):
        self.name = name
        self.title = title
        self.company_name = company_name
        self.start_date = start_date

    def getName(self):
        return self.name

    def getJob(self):
    	return self.title

    def startDate(self):
    	return self.start_date

    def getCompany(self):
    	return self.company_name

    def __str__(self):
    	return "%s is a %s that began working at %s on %s" % (self.name, self.title, self.company_name, self.start_date)

richard = Company("Richard", "Developer", "Google", "April 1st, 2017")

print(richard.getName())
print(richard.getJob())
print(richard.startDate())
print(richard)
    # Add the remaining methods to fill the requirements above