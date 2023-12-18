# Firewall Configuration Project

## Overview
This project focuses on setting up and configuring firewalls using UFW (Uncomplicated Firewall) on web servers. The main goal is to secure the servers by allowing only specific traffic based on predetermined rules.

### Resources
- [What is a firewall?](https://en.wikipedia.org/wiki/Firewall_(computing))

### Tools
- Telnet
- UFW (Uncomplicated Firewall)

## Important Information
- **Network Restrictions**: Some networks have firewalls that may block certain types of traffic.
- **Warning**: Incorrect firewall settings, especially those related to SSH (port 22), can lead to lockout from the server.

### Quiz Questions
Quiz questions related to firewall concepts and configurations are included.

## Server Information
- `361041-web-01` (Ubuntu, IP: 100.25.171.213)
- `361041-web-02` (Ubuntu, IP: 184.73.99.187)
- `361041-lb-01` (Ubuntu, IP: 100.26.177.120)

## Tasks
### Task 0: Block All Incoming Traffic But
- **Objective**: Configure UFW to block all incoming traffic except for specific TCP ports.
- **Requirements**:
  - The configuration is primarily for `web-01`.
  - Allow only TCP ports 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).
  - Include UFW command documentation.

### Repository and Submission
- **GitHub Repository**: `alx-system_engineering-devops`
- **Directory**: `0x13-firewall`
- **File**: `0-block_all_incoming_traffic_but`

## Notes
- Be cautious when modifying firewall rules. Ensure continuous access to the server, especially via SSH (port 22).


