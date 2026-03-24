class Course: #creating course class to hold course objects from scrape
    def __init__(self, code, name, num_credits, year, prerequisites=None, is_passed=False, complete=False,):
        self.code = code
        self.name = name
        self.num_credits = num_credits
        self.prerequisites = prerequisites
        self.is_passed = is_passed
        self.complete = complete
        self.year = year