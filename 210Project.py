

# The Advisor Engine: Year 1 to Year 2 Logic
def advisor_bot():
    print("--- CS ADVISOR ENGINE v2.0 ---")
    #questions for Dr Hui:
    #  1. Electives..placeholders, or do I need to account for all possibilities?
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
    
    from Scraper1 import course_objects #bringing in my list of scraped courses from scraper

    proposition_map = {
    course.code: chr(112 + i) for i, course in enumerate(course_objects)
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
