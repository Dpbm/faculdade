#!/bin/bash
socat TCP4-LISTEN:8080,fork /tmp/test &
echo "Hello, world" | nc -4 -v localhost 8080
