import pytools

def test_docker_is_installed():
    # Given
    command = 'docker --version'

    # When
    out, err = pytools.local_exec([command])

    # Then
    assert 'Docker' in str(out)

def test_docker_is_running():
    # Given
    command = 'docker ps'

    # When
    out, err = pytools.local_exec([command])

    # Then
    assert 'NAMES' in str(out)
