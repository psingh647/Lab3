#!/usr/bin/env python3
'''Lab 3 Part 2 - Checking Free Disk Space'''
# Author ID: psingh647

import subprocess

def free_space():
    # Launch the Linux command and process its output
    process = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    # Decode the output to a UTF-8 string and strip newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())

