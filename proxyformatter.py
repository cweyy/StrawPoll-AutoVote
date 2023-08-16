import json

# Lese die JSON-Datei
with open('proxies.json', 'r') as json_file:
    proxy_data = json.load(json_file)

# Erstelle eine Liste für die formatierten Proxies
formatted_proxies = []

# Iteriere durch jede Proxy-Information und formatiere sie
for proxy in proxy_data:
    proxy_ip = proxy['ip']
    proxy_port = proxy['port']
    formatted_proxy = f"{proxy_ip}:{proxy_port}"
    formatted_proxies.append(formatted_proxy)

# Schreibe die formatierten Proxies in die proxies.txt-Datei
with open('proxies.txt', 'w') as txt_file:
    txt_file.write('\n'.join(formatted_proxies))

print("Proxies wurden erfolgreich in proxies.txt gespeichert.")
