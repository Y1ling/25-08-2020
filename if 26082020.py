# practice of if else statement
# enter an the answer between ABCD
x = str(input("Which one of these is the best Uni in SA： \n"
              "A. Flinders\n"
              "B. tafe SA\n"
              "C. Uni SA\n"
              "D. Adelaide Uni\n"))
# Use if else statement to identity the answer
# For each different case, execute the specific operation
if x == "A":
    print("Congratulations, you made the right choice")
elif x == "B":
    print("Sorry, wrong answer!!")
elif x == "C":
    print("Nope, you chose the wrong one!!")
elif x == "D":
    print("Is it so hard to choose the right one?")
else:
    print("invalid answer, please do again!!!")