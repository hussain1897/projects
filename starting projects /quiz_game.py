print("Welcome to the computer Quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()
#if statements checks to see if input is yes
#.lower used to automatically put input into lower case 

print("Okay! Let's play :)")

score = 0 

answer1 = input("what does CPU stand for ? ").lower()
if answer1 == "central processing unit":
    print ('Correct!')
    score +=1 #if statement checks answer adds 1 to score if it is right
else:
    print("incorrect :(")

answer1 = input("What does GPU stand for? ")
if answer1.lower() == "graphics processing unit":
    print ('Correct!')
    score +=1
else: 
    print("incorrect :(")

answer1 = input("What does RAM stad for? ").lower()
if answer1 == "random access memory":
    print ('Correct!')
    score +=1
else: 
    print("incorrect :(")

answer1 = input("What does PSU stand for? ").lower()
if answer1 == "power supply unit":
    print ('Correct!')
    score +=1
else: 
    print("incorrect :(")

print("You got "+ str(score) + " questions correct!")
print("You got "+ str((score/4) * 100) + "%.")