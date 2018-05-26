#!/bin/bash
until lt $2 --port 5000 --subdomain campgrounds; do
echo "Server 'myserver' crashed with exit code $?.  Respawning.." >&2
sleep 1
done
