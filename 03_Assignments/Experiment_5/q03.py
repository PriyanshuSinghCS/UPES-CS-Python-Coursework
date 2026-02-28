# WAP to input a list of scores for N students in a list data type. Find the score of the runner
# up and print the output. 
# Sample Input 
# N = 5 
# Scores= 2 3 6 6 5 
# Sample output 
# 5 
# Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, 
# we print 5 as tn = int(input("Enter number of students: "))

n = int(input("Enter number of students: "))
scores = []
for i in range(n):
    x = int(input())
    scores.append(x)

max_score = scores[0]

for s in scores:
    if s > max_score:
        max_score = s

runner_up = None

for s in scores:
    if s != max_score:
        if runner_up is None or s > runner_up:
            runner_up = s

print(runner_up)

