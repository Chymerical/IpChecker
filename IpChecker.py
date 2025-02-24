#!/usr/bin/env python3
import ipaddress
import os
import sys
import argparse

#Default function to print the container's configured IP network from the CONTAINER_NETWORK environment variable or fall back to a default IP
def ip_network_report():
    container_ip_network = os.environ.get('CONTAINER_NETWORK','192.168.1.0/24')
    print(container_ip_network)

#Checking for collision after putting each IP adress to a list.
def collision_checker(file_path):

    networks = []

    try:
        file = open(file_path, 'r')
        for line in file:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith('#'):
                    try:
                        network = ipaddress.ip_network(line, strict=False)
                        networks.append(network)
                    except ValueError:
                        print(f"Invalid network format: {line}")
        file.close
        found_collision = False
        n = len(networks)
        # Checking for collision
        for i in range(n):
            for j in range(i+1, n):
                if networks[i].overlaps(networks[j]):
                    found_collision = True
                    print(f"Collision: {networks[i]} overlaps with {networks[j]}")
        if not found_collision:
            print("No collisions found.")
    except FileNotFoundError:
        print(f"File not found: {file_path}", file=sys.stderr)
        sys.exit()

def main():
    parser = argparse.ArgumentParser(
        description="IP Tool for reporting IP networks and detecting collisions"
    )
    parser.add_argument(
        '--check-collision', type=str, metavar='FILE',
        help="Provide the check collision argument and a file path"
    )
    args = parser.parse_args()

    if args.collision_checker:
        collision_checker(args.collision_checker)
    else:
        ip_network_report()

if __name__ == '__main__':
    main()