exam_mark=-1
while not(1<=exam_mark<=100):
    exam_mark=int(input('Please input the exam mark of the student: '))
    if not(1<=exam_mark<=100):
        print ('Exam Mark has to be between 1 and 100')
if exam_mark>=71:
    print ('Distinction')
elif exam_mark>61:
    print ('Merit')
elif exam_mark>50:
    print ('Pass')
else:
    print ('Fail')