
# Aula 01 - Python aplicado ao monitoramento

hosts = [
    {"nome": "SW-CORE-01", "status": "online"},
    {"nome": "SW-ACCESS-02", "status": "offline"},
    {"nome": "LINK-ISP-01", "status": "online"},
    {"nome": "FIREWALL-01", "status": "offline"}
]

total_offline = 0

print("=== MONITORAMENTO DE HOSTS ===")

for host in hosts:
    if host["status"] == "offline":
        total_offline += 1
        print(f"ALERTA: {host['nome']} está offline!")

print("\n=== RESUMO ===")
print(f"Total de hosts: {len(hosts)}")
print(f"Hosts online: {len(hosts) - total_offline}")
print(f"Hosts offline: {total_offline}")