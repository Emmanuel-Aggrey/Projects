import psutil
import time
from datetime import datetime
import json
import csv

cpu_percentage = psutil.cpu_percent()

#METHOD TO SET CPU AND TIME INTERVAL
def get_cpu_percentage(interval=5,repeat=5):
    cpu_percentage = psutil.cpu_percent(interval=interval)
    

    # LOOP PER THE REQUIRD INTERVAL
    for i in range(repeat):
        cpu_percentage = psutil.cpu_percent(interval=interval)
  
        data = {
            'CPU_Usage': cpu_percentage,
            'Time_taken': datetime.now().strftime('%H:%M:%S')

        }

        # DUMP THE RESULTS TO JSON
        json_object =  json.dumps(data,indent=4)
        with open ('LOGS/cpu_usage.json','a') as json_file:
            json_file.write(json_object)
            print(json_object)

        
        # with open ('PROJECT1/cpu_usage.csv', 'a') as csv_file:
        #     csv_data  = csv.writer(csv_file)
        #     csv_data.writerow([data.get('CPU_Usage'),data.get('Time_taken')])
        #     return csv_data


    return cpu_percentage

    interval = int(input('Enter The Number Of sync interval : ').strip() or 1)

# RUN THE RESULTS
get_cpu_percentage()


