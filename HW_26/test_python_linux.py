import argparse
import sys
import subprocess
import os


def test_ip_info():
    # argument = args()
    content = subprocess.Popen(["ifconfig", "enp0s8"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    assert '10.0.3.15' in content
    print(content)


def test_route_info():
    content = subprocess.Popen(["ip", "r"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    assert '10.0.3.2' in content
    print(content)


def test_proc_info():
    content = subprocess.Popen(["lscpu"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    assert 'i7-4770' in content
    print(content)


def test_process_info():
    content = subprocess.Popen(["ps", "5374"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    print(content)


def test_ps():
    content = os.popen("ps -Af |wc -l").read()
    assert int(content) > 0
    print(content)


def test_net_stat():
    content = subprocess.Popen(["netstat", "-i"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    assert 'enp0s8' in content
    print(content)


def test_service_status():
    status = os.popen("systemctl status apache2.service").read()
    assert 'running' in status
    print(status)


def test_tcp_state():
    content = os.popen("lsof -i | grep TCP").read()
    assert 'LISTEN' in content
    print(content)


def test_pkg_version():# pkg_name
    content = os.popen('dpkg -s {}'.format('python')).read()
    assert 'Package: python' in content
    print(content)


def test_dir(): # dir_path
    content = subprocess.Popen(["ls", "/var/log/"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    print(content)


def test_pwd():
    content = subprocess.Popen(["pwd"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    assert "/home/ivan/QAu/otus_qa_course/otus_qa_course" in content
    print(content)


def test_core_version():
    content = subprocess.Popen(["uname", "-r"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    assert "4.18.0-25-generic" in content
    print(content)


def test_os_version():
    content = subprocess.Popen(["lsb_release", "-a"], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    assert 'Ubuntu 18.04.2 LTS' in content
    print(content)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='test')
# parser.add_argument('-g', '--global')
pkvg = subparsers.add_parser('pkv')
pkvg.add_argument('-n', '--name')


# Create a test_ip_info subcommand
parser_test_ip_info = subparsers.add_parser('i', help='Verify IP address')
parser_test_ip_info.set_defaults(func=test_ip_info)

# Create a test_route_info subcommand
parser_test_route_info = subparsers.add_parser('r', help='Show default route')
parser_test_route_info.set_defaults(func=test_route_info)

# Create a test_proc_info subcommand
parser_test_proc_info = subparsers.add_parser('test_proc_info', help='Show process state')
parser_test_proc_info.set_defaults(func=test_proc_info)


# Create a test_process_info subcommand
parser_test_process_info = subparsers.add_parser('pi', help='Show process info')
parser_test_process_info.set_defaults(func=test_process_info)

# Create a test_ps subcommand
parser_test_ps = subparsers.add_parser('ps', help='Show all processes')
parser_test_ps.set_defaults(func=test_ps)

# Create a test_net_stat subcommand
parser_test_net_stat = subparsers.add_parser('nt', help='Show net stats')
parser_test_net_stat.set_defaults(func=test_net_stat)

# Create a test_service_status subcommand
parser_test_service_status = subparsers.add_parser('sst', help='Show service status')
parser_test_service_status.set_defaults(func=test_service_status)

# Create a test_tcp_state subcommand
parser_test_tcp_state = subparsers.add_parser('tcp', help='Show tcp state')
parser_test_tcp_state.set_defaults(func=test_tcp_state)

# Create a test_pkg_version subcommand
parser_test_pkg_version = subparsers.add_parser('pkv', help='Show pkg version')
parser_test_pkg_version.set_defaults(func=test_pkg_version)

# Create a test_dir subcommand
parser_test_dir = subparsers.add_parser('d', help='Show list of files in directory')
parser_test_dir.set_defaults(func=test_dir)

# Create a test_pwd subcommand
parser_test_pwd = subparsers.add_parser('p', help='Show current directory')
parser_test_pwd.set_defaults(func=test_pwd)

# Create a test_core_version subcommand
parser_test_core_version = subparsers.add_parser('cv', help='Show core version')
parser_test_core_version.set_defaults(func=test_core_version)

# Create a test_os_version subcommand
parser_test_os_version = subparsers.add_parser('osv', help='Show OS version')
parser_test_os_version.set_defaults(func=test_os_version)


if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()
options.func()
