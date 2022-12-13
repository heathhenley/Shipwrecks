import json
import re
import requests


URL = "https://beavertaillight.org/wrecks"
RE_LATLON = r"(?P<lat>[\d]{1,3}\-[\d]{1,3}\-[\d]{1,3}(\.\d{1,3}){0,1}[NnSs])\s(?P<lon>[\d]{1,3}\-[\d]{1,3}\-[\d]{1,3}(\.\d{1,3}){0,1}[WwEe])"
filename = r"rhode_island_wreck_database_beavertail.json"


# Convert between min/seconds rep to decimal
def ll_to_decimal(ll_str):
  ll, mins, secs = ll_str.split("-")
  l = secs[-1]
  sign = -1.0 if l in "SsWw" else 1.0
  secs = secs[:-1]
  return sign * (float(ll) + float(mins) / 60 + float(secs) / 3600)

# This generates a list of wrecks in the json file that contain a lat / lon
# string that matches the regex format above in their "location" field
def wrecks_with_loc_dict_from_file():
  data = None
  wreck_dict = {}
  with open(filename) as f:
    data = json.load(f)
    wrecks = data["data"]
    for wreck in wrecks:
      find_lat_lon = re.search(RE_LATLON, wreck['location'])
      if find_lat_lon:
        lat = ll_to_decimal(find_lat_lon.group('lat'))
        lon = ll_to_decimal(find_lat_lon.group('lon'))
        name, year = wreck["vname"], wreck["ylost"]
        wds = f"{URL}/r{wreck['region']}/{wreck['datasheet'].replace(' ', '%20')}"
        if name not in wreck_dict:
          wreck_dict[name] = (year, lat, lon, wds)
  return wreck_dict

# read all wrecks in - just looking to update wds here not location - used by
# the update add wds function below
def all_wrecks_dict_from_file():
  data = None
  wreck_dict = {}
  with open(filename) as f:
    data = json.load(f)
    wrecks = data["data"]
    for wreck in wrecks:
        name, year = wreck["vname"], wreck["ylost"]
        wds = f"{URL}/r{wreck['region']}/{wreck['datasheet'].replace(' ', '%20')}"
        if name not in wreck_dict:
          wreck_dict[name] = (year, None, None, wds)
  return wreck_dict

# insert / update in django model
# this is just a helper to update / insert all the wrecks that had locations in
# the json data
def insert_update_all_fields(wrecks_model):
  for name, (year, lat, lon, wds) in wrecks_with_loc_dict_from_file().items():
    obj, created = (wrecks_model.objects
                      .filter(vessel_name__iexact=name)
                      .update_or_create(
                        vessel_name=name,
                        year=year if year != '' else None,
                        latitude=lat,
                        longitude=lon,
                        beavertail_link=wds
                      ))
    print(created)
    print(obj)

def update_add_wds(wrecks_model):
  update_counter = 0
  for name, (year, _, _, wds) in all_wrecks_dict_from_file().items():
    try:
      wreck = wrecks_model.objects.get(vessel_name__iexact=name)
      print(f"{name} in db already...")
      if wreck.beavertail_link == '':
        print(f"wds empty, update with: {wds}")
        update_counter += 1
        wreck.beavertail_link = wds
        wreck.save()
    except:
      print(f"{name} not in db")
  print(f"Updated: {update_counter} records.")

def update_add_wreckhunter_link(wrecks_model):
  update_counter = 0
  wrecks = wrecks_model.objects.all()
  for wreck in wrecks:
    if wreck.wreckhunter_link == '':
      name = (str(wreck.vessel_name).lower().replace(' ', '')
              .replace('.', '').replace('uss', ''))
      path = f"https://wreckhunter.net/DataPages/{name}-dat.htm"
      res = requests.get(path)
      #print(res.status_code)
      if res.status_code == 200:
        print("Found a valid page!")
        print(path)
        wreck.wreckhunter_link = path
        wreck.save()
        update_counter += 1
  print(f"Updated: {update_counter} records.")

def fix_wreckhunter_links(wreck_model):
  for wreck in wreck_model.objects.all():
    if wreck.wreckhunter_link != "":
      new_link = str(wreck.wreckhunter_link).replace('http:', 'https:')
      wreck.wreckhunter_link = new_link
      wreck.save()

if __name__ == "__main__":
  for name, info in generate_wreck_dict_from_file().items():
    print(name, *info)
