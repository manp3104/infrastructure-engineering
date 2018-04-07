'''
Create a program/script in any language like Python, Bash, C, C++ etc. The program should scan all the Drives and folders like C:/User/* (Windows) and /home/* (Linux) recursively and then identify the top 10 files which have the largest size on the system.

Example: The tool should scan the Downloads folder, Documents Folder, Movies folder, C drive, E drive etc and display the 10 biggest files in these folders with their size in MB.
'''


import os
import heapq
import win32api


total_size = 0
max_val = 0
# Store the name of files(complete address) along with their size
heapData = [] 
q = 0


for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
    
    root = drive

    for root, dirs, files in os.walk(root):

        for file in files:
            path = os.path.join(root, file)
        

            try:
                file_size = os.path.getsize(path)
                total_size += file_size
                q += 1
                # Prints the number of files processed
                # print(q)    
                
                if len(heapData) < 10:
                    # Add the file to heapData
                    heapq.heappush(heapData, (float(file_size)/1054414.675, path))
                else:
                    # Add one file to heapData and remove one file from heapData 
                    heapq.heappushpop(heapData, (float(file_size)/1054414.675, path))

            except OSError:
                continue
        
# List to store 10 largest files in descending order(based on file size)
largestFiles = []
largestFiles = heapq.nlargest(10, heapData)

# Print the 10 largest files
for file in largestFiles:
    print(file)

    