print("         rede - intervalo de hosts - broadcast")

net = 0
for i in range(8):
    print(f"{i+1} = 10.240.100.{net} - 10.240.100.{net+1} a 10.240.100.{net+30} - 10.240.100.{net+31}")
    net += 32
