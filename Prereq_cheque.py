
#create prerequisite map and apply it to courses listed in course_objects

def check_eligibility(courses: list, semester: str, semester_order: list) -> None:
    course_map = {c.code: c for c in courses}
    def mark_prereqs_passed(code, course_map): #recursive function to mark previous classes as passed
        course = course_map.get(code)
        if not course:
            return
        course.is_passed = True
        for prereq_code in course.prerequisites:
            mark_prereqs_passed(prereq_code, course_map)
    
    semester_courses = [c for c in courses if c.year.lower() ==semester]
    print(course.code for course in semester_courses)
    unmet = [] 
    if semester in semester_order:
        current_index = semester_order.index(semester)
        prior_semesters = semester_order[:current_index]
        #verify previous semesters 
        for prior_semester in reversed(prior_semesters):
            prior_courses = [c for c in courses if c.year.lower() == prior_semester]
            is_prerequisite = [c for c in prior_courses if any(c.code in other.prerequisites for other in courses)]
            not_prerequisite = [c for c in prior_courses if not any(c.code in other.prerequisites for other in courses)]
            if not prior_courses:
                continue
            print(f"\n--- Verifying {prior_semester.title()} ---")
            for course in (is_prerequisite):
                if not course.is_passed:
                    answer = input(f"Have you passed {course.code} - {course.name}? (y/n): ").strip().lower()
                    if answer == "y":
                        mark_prereqs_passed(course.code, course_map)
                    else: unmet.append(course) 
            for course in not_prerequisite:
                course.is_passed == True
                    

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

        
        for prereq_code in course.prerequisites:
            prereq = course_map.get(prereq_code)
            if prereq and not prereq.is_passed:
                answer = input(f"Have you passed {prereq_code} - {prereq.name}? (y/n): ").strip().lower()
                if answer != "y":
                    unmet.append(prereq_code)
                else: mark_prereqs_passed(prereq_code, course_map)

        if unmet:
            print(f"Not eligible for {course.code}: you have not passed {', '.join(unmet)}.")
        else:
            print(f"You are eligible for {course.code}!")

