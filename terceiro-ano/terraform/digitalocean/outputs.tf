output "ip_server1"{
  value = digitalocean_droplet.test.ipv4_address
  description="Ip do servidor 1"
}

output "ip_server2"{
  value = digitalocean_droplet.test2.ipv4_address
  description="Ip do servidor 2"
}
