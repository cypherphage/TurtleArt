import os
import glob

pathname = 'C:\\2\\3\\4\\file.txt'
(dirname, filename) = os.path.split(pathname)
(shortname, extension) = os.path.splitext(filename)

print(f" dirname: {dirname} \n filename: {filename} \n shortname: {shortname} \n extension: {extension}")

#The glob module takes a wildcard and returns the path of all files and directories matching the wildcard

print(glob.glob('*.py'))

#os.stat() function returns an object that contains several different types of metadata about the file

x = glob.glob('*.py')
for file_name in x:
    print(os.path.realpath(file_name))


#List comprehensions
real_path = [os.path.realpath(f) for f in glob.glob('*.py')]
print(real_path)

#file size greater than 200
real_path_200 = [os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 200]
print(real_path_200)

size_with_path = [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]
print(size_with_path)

#swap key and vlaue of a dictionary
a_dict = {'a':1,'b':2,'c':3}
print(a_dict)
a_dict = {value:key for key, value in a_dict.items()}
print(a_dict)