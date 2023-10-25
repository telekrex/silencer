#!/usr/bin/env python3
import sys
from platform import system

if system() == 'Windows':
    hosts = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
else:
    hosts = '/etc/hosts'

try:
    # if the provided arg is to "enable" the muting, (forced lowercase)
    # then set target variable to the content of the 'hosts muted' file
    if str(sys.argv[1]).lower() in ['enable', 'start', 'on']:
        target = 'hosts muted'

    else:
        # if anything other than "enable" was asked for in arg,
        # then we assume "disable" and set target to content
        # of 'hosts default' file
        target = 'hosts default'

    # with target set, we open the system hosts file
    # and replace it with the content of target
    with open(target, 'r') as file:
        contents = file.read()
    with open(hosts, 'w') as file:
        file.write(contents)
    # program will exit when finished

except Exception as e:
    # if something went wrong, show me
    print(e)