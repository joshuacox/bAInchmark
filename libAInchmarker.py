#!/usr/bin/env python3
import os, sys, csv, subprocess
from dotenv import load_dotenv
from datetime import datetime
from ollama import Client

class bAInchmarker:
    def __init__(self):
        self.outputDir = self.get_env_var('outputDir','./output')
        self.resultsOutputDir = self.get_env_var('resultsOutputDir','./results')
        self.uname_s = subprocess.run(["uname", "-s"], capture_output=True, text=True).stdout.rstrip()
        self.uname_n = subprocess.run(["uname", "-n"], capture_output=True, text=True).stdout.rstrip()
        self.uname_r = subprocess.run(["uname", "-r"], capture_output=True, text=True).stdout.rstrip()
        self.uname_v = subprocess.run(["uname", "-v"], capture_output=True, text=True).stdout.rstrip()
        self.uname_m = subprocess.run(["uname", "-m"], capture_output=True, text=True).stdout.rstrip()
        self.uname_p = subprocess.run(["uname", "-p"], capture_output=True, text=True).stdout.rstrip()
        self.uname_i = subprocess.run(["uname", "-i"], capture_output=True, text=True).stdout.rstrip()
        self.uname_o = subprocess.run(["uname", "-o"], capture_output=True, text=True).stdout.rstrip()
        self.card = subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True).stdout.rstrip()
        self.ollama_host = self.get_env_var('OLLAMA_HOST','localhost')
        self.ollama_client = Client(host=f'http://{self.ollama_host}:11434')
        self.fieldnames = ['name',
                        'total_duration',
                        'lines',
                        'words',
                        'chars',
                        'size',
                        'size_gib',
                        'size_gb',
                        'topic',
                        'prompt',
                        'card',
                        'uname_s',
                        'uname_n',
                        'uname_r',
                        'uname_v',
                        'uname_m',
                        'uname_p',
                        'uname_i',
                        'uname_o',
                        'load_duration',
                        'eval_duration',
                        'outputDestination',
                        'prompt_eval_duration',
                        'created_at',
                        'done_reason',
                        'done',
                        'prompt_eval_count',
                        'eval_count']

    def get_env_var(self, env_var, default_value):
        try:
            if os.getenv(env_var):
                this_env_var = os.getenv(env_var)
            elif load_dotenv():
                if os.getenv(env_var):
                    this_env_var = os.getenv(env_var)
                else:
                    this_env_var = default_value
            else:
                this_env_var = default_value
        except:
            this_env_var = default_value
        return this_env_var

    def usage(self):
        print(f"Don't forget the quotes!\nusage:\n{sys.argv[0]} 'topic' 'prompt'")

    def check_destination(self, thisName, thisDir, topic):
        thisDestination = f'{thisDir}/{thisName}'
        date = datetime.today().strftime('%Y-%m-%d')
        try:
            os.mkdir(thisDir)
        except FileExistsError:
            pass
        if os.path.isfile(thisDestination):
            date=datetime.today().strftime('%Y-%m-%d-%s')
            thisDestination=f'{thisDir}/{topic}-{date}.md'
        if os.path.isfile(thisDestination):
            date=datetime.today().strftime('%Y-%m-%d-%s.%f')
            thisDestination=f'{thisDir}/{topic}-{date}.md'
        if os.path.isfile(thisDestination):
            print(f'something is wrong will not overwrite {thisDestination}')
            exit(1)
        return thisDestination

    def make_header(self, outputDestination, count_zero, topic, model):
        # make a md header like so:
        # $topic #$countzero
        ### written by $model
        try:
            with open(outputDestination, 'a+') as file:
                file.write(f"# {topic} #{count_zero}\n\n")
                file.write(f"### writen by {model}\n\n")
        except IOError:
            print("Error: could not write file " + outputDestination)
            exit(1)

    def tempDebug():
        # DEPRECATED
        # this function was used to see if wc got different results than the python did in counting  
        # can be deleted in the future, but it is interesting
        tmpdirname = subprocess.run(["mktemp", "-d"], capture_output=True, text=True).stdout.rstrip()
        tmp_file = tmpdirname + "/tmpfile"
        with open(tmp_file, 'a+') as tmpfile:
            tmpfile.write(response['message']['content'])
            tmpfile.seek(0)
            lines = subprocess.run(["wc", "--lines", tmp_file], capture_output=True, text=True).stdout.rstrip()
            words = subprocess.run(["wc", "--words", tmp_file], capture_output=True, text=True).stdout.rstrip()
            chars = subprocess.run(["wc", "--chars", tmp_file], capture_output=True, text=True).stdout.rstrip()
            print(f'lines = {lines}')
            print(f'words = {words}')
            print(f'chars = {chars}')

    def runner(self, topic, prompt):
        date = datetime.today().strftime('%Y-%m-%d')
        resultsOutput = self.check_destination(f'{topic}-{date}.csv', self.resultsOutputDir, topic)
        with open(resultsOutput, 'w') as csvfile:
            fieldnames = self.fieldnames
            results_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            results_writer.writeheader()
        ollama_list = self.ollama_client.list()
        count_zero = 0

        for model in ollama_list['models']:
            # Pre increment this so that we begin with 1 for our first ouput
            count_zero += 1

            # Each loop we need to check to make sure our output destination is vacant
            outputDestination = self.check_destination(f"{topic}-{model['name']}-{date}.md", self.outputDir, topic)
            self.make_header(outputDestination, count_zero, topic, model['name'])

            response = self.ollama_client.chat(model=model['name'], messages=[
              {
                'role': 'user',
                'content': prompt,
              },
            ])
            print(response)

            # Write the output as a markdown file
            with open(outputDestination, 'a+') as file:
                file.write(response['message']['content'])

            # Gather data
            # we divide durations by 1_000_000_000 to get it in seconds
            # to be more human readable
            # print(float(total_duration) / 1_000_000_000.0)
            load_duration = response['load_duration'] / 1_000_000_000.0
            eval_duration = response['eval_duration'] / 1_000_000_000.0
            total_duration = response['total_duration'] / 1_000_000_000.0
            prompt_eval_duration = response['prompt_eval_duration'] / 1_000_000_000.0
            size = model['size']
            size_gb = ( model['size'] / ( 10 ** 9 ))
            size_gib = ( model['size'] / ( 2 ** 30 ))
            lines = len(response['message']['content'].split('\n'))
            words = len(response['message']['content'].split())
            chars = len(response['message']['content'])
            created_at = response['created_at']
            done_reason = response['done_reason']
            done = response['done']
            prompt_eval_count = response['prompt_eval_count']
            eval_count = response['eval_count']

            # Write to our results CSV file
            with open(resultsOutput, 'a', newline='') as csvfile:
                fieldnames = self.fieldnames
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
                    'name': model['name'],
                    'total_duration': total_duration,
                    'lines': lines,
                    'words': words,
                    'chars': chars,
                    'size': size,
                    'size_gib': size_gib,
                    'size_gb': size_gb,
                    'topic': topic,
                    'prompt': prompt,
                    'card': self.card,
                    'uname_s': self.uname_s,
                    'uname_n': self.uname_n,
                    'uname_r': self.uname_r,
                    'uname_v': self.uname_v,
                    'uname_m': self.uname_m,
                    'uname_p': self.uname_p,
                    'uname_i': self.uname_i,
                    'uname_o': self.uname_o,
                    'load_duration': load_duration,
                    'eval_duration': eval_duration,
                    'outputDestination': outputDestination,
                    'prompt_eval_duration': prompt_eval_duration,
                    'created_at': created_at,
                    'done_reason': done_reason,
                    'done': done,
                    'prompt_eval_count': prompt_eval_count,
                    'eval_count': eval_count
                })
