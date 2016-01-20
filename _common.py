import sys
import subprocess


__all__ = ['log_info', 'handle_error', 'run_command', ]


def log_info(msg):
    sys.stdout.write('* {}\n'.format(msg))
    sys.stdout.flush()


def handle_error(msg):
    sys.stderr.write('* {}\n'.format(msg))
    sys.exit(1)


def run_command(command, ignore_error=False, return_stdout=False):
    if not isinstance(command, (list, tuple)):
        command = [command, ]
    command_str = ' '.join(command)
    log_info('Running command {}'.format(command_str))
    try:
        stdout = subprocess.check_output(command)
    except subprocess.CalledProcessError as err:
        if not ignore_error:
            handle_error('Command failed: {}'.format(err))
    else:
        return stdout.decode() if return_stdout else None
