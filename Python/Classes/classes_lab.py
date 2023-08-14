class Student:
    def __init__(self,name_var,age_var,classroom_var):
        self.name=name_var
        self.age=age_var
        self.classroom=classroom_var
    def average_test(self,test_score_1,test_score_2,test_score_3):
        return sum((test_score_1,test_score_2,test_score_3))/3
student_1= Student('John Smith',22,'Physics')
student_2= Student('Molly Smith',21,'Geography')

print('Age of',student_2.name,'is',student_2.age)

student_2_results=student_2.average_test(72,45,89)

print ('The average score that',student_2.name,'got in',student_2.classroom,'was',student_2_results)