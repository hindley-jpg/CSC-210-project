
#create prerequisite map and apply it to courses listed in course_objects

def check_eligibility(courses: list) -> None:
    course_map = {c.code: c for c in courses}
    
    semester = input("What semester are you currently planning? input in the format 'year 1 fall', etc").strip().lower()
    semester_courses = [c for c in courses if c.year.lower() ==semester]
    print(course.code for course in semester_courses)
    for course in semester_courses:
        print(f"\n--- Checking {course.code} ---")
        course = course_map.get(course.code)

        if not course:
            print(f"Course '{course.code}' not found.")
            continue
        
        if course.code == "CSC 326" or course.code == "CSC 327":
            print("You must take CSC 326 and CSC 327 in the same semester")
            continue

        if not course.prerequisites:
            print(f"You are eligible for {course.code} — no prerequisites required.")
            continue

        unmet = []
        for prereq_code in course.prerequisites:
            prereq = course_map.get(prereq_code)
            if prereq and not prereq.is_passed:
                answer = input(f"Have you passed {prereq_code} - {prereq.name}? (y/n): ").strip().lower()
                if answer != "y":
                    unmet.append(prereq_code)
                else: prereq.is_passed = True

        if unmet:
            print(f"Not eligible for {course.code}: you have not passed {', '.join(unmet)}.")
        else:
            print(f"You are eligible for {course.code}!")
#change the wording & output scenarios to fit desired 2 yr forcast
# deal with the odd total lines