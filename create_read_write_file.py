'''
process: read the text file
input :set the path of text file
output: Display the text
'''

def readfile(path):
    f = open(path, "r")
    print(f.read())
'''
process:create file text file 
input :set path for creation
output:Text file will be created
'''

def createfile(path):
    f = open(path, "w")

'''
process:exiting file add the data 
input :set data(text variable) to write and set path(path) 
Output: append data to text file
'''

def appenddatatofile(path, text):
    f = open(path, "a")
    f.write(text)
    f.close()

'''
process:CREATE file add the data 
input :set data(text variable) to write and set path(path) 
Output:File is created and data will write  
'''

def createfileandwrite(path, text):
    filehandle = open(path, 'w')
    filehandle.write(text)
    filehandle.close()

path = 'C:/Users/user/Downloads/p1.txt'
text = "TEXT TO WRITE OR APPEND"

readfile(path)
createfile(path)
appenddatatofile(path, text)
createfileandwrite(path, text)
