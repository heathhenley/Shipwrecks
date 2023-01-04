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


if __name__ == "__main__":
  for name, info in all_wrecks_dict_from_file().items():
    print(name, *info)
