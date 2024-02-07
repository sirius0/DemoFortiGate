import requests
from pprint import pprint

# Ce script est conçu pour configurer via l'API un FortiGate afin de
# modifier l'addresse IP et les services accessibles depuis le port 1.

URL = "https://192.168.1.72"
request = f"{URL}/api/v2/cmdb/system/interface/port1"
API_TOKEN = "pjzw8j9tH8Nm1H9gj96kN58Q61r7dk"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Payload to change the IP and the administrative access of port 1
data = {
    "ip": "10.1.1.20/255.255.255.0",
    "fortilink-split-interface": "disable",
    "allowaccess" : "http https ssh fgfm ping"
}

try:
    requests.packages.urllib3.disable_warnings()
    response = requests.put(request, headers=headers, json=data, verify=False)

    if response.status_code in [200, 204]:
        print("La mise à jour de l'interface a réussi.")
    else:
        pprint(f"Erreur lors de la requête: {response.status_code}, Réponse du serveur: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Erreur de requête: {e}")
