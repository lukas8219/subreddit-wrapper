from threading import local
import src.subreddit_downloader as download
import json
import subprocess

configOptions = json.loads(open('./config.json').read());

credentials = configOptions["credentials"];
config = configOptions["config"];
subred = configOptions["subreddits"];
keyword = configOptions["keyword"];

def parse_command(subreddit, keyword, **args):

        cmd = ['python src/subreddit_downloader.py {0} '.format(subreddit)];

        for arg in args:
            if args[arg]:
                cmd.append('--{0} {1} '.format(arg, args[arg]))

        cmd.append('--keyword "{0}"'.format(keyword))

        return ''.join(cmd);

for subreddit in subred:
    parsedCmd = parse_command(**config, **credentials, subreddit=subreddit, keyword=keyword)
    print('Starting {0} with cmd {1}'.format(subreddit, parsedCmd))
    proc = subprocess.call(parsedCmd, shell=True);
