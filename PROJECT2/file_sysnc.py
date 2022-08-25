from dirsync import sync
import os
from threading import Timer


def directory(message=None):

    path = input(message)
    path = path if path else os.getcwd()
    # print("path",path)
    if not os.path.exists(path):
        os.makedirs(path)
        print('path not available creating directory')
   
    return path

# directory()
run =True
def fileSysnc(interval=1):

    #source must be privided else error
    source=''
    path=''
    while True:
        source = input('Enter A Valid Source : ').strip()
        print(source)
        path = os.path.exists(source)
        if source and path:
            break

    destination =input('Enter A Destination Directory:  \nif NULL will be saved in current working directory \Destination: ').strip() or os.getcwd()+'/Destination'
    # print("destination dir ",destination)
    logfile_name = input('Enter A Log File Name: ' ).strip() or "logger"
    
    logfile_dir = directory('Enter A Log Directory  \nif NULL will be saved in current working directory : ')
    logfile_name = logfile_dir+'/'+logfile_name+'.log'
    # print("log_dir",logfile_dir+'/'+logfile_name)
    
    interval = int(input('Enter The Number Of sync interval : ').strip() or 1)

    if run:
        Timer(interval,fileSysnc).start()
    # RUN SYNC BETWEEN SOURCE AND DESTINATION

    
    sync(source, destination, logfile_name,'sync',verbose=True,purge=True,create=True)


    print(f'waiting for {interval} seconds to begin sync')



fileSysnc()


# TESTING_DIR/source