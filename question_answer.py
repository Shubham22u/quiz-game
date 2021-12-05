print("Welcome To Computer Basic Quiz! ")

playing = input("Do You Want To Play? 'yes' or 'no' :")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Start The Quiz  :)  ")

score = 0
##################################################################################

answer = input("Question 1 ----   What does CPU stand for ?  ")
if answer.lower() == "central processing unit":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

##################################################################################

answer = input("Question 2 ----   What does GPU stand for ?  ")
if answer.lower() == "graphics processing unit":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

###################################################################################

answer = input("Question 3 ----   What does UPS stand for ?  ")
if answer.lower() == "uninterruptible power supply":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

####################################################################################

answer = input("Question 4 ----   What does RAM stand for ?  ")
if answer.lower() == "random access memory":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

####################################################################################

answer = input("Question 5 ----   What does ROM stand for ?  ")
if answer.lower() == "read only memory":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

####################################################################################

answer = input("Question 6 ----   What does URL stand for ?  ")
if answer.lower() == "uniform resource locator":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

###################################################################################

answer = input("Question 7 ----   What does USB stand for ?  ")
if answer.lower() == "universal serial bus":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

###################################################################################

answer = input("Question 8 ----   What does CD stand for ?  ")
if answer.lower() == "compact disk":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

##################################################################################

answer = input("Question 9 ----   What does DVD stand for ?  ")
if answer.lower() == "digital versatile disc":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

###################################################################################

answer = input("Question 10 ----   What does IP stand for ?  ")
if answer.lower() == "internet protocol":
    print("Correct! To The Next Question ------->")
    score += 1
else:
    print("Incorrect! Please Try Again After Some Study")

###################################################################################

print(" You Got  " + str(score) + "   Questions Correct! ")
print(" You Got  " + str((score/10)*100) + "% ")

