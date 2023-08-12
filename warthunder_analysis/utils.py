import os
import requests
from bs4 import BeautifulSoup


WT_WIKI_URL = 'https://wiki.warthunder.com/'
VEHICLE_LINKS_SELECTOR = '#mw-content-text > div.mw-parser-output > table > tbody > tr:not(:first-child) > td:nth-child(2) > a'

def fetch_url(url: str):
  response = requests.get(url)
  response.raise_for_status()
  return response.text

def dump_list_to_file(items: list, file_path: str, mode='w'):
  with open(file_path, mode) as f:
    f.write("\n".join(items))

def generate_premium_ground_vehicle_links():
  html = fetch_url(f"{WT_WIKI_URL}Category:Premium_ground_vehicles")
  soup = BeautifulSoup(html, 'html5lib')
  a_tags = soup.css.select(VEHICLE_LINKS_SELECTOR)
  return [f"{WT_WIKI_URL}{a.get('href').lstrip('/')}" for a in a_tags]
