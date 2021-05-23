import pytools

def test_docker_is_installed():
    # Given
    command = 'docker --version'

    # When
    out, err = pytools.local_exec(command)

    # Then
    assert 'Docker' in str(out)

def test_docker_is_running():
    # Given
    command = 'docker ps'

    # When
    out, err = pytools.local_exec(command)

    # Then
    assert 'NAMES' in str(out)

def test_click_is_installed():
    # Given
    command = 'pip list | grep click'

    # When
    out, err = pytools.local_exec(command)

    # Then
    assert 'click' in str(out)

def test_ci_master_is_running():
    # Given
    command = 'docker ps | grep ci_master'

    # When
    out, err = pytools.local_exec(command)

    # Then
    assert 'ci_master' in str(out)

def test_ci_target_is_running():
    # Given
    command = 'docker ps | grep ci_target'

    # When
    out, err = pytools.local_exec(command)

    # Then
    assert 'ci_target' in str(out)

def test_deployer_ping_is_working():
    # Given
    command = './deployer.py ping -i False'

    # When
    out, err = pytools.local_exec(command)
    print("out: " + str(out.decode("utf-8")))

    # Then
    assert 'pong' in str(out)
