
import os
import re

def batch_rename(directory, pattern, replacement):
    for filename in os.listdir(directory):
        new_filename = re.sub(pattern, replacement, filename)
        if new_filename != filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')

def batch_rename(directory,replacement):
    i=0
    for filename in os.listdir(directory):
        if 'jpg' in filename.lower():
            new_filename=replacement+str(i)+".jpg"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')
            i+=1
        else:
            print(f'Skipped: {filename} (not a JPG)')
        

if __name__ == "__main__":
    #directory = input("Enter directory path: ")
    #pattern = input("Enter regex pattern to match: ")
    #replacement = input("Enter replacement string: ")
    #batch_rename(directory, pattern, replacement)
    directory='D:\\GitHub\\jack_img\\'
    t='t001'
    t='t002'
    t='t003'
    replacement='3D print 1_64 scale 3D-printable train Electric Train Toy Mecha-Punk Train '
    batch_rename(directory+t,replacement+t)
