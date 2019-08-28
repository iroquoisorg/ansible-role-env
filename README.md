# env

[![Build Status](https://travis-ci.com/iroquoisorg/ansible-role-env.svg?branch=master)](https://travis-ci.com/iroquoisorg/ansible-role-env)

Ansible role for env

This role was prepared and tested for Ubuntu 16.04.

# Installation

`$ ansible-galaxy install iroquoisorg.env`

# Usage

## Environment variables

To set global environment variables, use `env_vars` variable in a following way:

```
env_vars:
    VARIABLE: 'value'
    OTHER_VARIABLE: 'some_value'
```

This role will update variables' value if necessary.

## Pam environment variables - .pam_environment

In case you want to narrow down visibility of your environment variables to only one user (for example: www-data) and not 
expose them to everyone use env_pam_users option to set it. Read more: https://help.ubuntu.com/community/EnvironmentVariables#A.2BAH4-.2F.pam_environment

```
env_pam_users:
  - { name: "www-data", "template": "pam-environment.www-data.j2" }
```

Or for multiple users:

```
env_pam_users:
  - { name: "www-data", "template": "pam-environment.www-data.j2" }
  - { name: "test-user", "template": "pam-environment.test-user.j2" }
```

Place environment variables in a pam-env file located in your templates folder. They get overwritten with every deploy.

# Default settings

```
---
env_hostname: ""
env_vars: {}
env_timezone: "Etc/UTC"
env_cron_jobs: []  # {job: "git status", name: "job name", user: "www-data", minute: "*", hour: "*", day: "*", weekday: "*", month: "*" }
env_hosts: []  # {ip: "127.0.0.1", host: "localhost"}
env_cron_host: false
env_pam_users: []

```

# Development

Please check [development guide](DEVELOPMENT.md) for details about developing and testing this role.
