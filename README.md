# env

[![Build Status](https://travis-ci.com/iroquoisorg/ansible-role-env.svg?branch=master)](https://travis-ci.com/iroquoisorg/ansible-role-env)

Ansible role for env

This role was prepared and tested for Ubuntu 16.04.

# Installation

`$ ansible-galaxy install iroquoisorg.env`

# Default settings

```
---
env_hostname: ""
env_vars: []
env_timezone: "Etc/UTC"
env_cron_jobs: []  # {job: "git status", name: "job name", user: "www-data", minute: "*", hour: "*", day: "*", weekday: "*", month: "*" }
env_hosts: []  # {ip: "127.0.0.1", host: "localhost"}
env_cron_host: false

```

# Development

Please check [development guide](DEVELOPMENT.md) for details about developing and testing this role.
