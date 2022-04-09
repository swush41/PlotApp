from array import array
import requests
import json
from datetime import datetime
from csv import writer
import schedule
import time

def collect():
  
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    pretty = json.loads(response.text)

    time = pretty['time']['updatedISO'][11:][:-9]
    price = pretty['bpi']['USD']['rate_float']

    d = [time, price]
    print(price)

    with open('plot.csv', 'a') as f_object:
  
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(d)
    
        #Close the file object
        f_object.close()
        print('done!')
# every two mins add one value


print('running....')
schedule.every(1).minutes.do(collect)
    

while True:
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)