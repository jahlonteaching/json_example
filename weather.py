import json
import requests


url = "https://api.open-meteo.com/v1/forecast?latitude=4.6473&longitude=-74.0962&hourly=temperature_2m,precipitation&" \
      "timezone=auto&start_date=2022-10-24&end_date=2022-10-28"
response = requests.get(url)
data = json.loads(response.text)

print(json.dumps(data, indent=4))
