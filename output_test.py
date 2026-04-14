def recommend_course_plans(courses: list, semester: str, semester_order: list) -> None:
    course_map = {c.code: c for c in courses}

    # Find the 3 semesters following the current one
    if semester not in semester_order:
        print(f"Semester '{semester}' not recognized.")
        return

    current_index = semester_order.index(semester)
    future_semesters = semester_order[current_index : current_index + 5]

    if not future_semesters:
        print("No future semesters to plan for.")
        return

    # Build a plan: for each future semester, determine eligible and ineligible courses
    def build_plan(course_map):
        plan = {}
        for semester in future_semesters:
            semester_courses = [c for c in courses if c.year.lower() == semester]
            eligible = []
            ineligible = []
            total_credits = 0

            for course in semester_courses:
                prereqs_met = all(
                    course_map[p].is_passed
                    for p in course.prerequisites
                    if p in course_map
                )
                #check that total credits does not exceed 18
                if prereqs_met:
                    if total_credits + course.num_credits <= 18:
                         eligible.append(course)
                         total_credits += course.num_credits
                    else: 
                        ineligible.append(course)#too many credits
                else:
                    ineligible.append(course)

            plan[semester] = {"eligible": eligible, "ineligible": ineligible, "total_credits": total_credits}
        return plan

    #output function controlling plan print
    print("Generating possible course plan for the next 3 semesters...")
    plan = build_plan(course_map)
    for semester, data in plan.items():
        print(f"\n  {semester.title()}")
        print(f"\n total credits: {data['total_credits']}/18")
        if data["eligible"]:
            print("  Eligible courses:")
            for c in data["eligible"]:
                print(f"    - {c.code}: {c.name}")

        if data["ineligible"]:
            print("  Courses with unmet prerequisites:")
            for c in data["ineligible"]:
                unmet = [p for p in c.prerequisites if not course_map.get(p, None) or not course_map[p].is_passed]
                if unmet:
                    print(f"    - {c.code}: {c.name} (missing: {', '.join(unmet)})")
                else:
                        print(f"    - {c.code}: {c.name} (would exceed 18 credit cap)")

    print()
      