

# The Advisor Engine: Year 1 to Year 2 Logic
def advisor_bot():
    print("--- CS ADVISOR ENGINE v2.0 ---")
    #questions for Dr Hui:
    # 1. modularity? to what extent? 2. should i scrape the course list, or do static? 3. Electives..placeholders, or do I need to account for all possibilities?
    # 
    # 1. ACADEMIC STATE (Inputs) 
    passed_math121 = input("Passed Calculus I? (y/n): ") == 'y'
    passed_CSC210 = input("Passed Discrete Math (CSC 210)? (y/n): ") == 'y'
    passed_CSC223 = input("Passed OOP (CSC 223)? (y/n): ") == 'y'
    from model import Course
    def __repr__(self):
        # Join the list into a readable string for the repr
        prereq_str = ", ".join(self.prerequisites) if self.prerequisites else "None"
        return (f"Course({self.code}, {self.name}, "
                f"Prereqs: [{prereq_str}], Passed: {self.is_passed})")
    
    
    CSC120 =  Course("CSC 120", "Intro to Computational Thinking",3,) #planning to make this list a separate module and import
    MATH121 = Course("MATH 121", "Calculus I",4,)
    ENG101 = Course("ENG 101", "Writing and Rhetoric", 3,)
    CSC123 = Course("CSC 123", "Intro to Computer Programming",3,)
    PHIL201 = Course("PHIL 201", "The Classical Mind", 3)
    MATH122 = Course("Math 122", "Calculus II", 4, ["Math121"],)
    CSC223 = Course("CSC 223", "Object Oriented Programming", 3,)
    CSC220 = Course("CSC 220", "Discrete Mathematics",3,)
    PHIL202 = Course("PHIL 202", "The Modern Mind", 3)
    TRS201 = Course("TRS 201", "Faith Seeking Understanding",3)
    CSC212 = Course("CSC 212", "Theory of Computing", 3,)
    CSC280 = Course("CSC280", "Data Structures", 3)
    CSC370 = Course("CSC 370", "Concepts of Programming Languages")
    TRS202A = Course("TRS 202A","",3)
    TRS202B = Course("TRS 202B")
    course_List = [CSC120, MATH121, ENG101, CSC123, PHIL201, MATH122, CSC220, CSC223, PHIL202, TRS201, CSC212, CSC280, CSC370, TRS202A, TRS202B,
                   ]

    proposition_map = {
    course.code: chr(112 + i) for i, course in enumerate(course_List)
    }
    print(proposition_map)

    
    # 2. INFERENCE RULES
    # Transitivity Check: Discrete Math is the gateway to Theory of Computing (212)
    can_take_theory = passed_CSC210
    
    # Prerequisite Check: OOP is Necessary for Data Structures (280)
    can_take_data = passed_CSC223
    
    # 3. YEAR 2 PREDICTIONS (Transitivity + Modus Ponens)
    # If you can take Data Structures, you can eventually take Graphics (322)
    can_eventually_take_graphics = can_take_data
    
    print("\n--- YOUR LOGICAL PATH ---")
    if can_take_theory:
        print("[ELIGIBLE]: CSC 212 (Theory of Computing)")
    else:
        print("[BLOCKED]: CSC 212. Reason: Discrete Math (210) is a Necessary Condition.")
        
    if can_eventually_take_graphics:
        print("[PATH OPEN]: You are on track for CSC 322 (Graphics) in Semester 4.")
    else:
        # Modus Tollens
        print("[PATH BLOCKED]: Senior Graphics is unreachable until CSC 223 is cleared.")

advisor_bot()
