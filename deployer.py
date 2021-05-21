#!/usr/bin/env python3
import click
import os

__author__ = "Simon Lefort"

def local_exec(cmd):
    """
    Execute command locally
    """
    click.echo(cmd)
    os.system(cmd)

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
    # fix_ssh_target('ci_bootstrap_target')
    # fix_ssh_target('ci_target')
    return

if __name__ == "__main__":
    main()
