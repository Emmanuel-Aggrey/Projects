from dirsync import sync
import os



def directory(message=None):

    path = input(message)
    path = path if path else os.getcwd()
    # print("path",path)
    if not os.path.exists(path):
        os.makedirs(path)
        print('path not available creating directory')
   
    return path

# directory()

def fileSysnc():

    source = input('Enter A Valid Source : ')
    print("source",source)

    destination =input('Enter A Destination Directory:  \nif NULL will be saved in current working directory \Destination: ') or os.getcwd()+'/Destination'
    # path = destination if destination  else  os.getcwd()+'/Destination'
    print("destination dir ",destination)
    # path = path if path else os.getcwd()
    logfile_name = input('Enter A Log File Name: ' ) or "logger"
    
    logfile_dir = directory('Enter A Log Directory  \nif NULL will be saved in current working directory : ')
    print("log_dir",logfile_dir+'/'+logfile_name+'.log')
    
    interval = input('Enter The Number Of sync interval : ') or 1



    sync(source, destination, logfile_name,'sync',verbose=True,purge=True,create=True)


fileSysnc()


# TESTING_DIR/source