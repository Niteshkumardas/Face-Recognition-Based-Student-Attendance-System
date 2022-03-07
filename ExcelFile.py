import csv
import sys
from datetime import datetime
from matplotlib.style import use
import pandas as p
# from predict import 
# field names
#fields = ['SN','Name', 'Time','Attendance Record']
	
# data rows of csv file
# format_data = "%H:%M:%S"

def attendance(name):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    rows = ['1', name, current_time,'Present']
    #for name in rows:


    # name of csv file
    filename = "attendance.csv"
        
    reader = p.read_csv(filename, usecols='name')
    print(reader)
    # writing to csv file
    with open(filename, 'a') as csvfile:
        # creating a csv writer object
        #csvreader=csv.reader(csvfile)
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)


            
        # writing the fields
        # csvwriter.writerow(fields)
            
        # writing the data rows
        '''for name in csvfile:
            i=0
            if (name[i]!=name[i+1]):

                csvwriter.writerow(rows)
            else:
                exit(0) '''


            
    csvfile.close()

if __name__ == "__main__":
    name = sys.argv[1]
    attendance(name)
            
