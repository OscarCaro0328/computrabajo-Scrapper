import requests
from bs4 import BeautifulSoup


my_set = {'1', '2', '3'}
print(my_set)
my_set.add('4')
print(my_set)
my_set.add('7')
print(my_set)
my_set.remove('2')
print(my_set)
my_set.add('0')
print(my_set)

# Create an empty dictionary
my_dict = {}

# Add elements to the dictionary
my_dict['apple'] = 2
my_dict['banana'] = 1
my_dict['orange'] = 3

# Print the dictionary
print(my_dict)  # {'apple': 1, 'banana': 2, 'orange': 3}

# Remove an element from the dictionary
del my_dict['banana']
my_dict['grape'] = '10'
# Print the updated dictionary
print(my_dict)  # {'apple': 1, 'orange': 3}

a = [1, 2, 3]
b = ['one', 'two', 'three']

pairs = zip(a, b)
print(pairs)
for pair in pairs:
    print(pair)

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
search_url = "https://co.computrabajo.com/ofertas-de-trabajo/?q=engineer&l=Bogot%C3%A1"

job_listings = []

# Loop through all the pages of the search results
for page_number in range(1, 11):
    page_url = f"{search_url}&p={page_number}"
    response = requests.get(page_url,headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract job listings from the current page
    listings = soup.find_all("article", {"class": "box_offer"})
    for listing in listings:
        job_title = listing.find("a", {"class": "js-o-link"}).text.strip()
        company_name = listing.find("span", {"class": "iE"}).text.strip()
        job_location = listing.find("span", {"class": "js-geo"}).text.strip()
        job_listings.append((job_title, company_name, job_location))

# Print the job listings
for listing in job_listings:
    print(listing)