score=0;
question1 ="What is the capital of France?"
answers="paris", "berlin", "london"
correct="paris"
correct_answer1=correct
print(question1)
print(answers)
name=input("enter your answer-")
if name==correct_answer1:
    print("Correct")
    score+=1
    print(score," point")
else:
    print("Incorrect")

question2 ="What is the capital of Qatar?"
answers1="doha", "beijing", "nur-sultan"
print(question2)
print(answers1)
correct1="doha"
name1=input("enter your answer-")
if name1==correct1:
    print("Correct")
    score+=1
    print(score," point")
else:
    print("Incorrect")

question3 ="What is the capital of Japan?"
answers3="madrid", "tokyo", "london"
print(question3)
print(answers3)
correct3="tokyo"
name3=input("enter your answer-")
if name3==correct3:
    print("Correct")
    score+=1
    print(score," point")
else:
    print("Incorrect")

question4 ="What is the capital of Vietnam?"
answers4="hanoi", "vientian", "doha"
print(question4)
print(answers4)
correct4="hanoi"
name4=input("enter your answer-")
if name4==correct4:
    print("Correct")
    score+=1
    print(score," point")
else:
    print("Incorrect")

question5 ="What is the capital of Laos?"
answers5="hanoi", "vientian", "doha"
print(question5)
print(answers5)
correct5="vientian"
name5=input("enter your answer-")
if name5==correct5:
    print("Correct")
    score+=1
    print(score," point")
else:
    print("Incorrect")

question6 ="What is the capital of south corea?"
answers6="seoul", "beijing", "doha"
print(question6)
print(answers6)
correct6="seoul"
name6=input("enter your answer-")
if name6==correct6:
    print("Correct")
    score+=1
    print(score," point")
else:
    print("Incorrect")

if score==6:
    print("excellent 9 out of 9")
else:
    print("better luck next time")










