'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6


OG = (SG*(100-FW) + FE*FW)/100
grade times worth added together
'''
print("Welcome to grading software v1.1 (Unstable build, may explode upon error")
SG = float(input("What is your semester grade"))
TS = float(input("What is the score of the test"))
TW = float(input("How much is the test worth?"))

endscore = SG*(100-TW) + TS * TW
endscore /=100
print("The Overall grade is:", endscore)
