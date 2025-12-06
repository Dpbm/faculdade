#!/usr/bin/env bash

set -e

echo "init..."
sudo pacman-key --init
echo "populate..."
sudo pacman-key --populate
echo "install keyring..."
sudo pacman -Sy archlinux-keyring --noconfirm
echo "update..."
sudo pacman -Su --noconfirm
echo "install remaning packages..."
sudo pacman -Syyu jupyterlab python3 python-pip --noconfirm
