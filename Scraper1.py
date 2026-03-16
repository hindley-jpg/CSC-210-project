import requests
from bs4 import BeautifulSoup
from model import Course
def scrape_computer_science_curriculum(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Locate the tbody tag
        all_tbodyies = soup.find_all('tbody')
       
        if not all_tbodyies:
            print("Could not find the <tbody> tag in the provided URL.")
            return []

        curriculum_data = []
        for tbody in all_tbodyies: 
            year_header = tbody.find_previous(['h2', 'h3', 'h4'])
            year_label = year_header.get_text(strip=True) if year_header else "Unknown Year"
        # Iterate through each table row (tr) within the tbody
            for row in tbody.find_all('tr'):
            # Find all table data cells (td) in the row
                cells = row.find_all('td')
                if len(cells) >= 3:
                    course_info = {
                        "year": year_label,
                        "code": cells[0].get_text(strip=True),
                        "course": cells[1].get_text(strip=True),
                        "credits": cells[2].get_text(strip=True)
                    }
                    curriculum_data.append(course_info)
        
        return curriculum_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

# Target URL
url = "https://engineering.catholic.edu/academics/undergraduate/computer-science/comp-sci-curriculum/index.html"

# Execute the scraper
data = scrape_computer_science_curriculum(url)
for item in data: print(item) #need to deal with the weird totals
#option to filter results
def filter_curriculum(course_list, key, value):
    return [item for item in course_list if value.lower() in item[key].lower()]
#Freshman_fall = filter_curriculum(data,"year", "Year 1 Fall")
#print(Freshman_fall)

#list of objects for each course scraped
course_objects = [Course(code=item['code'], name=item['course'], num_credits=int(item['credits'])) for item in data]


# 3. Verify it worked by accessing an attribute
print(f"Total objects created: {len(course_objects)}")
if course_objects:
    print(f"First course code: {course_objects[0].code}")
