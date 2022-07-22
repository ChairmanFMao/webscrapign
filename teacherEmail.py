from bs4 import BeautifulSoup
import requests

# This gets all of the teachers names and email off the school website

teachers = {}

for k in range(1,5):
    text = requests.get(f"https://nottinghamhigh.co.uk/staff/page/{k}/").text
    
    soup = BeautifulSoup(text, "html.parser")
    table = soup.select(".team-members-list__table")
        
    for i in table[0].find_all("tr"):
        counter = 0
        name = ""
        for j in i.find_all("td"):
            if counter == 0:
                name = j.text.replace("<td>","").replace("</td>","").strip()
            if counter == 1:
                teachers[name] = j.text.replace("<td>","").replace("</td>","").strip()
            counter += 1

for i in teachers.keys():
    print(f"Name: {i}\nEmail: {teachers[i]}")