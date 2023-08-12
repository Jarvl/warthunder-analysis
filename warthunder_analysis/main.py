import requests
from bs4 import BeautifulSoup

def fetch_url(url):
  response = requests.get(url)
  response.raise_for_status()
  return response.text

vehicle_link_selector = '#mw-content-text > div.mw-parser-output > table > tbody > tr:not(:first-child) > td:nth-child(2) > a'


wt_wiki_url = 'https://wiki.warthunder.com/'
premium_ground_vehicles_html = fetch_url(wt_wiki_url+'Category:Premium_ground_vehicles')
pgv_soup = BeautifulSoup(premium_ground_vehicles_html, 'html5lib')

vehicle_link_els = pgv_soup.css.select(vehicle_link_selector)
links = [wt_wiki_url+link.get('href').lstrip('/') for link in vehicle_link_els]

print(links)



"""
Need to pull the following:
- Vehicle name
- Country
- Type of tank
- Rank
- BR for each game mode
- Cost (pull from "Purchase" on page, if exists)
- Wheels vs treads
- Hull armor (front/side/back)
- Turret armor (front/side/back)
- Crew members
- Visibility
- Horizontal guidance
- Vertical guidance
- Is amphibious
- Forward speed (AB)
- Forward speed (RB/SB)
- Back speed (AB)
- Back speed (RB/SB)
- Engine power (AB)
- Engine power (RB/SB)
- Power-to-weight ratio (AB)
- Power-to-weight ratio (RB/SB)
- Weight (tons)
- Repair cost (AB)
- Repair cost (RB/SB)
- Crew training
- Crew training (Expert)
- Crew training (Aces)
- Crew training (Research Aces)
- Modifications list
- First stage ammunition amount (maybe?)
- Reload time
- Max ammo
- Has stabilizer
- Fire rate
- Ammunitions
  - name
  - type
  - pen @ 10m
  - pen @ 100m
  - pen @ 500m
  - pen @ 1000m
  - pen @ 1500m
  - pen @ 2000m
  - projectile velocity
  - projectile mass
  - fuse delay
  - fuse sensitivity
  - explosive mass
  - degrees richochet 0% chance 
  - degrees richochet 50% chance 
  - degrees richochet 100% chance 
- coax machine gun caliber
- has mounted MG

"""