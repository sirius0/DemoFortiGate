import requests
from pprint import pprint

# Ce script est conçu pour interroger via l'API un FortiGate afin de 
# récupérer la liste de toutes les adresses de pare-feu configurées.

URL = "https://192.168.1.72"
request = f"{URL}/api/v2/cmdb/firewall/address"
API_TOKEN = "pjzw8j9tH8Nm1H9gj96kN58Q61r7dk"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

try:
    requests.packages.urllib3.disable_warnings()
    response = requests.get(request, headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()
        pprint(data)

    else:
        print(f"Erreur lors de la requête: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erreur de requête: {e}")
