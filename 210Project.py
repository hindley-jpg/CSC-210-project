

# The Advisor Engine: Year 1 to Year 2 Logic
def advisor_bot():
    print("--- CS ADVISOR ENGINE v2.0 ---")
    
    # 1. ACADEMIC STATE (Inputs) 
    from Scraper1 import course_objects #bringing in my list of scraped courses from scraper
    from Prereq_cheque import check_eligibility
    from output_test import recommend_course_plans

    prerequisites_map = {
    "CSC 123": [],
    "CSC 223": ["CSC 123"],
    "CSC 212": ["CSC 210"],
    "CSC 280": ["CSC 223"],
    "CSC 323": ["CSC 123"],
    "CSC 322": ["CSC 280"],
    "CSC 363": ["CSC 280"], 
    "CSC 370": ["CSC 280"],
    "CSC 442": ["CSC 363"], 
    "CSC 390": ["CSC 326"],
    "CSC 306": ["CSC 390"],
    "MATH 122": ["MATH 121"],
    "MATH 309": ["MATH 122"],
    "PHIL 202": ["PHIL 201"],
    "PHIL 362": ["PHIL 202"],
    "TRS 202": ["TRS 201"],
    }
    #applying prerequesite dictionary to course_objects dictionary 
    for course in course_objects:
        course.prerequisites = prerequisites_map.get(course.code, []) 
    check_eligibility(course_objects)
    semester_order = [
        "year 1 fall", "year 1 spring",
        "year 2 fall", "year 2 spring",
        "year 3 fall", "year 3 spring",
        "year 4 fall", "year 4 spring"
    ]

advisor_bot()
