"""Generate sales report showing total melons each salesperson sold."""


# salespeople = []
# melons_sold = []
sales_by_person = {}

# open sales-report file ans save to variable 
f = open('sales-report.txt')

# iterate over file
for line in f:
    entries = line.rstrip().split('|')

    # assign sales person name and number of melons sold to variables
    salesperson = entries[0]
    melons = int(entries[2])

    # check if salesperson already exists in list
    # would be more organized and have a faster lookup if a dictionary were used
    if salesperson in sales_by_person:
        # add melons sold to exisiting melons
       sales_by_person[salesperson] += melons
    else:
        # add sales person and number of melons sold to dictionary
        sales_by_person[salesperson] = melons
 
#  print easy to read report with sales person's name and the total number
# of melons sold
for person, melons in sales_by_person.items():
     print(f'{person} sold {melons} melons')


