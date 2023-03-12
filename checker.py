import requests
import sys

cve_id = sys.argv[1]

url = f"http://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}"

response = requests.get(url)


if response.status_code == 200:
    # CVE exists, print the details
    cve_data = response.json()['result']['CVE_Items'][0]['cve']
    print(f"CVE found:\n{cve_data}")
else:
    # CVE not found, print an error message
    print(f"CVE {cve_id} not found")
