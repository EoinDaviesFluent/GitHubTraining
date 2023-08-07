exam_mark=-1
level=-1
while not(1<=exam_mark<=100):
    exam_mark=int(input('Please input the exam mark of the student: '))
    if not(1<=exam_mark<=100):
        print ('Exam Mark has to be between 1 and 100')

while not(level in (1,2)):
    level=int(input('Please input the level of the student: '))
    if not(level in (1,2)):
        print ('Level has to be 1 or 2')
if level==1:
    if exam_mark>=71:
        print ('Distinction')
    elif exam_mark>61:
        print ('Merit')
    elif exam_mark>50:
        print ('Pass')
    else:
        print ('Fail')
else:
    if exam_mark>=66:
        print ('Distinction')
    elif exam_mark>51:
        print ('Merit')
    elif exam_mark>40:
        print ('Pass')
    else:
        print ('Fail')
