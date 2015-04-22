import os

def rename_files():
    #Here I show the two ways to pass file path to the method chdir of the os object
    #os.chdir('C:\\Udacity\\stage3\\prank')
    os.chdir('C:\\Secret')
    #os.chdir(r'C:\Udacity\stage3\prank')

    #since the current directory is the directory where my files are
    #I can rightly assume that the method curdir will assign the list
    #of files in folder prank to the list files
    files=os.listdir(os.curdir)
    new_file_name=''
    #loop through files in the folder
    for current_file in files:
        #loop through letters of the file name for each file in the outer loop
        for i in current_file:
            #here's an interesting way I found to eliminate numbers from the file name
            new_file_name = ''.join(i for i in current_file if not i.isdigit())
        os.rename(current_file,new_file_name)


rename_files()

    

    
    
