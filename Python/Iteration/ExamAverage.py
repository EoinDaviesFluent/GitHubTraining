sum_of_exam_scores=0
for i in range(3):
    score=-1
    if i==0:
        print ('Please input the score for the Maths Exam')
    elif i==1:
        print ('Please input the score for the English Exam')
    else:
        print ('Please input the score for the ICT Exam')
    while not(0<=score<=100):
        score=int(input(': '))
        if not(0<=score<=100):
            print ('Exam score must be between 0 and 100')
    sum_of_exam_scores+=score
average_exam_score=sum_of_exam_scores/3

if average_exam_score>=65:
    print ('Average score is',round(average_exam_score,1),': Pass')
else:
    print ('Average score is',round(average_exam_score,1),': Fail')