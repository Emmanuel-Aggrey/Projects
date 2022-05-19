
=======================================================================================

**PROJECT ONE DEPENDENCIES**

i.	psutil : this package gets properties mostly about hardware of pcs


=====================================================================================

**PROJECT TWO DEPENDENCIES**

i.	dirsync :This package helps sync directories very efficient and have good documentation

The dirsync package has a default parameters as

sync(**source, destination, sync, logger=logger, **options** )

where when logger is provided disables the verbose=True which logs the sync to console

for that reason, i have overriden the paramaters and added a **logger parameter as logfile_name** which logs to file and also to console

sync(**source, destination, logfile_name,'sync',**options**)

======================================================================================

**PROJECT THREE DEPENDENCIES**

i.	socket : Helps to implement socket programming in python (communication between server and clients async)

ii.	select: Selects the incoming port and forwards it socket.accept() to use a single port in the the request and response circle

iii.	pandas: Data analytics package - used to read the csv file used to save  clients and server data

=======================================================================================
