import psutil
import time
from datetime import datetime
import json

cpu_percentage = psutil.cpu_percent()


def get_cpu_percentage(interval=4,repeat=5,seconds=1):
    cpu_percentage = psutil.cpu_percent(interval=interval)
    

    
    for i in range(repeat):
        # start = datetime.now()
        cpu_percentage = psutil.cpu_percent(interval=interval)
        # end = datetime.now()
        # time_taken = end - start
        data = {
            'CPU Usage': cpu_percentage,
            'Time_taken': datetime.now().strftime('%H:%M:%S')

        }
        # time.sleep(seconds)

        json_object =  json.dumps(data,indent=4)
        with open ('cpu_usage.json','a') as json_file:
            json_file.write([json_object])
            print(json_object)


    return cpu_percentage


get_cpu_percentage()



# your code here    
