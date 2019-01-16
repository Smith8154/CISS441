import csv
import json

"""
who: Will Smith
when: 2019/01/15
what: it formats some stuff by doing some stuff I don't particularly understand
"""

playStore = []  # this is to collect data for printing at the end 
playStore_total = 0    # for counting the rows of data
with open('data1/googleplaystore.csv', 'r') as csvfile:

    # parse csv file pointer into playStore
    playStore_data = csv.DictReader(csvfile, delimiter=',', quotechar='"')

    # interate over playStore to process. 
    for playStore_row in playStore_data:
        playStore_total += 1

        playStore_app = playStore_row['App']
        playStore_category = playStore_row['Category']
        playStore_rating = playStore_row['Rating']
        playStore_installs = playStore_row['Installs']
        playStore_price = playStore_row['Price']

        # only show the first 20 rows. 
        if playStore_total <= 20:
            print(playStore_total, playStore_app ,playStore_category, playStore_rating, playStore_installs, playStore_price)
            playStore.append({playStore_total: [playStore_app ,playStore_category, playStore_rating, playStore_installs, playStore_price]
                })

            
print("I found " + str(playStore_total) + " apps.")
print("Donezo.")

print(json.dumps(playStore))
