import psutil

pids =psutil.pids()
data = {
    'descriptors_opened':len(pids)
}

print(data)

