import pandas as p
import csv
from datetime import datetime
now=datetime.now()
current_time = now.strftime("%H:%M:%S")
data=[['1','ram',current_time,'present'],['2','Shyam',current_time,'present']]
filename = "attendance.csv"
col_list=["SN","Name","Time","Attendance"]       
reader = p.read_csv(filename, usecols=col_list)
test=reader['Name'][0]

def attendance(name,test):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    rows = ['1', name, current_time,'Present']
    #for name in rows:


    # name of csv file
    filename = "attendance.csv"
        
    # writing to csv file
    with open(filename, 'a') as csvfile:
        # creating a csv writer object
        #csvreader=csv.reader(csvfile)
        csvwriter = csv.writer(csvfile)
        if test!=name:
            csvwriter.writerows(rows)
    csvfile.close()

attendance('shyam',test)
    




            
    

            

            

        
