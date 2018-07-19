with open('exam.txt') as tf:
    exam_lines = tf.readlines()
#print file content
print(exam_lines)
#print number of lines in the file
print(len(exam_lines))
#print fifth line
print(exam_lines[4])
#getting last line by using negative index
last = exam_lines[-1]
#print last line
print(last)
# print the letter o from the last line which is the 6th letter
print(last[5])
#split() splits the line in to a list, I can pass a parameter to split, the default is spaces, so separating 
#the list by its spaces allows me to count the words in the sentence
print(len(last.split()))
d = {"levelone": [1, 2, {'leveltwo': [5, 6, [1, ['get me please']]]}]}
#lt1 gets the value in the dictionary
lt1 = d['levelone']
#d2 gets the 3rd item in the list
d2 = lt1[2]
#lt2 gets the value of the inner dictionary
lt2 = d2['leveltwo']
#lt3 gets the content of the list inside a list
lt3 = lt2[2][1][0]
#print the string get me please
print(lt3)
mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]
#set allows me to make a list from mylist that conatins only the unique characters inside my list
#without the repeted characters
print(len(set(mylist)))
#end of file
