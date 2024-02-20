import argparse
import json
from os.path import exists
from os import chmod
import stat
import subprocess
import time


def init():
    with open('.git/hooks/commit-msg', 'w') as f:
        f.write('''
        #!/bin/sh
        
        python3 tears.py commit -m $1
        ''')
        chmod('.git/hooks/commit-msg', stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)


def goal():
    goal_txt = input("What's your goal for your next git commit?")
    duration = int(input("How long will it take to do that? (mins)"))
    finish_time = time.time() + (duration*60)
    with open('.git/hooks/tears.json', 'w') as f:
        json.dump({'goal': goal_txt, 'finish_time': finish_time}, f)
        quit(0)


def commit(message_file):
    tears_goal = {}
    if exists('.git/hooks/tears.json'):
        with open('.git/hooks/tears.json', 'r') as f:
            tears_goal = json.load(f)
    if tears_goal:
        time_remaining = tears_goal['finish_time'] - time.time()
        if time_remaining >= 0:
            with open(message_file, 'r') as mf:
                first_line = mf.readline()
                if first_line.startswith(tears_goal['goal']):
                    quit(0)
    subprocess.run(['git', 'checkout', '-q', '-f'])
    print('Like tears in rain...')
    quit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='tears')
    parser.add_argument('command', help='command', choices=['init', 'goal', 'commit'])
    parser.add_argument('-m', '--message', help='git commit message file')
    args = parser.parse_args()
    if args.command == 'init':
        init()
    elif args.command == 'goal':
        goal()
    elif args.command == 'commit':
        commit(args.message)
