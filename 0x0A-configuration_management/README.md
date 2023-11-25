# Puppet Tasks

This repository contains tasks for managing systems with Puppet.

## Task 0: Create a File

**File:** `0-create_a_file.pp`

**Description:** Using Puppet, create a file in `/tmp`.

**Requirements:**
- File path: `/tmp/school`
- File permission: 0744
- File owner: `www-data`
- File group: `www-data`
- File contains: `I love Puppet`

## Task 1: Install a Package

**File:** `1-install_a_package.pp`

**Description:** Using Puppet, install `flask` from `pip3`.

**Requirements:**
- Install `flask`
- Version: 2.1.0

## Task 2: Execute a Command

**File:** `2-execute_a_command.pp`

**Description:** Using Puppet, create a manifest that kills a process named `killmenow`.

**Requirements:**
- Must use the `exec` Puppet resource
- Must use `pkill`

## Repository Information

- **GitHub Repository:** `alx-system_engineering-devops`
- **Directory:** `0x0A-configuration_management`

