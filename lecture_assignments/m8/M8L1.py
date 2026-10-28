#using relative path
#could use absolute path: /workspaces/cpsc223_python/lecture_assignments/m8/pi.txt
#but no need

#read() returns the contents of the file as one string
with open('pi.txt') as file_object:
    contents = file_object.read()

print(contents.strip())

# readlines() returns list of lines
with open('pi.txt') as file_object:
    contents = file_object.readlines()

print(contents)