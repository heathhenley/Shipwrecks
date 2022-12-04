import json
import re


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

def generate_wreck_dict_from_file():
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

# insert / update in django model
def insert_update(wrecks_model):
  for name, (year, lat, lon, wds) in generate_wreck_dict_from_file().items():
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



if __name__ == "__main__":
  for name, info in generate_wreck_dict_from_file().items():
    print(name, *info)
