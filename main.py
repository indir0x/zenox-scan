from scanner.discovery import discover_hosts

def main():
    rede = input("Digite a rede (ex: 192.168.0.0/24 ou domínio): ")
    hosts_ativos = discover_hosts(rede)

    print("\n--- Hosts encontrados ---")
    for ip in hosts_ativos:
        print(f"[+] {ip}")

if __name__ == "__main__":
    main()
