resource "digitalocean_droplet" "test" {
  name   = "ax-1"
  size   = "${var.size}"
  image  = "${var.image}"
  region = "${var.region}"
  ssh_keys=[digitalocean_ssh_key.pub_key.fingerprint]
}

resource "digitalocean_droplet" "test2" {
  name   = "ax-2"
  size   = "${var.size}"
  image  = "${var.image}"
  region = "${var.region}"
  ssh_keys=[digitalocean_ssh_key.pub_key.fingerprint]
}
