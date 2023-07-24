import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://allotrough.atlassian.net/rest/api/3/issue/T2-1"

auth = HTTPBasicAuth("allotrough@gmail.com", "ATATT3xFfGF0OCKi1LAGZh9kF5Yz76FI6nTZ99ZuimBHLf_1FDpjk-CXmcl73-qsK32MtgQzM0ywQ6VrLLKp_3qAOcIN8g6K4gKmaeAgQ0C_jFdrt2In2W-X4AjBd2tTYJ7KELgG3rFzOvjODXQWhQeDJ757Xz25ENKsJG4TYkAtTZx5tMBpA_w=AE3A039A")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))