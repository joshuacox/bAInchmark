#!/usr/bin/env python3
import os, sys, csv, subprocess, tempfile
from dotenv import load_dotenv
from datetime import datetime
from ollama import Client
# These variables can be overridden by env
def get_env_var(env_var, default_value):
    try:
        if os.getenv(env_var):
            this_env_var = int(os.getenv(env_var))
        elif load_dotenv():
            if os.getenv(env_var):
                this_env_var = int(os.getenv(env_var))
            else:
                this_env_var = default_value
        else:
            this_env_var = default_value
    except:
        this_env_var = default_value
    return this_env_var

date = datetime.today().strftime('%Y-%m-%d')
outputDir = get_env_var('outputDir','./output')
resultsOutputDir = get_env_var('resultsOutputDir','./results')
topic = get_env_var('topic','godParticle')
prompt = get_env_var('prompt',"write me a blog post about the god particle")
#prompt = get_env_var('prompt',"what is two plus three?")
#prompt = get_env_var('prompt',"write me a hikou about snowboarding?")
uname = subprocess.run(["uname", "-a"], capture_output=True, text=True).stdout
card = subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True).stdout
ollama_host = get_env_var('OLLAMA_HOST','localhost')
ollama_client = Client(host=f'http://{ollama_host}:11434')

def usage():
    print("Don't forget the quotes!")
    print('usage:')
    print(f"{sys.argv[0]} 'topic' 'prompt'")

def check_results_destination(resultsOutput):
    try:
        os.mkdir(resultsOutputDir)
    except FileExistsError:
        pass
    if os.path.isfile(resultsOutput):
        date=datetime.today().strftime('%Y-%m-%d-%s')
        resultsOutput=f'{resultsOutputDir}/{topic}-{date}.csv'
    if os.path.isfile(resultsOutput):
        date=datetime.today().strftime('%Y-%m-%d-%s.%f')
        resultsOutput=f'{resultsOutputDir}/{topic}-{date}.csv'
    if os.path.isfile(resultsOutput):
        print('something is wrong will not overwrite results output')
        exit(1)
    return resultsOutput 
    #echo "model,time,size,lines,words,chars,unit,topic,prompt,card,uname,date" >> ${resultsOutput}

def check_output_destination(outputDestination):
    try:
        os.mkdir(outputDir)
    except FileExistsError:
        pass
    if os.path.isfile(outputDestination):
        date=datetime.today().strftime('%Y-%m-%d-%s')
        outputDestination=f'{outputDir}/{topic}-{date}.md'
    if os.path.isfile(outputDestination):
        date=datetime.today().strftime('%Y-%m-%d-%s.%f')
        outputDestination=f'{outputDir}/{topic}-{date}.md'
    if os.path.isfile(outputDestination):
        print('something is wrong will not overwrite output')
        exit(1)
    return outputDestination


def make_header(outputDestination, count_zero, topic, model):
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
        thisTemp = tempfile.TemporaryFile(mode='w+')
        thisTemp.write(response['message']['content'])
        #words=$(wc --words  ${outputDestination})
        thisTemp.seek(0)
        print(thisTemp.read())
        print(thisTemp.name)
        tmpdirname = subprocess.run(["mktemp", "-d"], capture_output=True, text=True).stdout
        tmp_file = tmpdirname.rstrip() + "/tmpfile"
        print(tmp_file)
        with open(tmp_file, 'a+') as tmpfile:
            tmpfile.write(response['message']['content'])
            tmpfile.seek(0)
            echo1 = subprocess.run(["echo", "wc", "--lines", tmp_file], capture_output=True, text=True).stdout
            print("echo1" + echo1)
            lines = subprocess.run(["wc", "--lines", tmp_file], capture_output=True, text=True).stdout
            words = subprocess.run(["wc", "--words", tmp_file], capture_output=True, text=True).stdout
            chars = subprocess.run(["wc", "--chars", tmp_file], capture_output=True, text=True).stdout
            print(lines)
            print(f'lines = {lines}')
            print(f'words = {words}')
            print(f'chars = {chars}')
            tmpfile.seek(0)
            print(tmpfile.read())

def while_read_ollama_runner():
    resultsOutput = check_results_destination(f'{resultsOutputDir}/{topic}-{date}.csv')
    with open(resultsOutput, 'w', newline='') as csvfile:
        results_writer = csv.writer(csvfile, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        results_writer.writerow(['model', 'total_duration', 'lines', 'words', 'chars', 'size', 'size_gib',
        'size_gb', 'topic', 'prompt', 'card', 'uname', 'load_duration', 'eval_duration',
        'prompt_eval_duration', 'created_at', 'done_reason', 'done', 'prompt_eval_count', 'eval_count'])
    ollama_list = ollama_client.list()
    count_zero = 0
    for model in ollama_list['models']:
        count_zero += 1
        outputDestination = check_output_destination(f"{outputDir}/{topic}-{model['name']}-{date}.md")
        make_header(outputDestination, count_zero, topic, model['name'])
        time1 = datetime.today().strftime('%s.%f')
        response = ollama_client.chat(model=model['name'], messages=[
          {
            'role': 'user',
            'content': prompt,
          },
        ])
        print(response)
        time2 = datetime.today().strftime('%s.%f')
        with open(outputDestination, 'a+') as file:
            file.write(response['message']['content'])
        load_duration = response['load_duration'] / 1_000_000_000.0
        eval_duration = response['eval_duration'] / 1_000_000_000.0
        total_duration = response['total_duration'] / 1_000_000_000.0
        prompt_eval_duration = response['prompt_eval_duration'] / 1_000_000_000.0
        # print(float(total_duration) / 1_000_000_000.0)
        # print(float(time2) - float(time1))
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

        with open(resultsOutput, 'a', newline='') as csvfile:
            results_writer = csv.writer(csvfile, delimiter=',',
                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([model['name'], total_duration, lines, words, chars, size, size_gib,
            size_gb, topic, prompt, card, uname, load_duration, eval_duration, 
            prompt_eval_duration, created_at, done_reason, done, prompt_eval_count, eval_count])
