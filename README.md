## Fast-Query-Engine
Interactive Fast Query Engine for a Server log file.

Query Engine is an interactive tool for querying CPU utilization from Server logs from the command line. 
### generator.py 
replicates log for a given day and save “.log” file to a given directory. 
```
./generator.py /Users/tanmay/Desktop/2014-10-31.log
```
This command will generate a log file in the given path with file name 2014-10-31.log and prompt with the path of the newly created log file.

### query.py 
Command to run query engine:
```
./query.py /Users/tanmay/Desktop/2014-10-31.log
```

to run the interactive query that takes two commands:
#### QUERY 
for querying log file with input parameter <IP address of Server> <CPU ID> <Start time> <Stop time> 
  
#### EXIT 
to exit the query engine. The purpose of this tool is its fast query time.

![alt text]()



