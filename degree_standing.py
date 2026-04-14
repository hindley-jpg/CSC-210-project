#check degree standing, eligibility to graduate, etc. deans list, probation defined. 
def degree_standing (courses:list)-> None: 
    gpa = float(input ("what is your current Grade Point Average?"))
    fail = input ("Are you currently failing any class? (y/n) ").strip().lower()
    if gpa >= 3.5:
        print("Congratulations, you have made the Dean's List for this semester!")
    if fail == True:
        print ("You are on academic probation")
    else: 
        print ("keep up the good work!")
    
    
    

