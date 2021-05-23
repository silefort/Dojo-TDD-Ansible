import subprocess

def local_exec(instructions):
    ""
    Execute command locally
    @param instructions a list of command to execute
    @return tuple(stdout, stderr)
    ""
    instructions.append("exit")

    tty = subprocess.Popen(";".join(instructions),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = tty.communicate()
    return (stdout, stderr)

def get_ansible_target_ip():
    out, err = local_exec(["host ansible_target | awk '{ print $NF }'"])
    return out.rstrip()
