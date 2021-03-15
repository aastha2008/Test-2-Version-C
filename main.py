#Step 1: Introduce game and its rules
print("Welcome to the multiplication game. You will have three seconds to answer the multiplication question or you FAIL!")

#Step 2: Computer ask if user is ready to start
user_input=input("Are you ready to start, please enter yes or no: ")
if(user_input == "yes"):
  print("Ok then")
  import time
  import random
  total_score=-1
  '''
  for x in range(3,0,-1):
    time.sleep(1)
    print(x)
  #Step 3: Compter chooses two random numbers between 0-12
  
  cpt_number1=random.randint(0,12)
  cpt_number2=random.randint(0,12)
  print("The first computers number is: " + str(cpt_number1))
  print("The second computers number is: " + str(cpt_number2))

  #Step 4:Computer ask user the multiplication question and start timer
  start_time=time.time()
  user_answer=int(input("What is the answer to " + str(cpt_number1) + "*" + str(cpt_number2) + ":"))

  #Step 5: Computer lets them know how many secs has passed
  return_time=time.time()
  user_time=return_time-start_time
  print("The user took 1st time " + str(user_time) + " to answer.")

  #Step 6: If user answers correctly, cpt will ask another multiplicaion question, and wil restart timer
  '''
  user_answer=0
  cpt_number1=0
  cpt_number2=0
  while(user_answer == cpt_number1 * cpt_number2):
    print("Congrats you got the right answer")
    print("Ok then next question")
    for x in range(3,0,-1):
      time.sleep(1)
      print(x)
    cpt_number1=random.randint(0,12)
    cpt_number2=random.randint(0,12)
    start_time=time.time()
    user_answer=int(input("What is the answer to " + str(cpt_number1) + "*" + str(cpt_number2) + ":"))
    return_time=time.time()
    user_time=return_time-start_time
    print("The user here took " + str(user_time) + " to answer.")
    total_score+=1
    #print("Your total score is:" + str(total_score))
  else:
    print("Sorry you got it wrong. Your total score was: " + str(total_score))

    
  
elif(user_input == "no"):
  print("Sorry thanks")
else:
  print("Sorry this is invalid")
