import psutil
from datetime import datetime
import json,time

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
        # json_object =  json.dumps(data,indent=6)
        # with open ('memeory_consumption.json','a') as json_file:
        #     json_file.write(json_object)


    return processes


memeory_consumption()



# your code here    
