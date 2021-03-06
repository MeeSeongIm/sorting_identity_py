# non-interactive gradebook (organizing data)
# computes mean, median, standard deviation, variance. 

from math import sqrt

unique_id = []

model = {
    "Last": "Total", 
    "First": "Possible on", 
    "id": "000000", 
    "ex": [100,100,100],
    "hw": [5,5,5,5,5],
    "quiz": [5,5,5,5,5],
    "proj": [1,1,1,1,1],
    "final": [300]
    }

s1 = {
    "Last": "Etudient", 
    "First": "Un",  
    "id": "000000",  
    "ex": [90,80,70], 
    "hw": [5,5,5,5,5], 
    "quiz": [5,4,3,2,1], 
    "proj": [1,1,1,1,1], 
    "final": [250] 
    }

s2 = {
    "Last": "Person", 
    "First": "Two",  
    "id": "000000",  
    "ex": [90,80,70], 
    "hw": [5,5,5,5,5], 
    "quiz": [5,4,3,2,1], 
    "proj": [1,1,1,1,1], 
    "final": [200] 
    }

s3 = {
    "Last": "Anonymous", 
    "First": "Three",  
    "id": "000000",  
    "ex": [90,80,70], 
    "hw": [5,5,5,5,5], 
    "quiz": [5,4,3,2,1], 
    "proj": [1,1,1,1,1], 
    "final": [300] 
    }

s4 = {
    "Last": "Random", 
    "First": "Four",  
    "id": "000000",  
    "ex": [90,80,70], 
    "hw": [5,5,5,5,5], 
    "quiz": [0,0,0,0,0], 
    "proj": [1,1,1,1,1], 
    "final": [100] 
    }

unique_id.extend((dict(model), dict(s1),dict(s2),dict(s3), dict(s4)))

for i in range(0,len(unique_id)):
    print(unique_id[i]) 

def avg_ex(j):
    return sum(unique_id[i]["ex"][j] for i in range(1, len(unique_id)))/(len(unique_id)-1) 
for j in range(0,len(unique_id[0]["ex"])):
    print("Exam %s average is %s." % (j+1, avg_ex(j)))
 
ex_tot_poss = sum(unique_id[0]["ex"][i] for i in range(0, len(unique_id[0]["ex"]) ))
hw_tot_poss = sum(unique_id[0]["hw"][i] for i in range(0, len(unique_id[0]["hw"]) ))
quiz_tot_poss = sum(unique_id[0]["quiz"][i] for i in range(0, len(unique_id[0]["quiz"]) ))
proj_tot_poss = sum(unique_id[0]["proj"][i] for i in range(0, len(unique_id[0]["proj"]) ))
fin_tot_poss =  sum(unique_id[0]["final"][i] for i in range(0, len(unique_id[0]["final"]) ))

def ex_tot_pts(j):
    return sum(unique_id[j]["ex"][i] for i in range(0, len(unique_id[j]["ex"]))) # ex total pts for jth person
def hw_tot_pts(j):
    return sum(unique_id[j]["hw"][i] for i in range(0, len(unique_id[j]["hw"])))
def quiz_tot_pts(j):
    return sum(unique_id[j]["quiz"][i] for i in range(0, len(unique_id[j]["quiz"]))) 
def proj_tot_pts(j):
    return sum(unique_id[j]["proj"][i] for i in range(0, len(unique_id[j]["proj"]))) 
def fin_tot_pts(j):
    return sum(unique_id[j]["final"][i] for i in range(0, len(unique_id[j]["final"]))) 

def rescaled_exam(j):
    return (ex_tot_pts(j)/ex_tot_poss)*100
def rescaled_hw(j):
    return (hw_tot_pts(j)/hw_tot_poss)*100
def rescaled_quiz(j):
    return (quiz_tot_pts(j)/quiz_tot_poss)*100
def rescaled_proj(j):
    return (proj_tot_pts(j)/proj_tot_poss)*100
def rescaled_fin(j):
    return (fin_tot_pts(j)/fin_tot_poss)*100 

def student_class_avg(j):
    return float(rescaled_exam(j)*.4 + rescaled_hw(j)*.1 + rescaled_quiz(j)*.1 + rescaled_proj(j)*.1 + rescaled_fin(j)*.3)

print("Total possible on the exams is %s points." % ex_tot_poss) 
print("Total possible on HW is %s points." % hw_tot_poss) 
print("Total possible on quizzes is %s points." % quiz_tot_poss)
print("Total possible on projects is %s points." % proj_tot_poss)
print("Total possible on the final is %s points." % fin_tot_poss)

print("\n")


for j in range(1, len(unique_id)):
    print("%s %s has a total of %s exam points." % (unique_id[j]["Last"], unique_id[j]["First"], ex_tot_pts(j)))

print("\n")

for j in range(1, len(unique_id)):
    print("%s %s has a total of %s HW points." % (unique_id[j]["Last"], unique_id[j]["First"], hw_tot_pts(j)))

print("\n")

for j in range(1, len(unique_id)):
    print("%s %s has a total of %s quiz points." % (unique_id[j]["Last"], unique_id[j]["First"], quiz_tot_pts(j)))

print("\n")

for j in range(1, len(unique_id)):
    print("%s %s has a total of %s project points." % (unique_id[j]["Last"], unique_id[j]["First"], proj_tot_pts(j)))

print("\n")

for j in range(1, len(unique_id)):
    print("%s %s has a total of %s final points." % (unique_id[j]["Last"], unique_id[j]["First"], fin_tot_pts(j)))

print("\n")

for j in range(1, len(unique_id)):
    print("%s %s has exam average %s." % (unique_id[j]["Last"], unique_id[j]["First"], rescaled_exam(j))) 

"""
print(rescaled_exam(1)) 
print(rescaled_hw(1)) 
print(rescaled_quiz(1)) 
print(rescaled_proj(1)) 
print(rescaled_fin(1))
"""

print("\n")

 
def letter_grade(k):
    if k <=100 and 90<= k:
        return "A"
    elif k<90 and k>=80:
        return "B"
    elif k<80 and k >=70:
        return "C"
    elif k<70 and k >=60:
        return "D"
    else:
        return "F"


 
for j in range(1, len(unique_id)): 
    print("%s %s currently has class average %s, which is a %s in the class." % (unique_id[j]["Last"], unique_id[j]["First"], student_class_avg(j), letter_grade(student_class_avg(j))) )

print("\n")

class_avg = sum(student_class_avg(j) for j in range(1, len(unique_id)))/(len(unique_id)-1)
print("The class average with %s students is %s." % (len(unique_id)-1, class_avg))

class_avg_list = []
class_avg_list.extend((student_class_avg(j) for j in range(1, len(unique_id))))
class_avg_list.sort()
if len(class_avg_list) % 2 ==0:
    class_med = (class_avg_list[int(len(unique_id)/2)]+ class_avg_list[ int((len(unique_id)/2))+1])*0.5
else:
    class_med = class_avg_list[int(len(unique_id)/2)]  # = class_avg_list[int(len(unique_id)-1+1/2)]
 
print("Students' (sorted) averages are given in this list: %s with the class median being %s." % (class_avg_list, class_med))

std_deviation = sqrt(sum( (student_class_avg(j) - class_avg)**2 for j in range(1, len(unique_id)))/(len(unique_id)-1))
variance = std_deviation**2

print("The standard deviation for this class is %s and the variance is %s." % (std_deviation, variance))

 
