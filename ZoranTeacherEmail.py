import bs4
import requests

website = requests.get("https://nottinghamhigh.co.uk/staff/")
soup = bs4.BeautifulSoup(website.text, 'html.parser')
table = soup.select(".team-members-list__table")

for person in table[0].find_all("tr"):
    for col, val in zip(["Name:", "Email:", "", "", "Role:", ""], person.find_all("td")):
        if col:
            print(col, val.text.strip())
    print()
