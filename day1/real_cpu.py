import psutil

print(psutil.cpu_percent(interval=1))

#get everything (i.e. all the functions) that we can do with a library
print(dir(psutil))

#know what does subprocess do
print(psutil.subprocess.__doc__)