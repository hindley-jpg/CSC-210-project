

# The Advisor Engine: Year 1 to Year 2 Logic
def advisor_bot():
    print("--- CS ADVISOR ENGINE v2.0 ---")
    
    # 1. ACADEMIC STATE (Inputs) 
    from model import Course
    from Scraper1 import course_objects #bringing in my list of scraped courses from scraper
    course_map = {
    course.code: course for course in (course_objects)
    }
    print(course_map)
    prerequisites_map = {
    "CSC123": [],
    "CSC223": ["CSC123"],
    "CSC280": ["CSC223"],
    # ... and so on
    }

    for course in course_objects:
        course.prerequisites = prerequisites_map.get(course.code, [])

    # 2. INFERENCE RULES
    # Transitivity Check: Discrete Math is the gateway to Theory of Computing (212)
    #can_take_theory = passed_CSC210
    
    # Prerequisite Check: OOP is Necessary for Data Structures (280)
    #can_take_data = passed_CSC223
    
    # 3. YEAR 2 PREDICTIONS (Transitivity + Modus Ponens)
    # If you can take Data Structures, you can eventually take Graphics (322)
    #can_eventually_take_graphics = can_take_data
    
   # print("\n--- YOUR LOGICAL PATH ---")
    # if can_take_theory:
    #     print("[ELIGIBLE]: CSC 212 (Theory of Computing)")
    # else:
    #     print("[BLOCKED]: CSC 212. Reason: Discrete Math (210) is a Necessary Condition.")
        
    # if can_eventually_take_graphics:
    #     print("[PATH OPEN]: You are on track for CSC 322 (Graphics) in Semester 4.")
    # else:
    #     # Modus Tollens
    #     print("[PATH BLOCKED]: Senior Graphics is unreachable until CSC 223 is cleared.")

advisor_bot()
