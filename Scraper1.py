import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
from model import Course
def scrape_computer_science_curriculum(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        main_body = soup.find('div', class_='main-body')
        curriculum_data = []
        label_node = None
        for child in main_body.children:
            if isinstance(child, NavigableString) and "Fall 2023 or later" in child:
                label_node = child
                break
            elif hasattr(child, 'get_text') and "Fall 2023 or later" in child.get_text():
                label_node = child
                break
        # Locate the tbody tag
        if label_node:
          for sibling in label_node.find_next_siblings():
            for tbody in sibling.find_all("tbody"): 
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
#option to filter results

#list of objects for each course scraped
course_objects = [Course(code=item['code'], name=item['course'], num_credits=int(item['credits']),year=item['year']) for item in data]


# 3. Verify it worked by accessing an attribute
print(f"Total objects created: {len(course_objects)}")
if course_objects:
    print(f"First course code: {course_objects[0].year}")
