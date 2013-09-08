import xlrd 

book = xlrd.open_workbook('ROHP.xlsx')

guests = book.sheet_by_index(4)

status, shirt_size = guests.col_values(0), guests.col_values(19)

small, medium, large, xl = 0, 0, 0, 0

people = []
sizes = []

for i in range(len(status)):
    people.append([guests.cell_value(i, 0), guests.cell_value(i, 19)])

people = people[1:]    
for person in people:
    if person[0] == u'YES':
        sizes.append(person[1])

for size in sizes:
    if size == u'Small':
        small += 1
    elif size == u'Medium':
        medium += 1
    elif size == u'Large':
        large += 1
    elif size == u'X-Large':
        xl += 1
    

for person in people:
    print person




 


