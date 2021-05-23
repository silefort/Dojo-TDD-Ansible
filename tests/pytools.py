import subprocess

def local_exec(instructions):
    """
    Execute command locally
    @param instructions a list of command to execute
    @return tuple(stdout, stderr)
    """
    inst = [instructions, "exit"]

    tty = subprocess.Popen(";".join(inst),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = tty.communicate()
    return (stdout, stderr)

def get_ansible_target_ip():
    out, err = local_exec(["host ansible_target | awk '{ print $NF }'"])
    return out.rstrip()

def target_exec(instructions):
    """
    Execute command locally
    @param instructions a list of command to execute
    @return tuple(stdout, stderr)
    """
    cmd = 'docker exec -t ci_master ssh deploy@ci_target -i /app/ansible_forge/tools/docker/id_rsa -p 1234 -o "StrictHostKeyChecking=no" ' + instructions
    return local_exec(cmd)
