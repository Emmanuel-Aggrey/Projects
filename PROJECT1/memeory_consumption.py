import psutil
from datetime import datetime
import csv,time,json

def memeory_consumption(seconds=1,repeat=5):
    processes = psutil.Process()
    RSS= processes.memory_info().rss
    VMS= processes.memory_info().rss
    
    for i in range(repeat):

        # print('RSS: ',RSS,'VMS: ',VMS)
     
        data = {
            'RSS': RSS,
            'VMS':VMS,
            'Time_taken': datetime.now().strftime('%H:%M:%S')

        }
        time.sleep(seconds)

        print(data)

        json_object =  json.dumps(data,indent=6)
        with open ('LOGS/memeory_consumption.json','a') as json_file:
            json_file.write(json_object)
        
        # with open ('memeory_consumption.csv', 'a+') as csv_file:
        #     csv_data  = csv.writer(csv_file)
        #     csv_data.writerow([data.get('RSS'),data.get('VMS'),data.get('Time_taken')])
        #     return csv_data


    return processes


memeory_consumption()



# your code here    
