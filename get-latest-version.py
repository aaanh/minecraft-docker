import json
import requests
import sys
import os
from datetime import date

print("Python Script: Retrieve Minecraft Server Latest Version")
print("Copyright (C) ", date.today().year, " ", "Anh Hoang Nguyen")
print("-----------------------------------------------------")

res = requests.get('https://launchermeta.mojang.com/mc/game/version_manifest.json')

print('Version manifest GET status: ', res.status_code)

version_manifest = json.loads(res.text)
latest_version = version_manifest['latest']['release']

print('Latest version: ', latest_version)

latest_version_id = version_manifest['versions'][0]['id']

# if (latest_version_id == latest_version):
#     print('Latest version check: OK')
# else:
#     print('Latest version check: FAIL')
#     exit(1)

latest_version_manifest_url = version_manifest['versions'][0]['url']

print('Latest version manifest URL: ', latest_version_manifest_url)

res = requests.get(latest_version_manifest_url)

latest_version_download_url = json.loads(res.text)["downloads"]["server"]["url"]

print('Latest version download URL: ', latest_version_download_url)

# check if set_latest_version file exists

with open('set_latest_version.txt', 'w') as f:
    f.write(latest_version_download_url)


print("Script finished.")
exit(0)