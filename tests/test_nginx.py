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
