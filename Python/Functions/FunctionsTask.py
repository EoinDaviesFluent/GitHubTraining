import statistics
data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83" 
grades=data.split(',')
grades=list(map(int,grades))
print ('Grades Minimum:',min(grades))
print ('Grades Maximum:',max(grades))
print ('Grades Average:',round(sum(grades)/len(grades),2))
print ('Grades Mean:',statistics.mean(grades))
print ('Grades Median:',statistics.median(grades))
stringvar='In Grades, the maximum is {maximum}, the minumum is {minimum}, the average is {average}, the mean is {meanvar} and the median is {medianvar}'
print (stringvar.format(maximum=max(grades), minimum=min(grades), average=round(sum(grades)/len(grades),2), meanvar=statistics.mean(grades), medianvar=statistics.median(grades)))
