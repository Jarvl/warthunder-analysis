import os
import requests
from bs4 import BeautifulSoup

wt_wiki_url = 'https://wiki.warthunder.com/'
vehicle_link_selector = '#mw-content-text > div.mw-parser-output > table > tbody > tr:not(:first-child) > td:nth-child(2) > a'

def fetch_url(url: str):
  response = requests.get(url)
  response.raise_for_status()
  return response.text

def dump_list_to_file(items: list, file_path: str, mode='w'):
  with open(file_path, mode) as f:
    f.write("\n".join(items))

def generate_premium_ground_vehicle_links():
  html = fetch_url(f"{wt_wiki_url}Category:Premium_ground_vehicles")
  soup = BeautifulSoup(html, 'html5lib')
  a_tags = soup.css.select(vehicle_link_selector)
  return [f"{wt_wiki_url}{a.get('href').lstrip('/')}" for a in a_tags]

pgv_links = generate_premium_ground_vehicle_links()
pgv_links_file_path = os.path.join(os.path.dirname(__file__), 'data/premium_ground_vehicle_links.txt')
dump_list_to_file(pgv_links, pgv_links_file_path)


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