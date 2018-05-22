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
#split() splits the line in to a list 
print(len(last.split()))
d = {"levelone": [1, 2, {'leveltwo': [5, 6, [1, ['get me please']]]}]}
lt1 = d['levelone']
d2 = lt1[2]
lt2 = d2['leveltwo']
lt3 = lt2[2][1][0]
print(lt3)
mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]
print(len(set(mylist)))
