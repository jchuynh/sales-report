"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # creating a list of salespeople
melons_sold = [] # creating a list of melons_sold

f = open('sales-report.txt') # opening the file (sales-report.txt)
for line in f: # for line in f
    line = line.rstrip() # strip the whitespaces to the right
    entries = line.split('|') # split the entries by |

    salesperson = entries[0] # the first entry is the salesperson
    melons = int(entries[2]) # the third entry is the number of melons

    if salesperson in salespeople: # if the name of the person is in the list
        position = salespeople.index(salesperson) # find the position slaes person in the list

        melons_sold[position] += melons # update the number of melons sold based on the position of the salesperon
    else:
        salespeople.append(salesperson) # if the person is not on the list, add them to the list
        melons_sold.append(melons) # if the melons sold was not on the list, add them to the list


for i in range(len(salespeople)): # print the salespeople and the number of melons they sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')


# improvements: using a dictionary to keep track of salespeople and melons sold 
