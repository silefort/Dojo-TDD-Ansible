#!/usr/bin/env python3
import click
import subprocess
import os
import json

__author__ = "Simon Lefort"

def local_exec(cmd):
    """
    Execute command locally
    """
    click.echo(cmd)
    os.system(cmd)

def fix_ssh_target(target):
    """
    Fix ssh connection to target
    https://blog.dafert.org/system-is-booting-up-see-pam_nologin/
    fix "System is booting up. See pam_nologin(8) message"
    """
    cmd = 'docker exec ' + target + ' rm -f /etc/nologin'
    local_exec(cmd)
    cmd = 'docker exec ' + target + ' rm -f /var/run/nologin'
    local_exec(cmd)

@click.group()
def main():
    """
    Simple CLI wrapper around my main deployment/development actions
    """
    pass

@main.command()
@click.option('--name','-n', default='', help='container name')
@click.option('--build','-b', default='False', help='build before running')
def run(name, build):
    """
    build/run the ci containers
    --name -n name of the service to run
    --build build the container
    """
    cmd = 'docker-compose rm -s -f ' + name
    local_exec(cmd)
    cmd = 'docker-compose up -d'
    if build == 'True':
        cmd = cmd + ' --build'
    cmd = cmd + ' ' + name
    local_exec(cmd)
    cmd = ' docker exec ci_master sh -c  "chmod 400 /app/ansible_forge/tools/docker/id_rsa"'
    local_exec(cmd)
    fix_ssh_target('ci_target')
    return

@main.command()
def stop():
    """
    stop all the running containers
    """
    cmd = 'docker-compose down'
    local_exec(cmd)
    return

@main.command()
@click.option('--interactive','-i', default='True', help='run docker exec with -it')
def ping(interactive):
    """
    ping target from master
    """
    inter = ''
    if interactive == "True":
        inter = ' -it'
    cmd = 'docker exec' + inter + ' -e ANSIBLE_HOST_KEY_CHECKING=False ci_master sh -c "ansible -m ping -i /app/ansible_forge/inventories/docker/inventory.yml all"'
    local_exec(cmd)
    return

@main.command()
@click.option('--playbook','-p', help='playbook name')
@click.option('--verbose','-v', default='False', help='ansible verbosity')
@click.option('--tags','-t', default='', help='ansible tags')
@click.option('--interactive','-i', default='True', help='run docker exec with -it')
def ansible(playbook, verbose, tags, interactive):
    """
    deploy ansible playbook to target
    """
    inter = ''
    if interactive == "True":
        inter = ' -it'
    cmd = ' docker exec' + inter + ' ci_master sh -c  "cd /app/ansible_forge; ANSIBLE_HOST_KEY_CHECKING=False /usr/bin/ansible-playbook'
    if tags != '':
        cmd = cmd + ' --tags "' + tags + '"'
    if verbose == 'True':
        cmd = cmd + ' -v'
    # cmd = cmd + ' -i inventories/docker/inventory.yml playbooks/'+ playbook +'.yml --key-file="tools/docker/id_ecdsa""'
    cmd = cmd + ' -i inventories/docker/inventory.yml playbooks/main.yml --key-file="tools/docker/id_ecdsa""'
    local_exec(cmd)
    return

@main.command()
def fix_ssh():
    """
    fix ssh connection to target ( check deployer code to understand why )
    """
    fix_ssh_target('ci_bootstrap_target')
    fix_ssh_target('ci_target')
    return

@main.command()
def test():
    """
    launch pytest tests
    """
    cmd = 'pytest tests -v'
    local_exec(cmd)
    return

@main.command()
def ssh_target():
    """
    ssh into ci_target
    """
    cmd = 'docker exec -it ci_master ssh -v deploy@ci_target -i /app/ansible_forge/tools/docker/id_rsa -p 1234 -o "StrictHostKeyChecking=no"'
    local_exec(cmd)
    return

if __name__ == "__main__":
    main()

