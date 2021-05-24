import pytools

## 
# pytools.local_exec(command) : can execute command locally (on my machine)
# pytools.target_exec(command) : can execute command in the target

def test_always_true():
    # Given
    command = 'date'

    # When
    out, err = pytools.target_exec(command)

    # Then
    assert '20' in str(out)

def test_nginx_is_installed():
    # Given
    command = 'nginx -V'

    # When
    out, err = pytools.target_exec(command)
    print(out)

    # Then
    assert 'version: nginx' in str(out)

def test_nginx_is_running():
    # Given
    command = 'systemctl status nginx'

    # When
    out, err = pytools.target_exec(command)
    print(out)

    # Then
    assert 'active (running)' in str(out)

def test_nginx_is_listening_on_8080():
    # Given
    command = 'curl ci_target:8080/hello'

    # When
    out, err = pytools.master_exec(command)
    print(out)

    # Then
    assert 'world' in str(out)
