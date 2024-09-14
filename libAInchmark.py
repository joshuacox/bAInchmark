#!/usr/bin/env python
import os, sys, csv, subprocess, ollama, tempfile
from dotenv import load_dotenv
from datetime import datetime
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
#topic = get_env_var('topic','godParticle')
topic = get_env_var('topic','summer')
#prompt = get_env_var('prompt',"write me a blog post about the god particle")
# prompt = get_env_var('prompt',"what is two plus three?")
prompt = get_env_var('prompt',"write me a hikou about snowboarding?")
uname = subprocess.run(["uname", "-a"], capture_output=True, text=True).stdout
print("uname")
print(uname)
card = subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True).stdout
print("card")
print(card)

### event horizon

def usage():
    print("Don't forget the quotes!")
    print('usage:')
    print(f"{sys.argv[0]} 'topic' 'prompt'")

usage()

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


def make_header(outputDestination):
    # make a md header like so:
    # $topic #$countzero
    ### written by $model
    try:
        with open(outputDestination, 'a+') as file:
            file.write("# ${topic} #$count_zero")
            file.write("")
            file.write("### writen by ${model}")
            file.write("")
    except IOError:
        print("Error: could not write file " + outputDestination)
        exit(1)

def while_read_ollama_runner():
    resultsOutput = check_results_destination(f'{resultsOutputDir}/{topic}-{date}.csv')
    with open(resultsOutput, 'w', newline='') as csvfile:
        results_writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        results_writer.writerow(['model', 'total_duration', 'size', 'lines', 'words', 'chars', 'topic', 'prompt', 'card', 'uname', 'date'])
    ollama_list = ollama.list()
    count_zero = 0
    for model in ollama_list['models']:
        print(model)
        #print(f'{model['name']} {model['size']} {topic} {prompt}')
        count_zero += 1
        outputDestination = check_output_destination(f"{outputDir}/{topic}-{model['name']}-{date}.md")
        make_header(outputDestination)
        # time our run
        time1 = datetime.today().strftime('%s.%f')
        #ollama run ${model}  "${prompt}" | tee -a ${outputDestination}
        response = ollama.chat(model=model['name'], messages=[
          {
            'role': 'user',
            'content': prompt,
          },
        ])
        print(response)
        time2 = datetime.today().strftime('%s.%f')
        with open(outputDestination, 'a+') as file:
            file.write(response['message']['content'])
        thisTemp = tempfile.TemporaryFile(mode='w+')
        thisTemp.write(response['message']['content'])
        #words=$(wc --words  ${outputDestination})
        print(thisTemp)
        print(thisTemp.name)
        lines = subprocess.run(["wc", "--lines", thisTemp.name], capture_output=True, text=True).stdout
        print(f'lines = {lines}')
        exit(0)
        words = subprocess.run(["wc", "--words", thisTemp.name], capture_output=True, text=True).stdout
        chars = subprocess.run(["wc", "--chars", thisTemp.name], capture_output=True, text=True).stdout
        print(f'words = {words}')
        print(f'chars = {chars}')
        print(response['message']['content'])
        total_duration = response['total_duration']
        size = model['size']
        lines = len(response['message']['content'].split('\n'))
        words = len(response['message']['content'].split(' ')) + lines
        chars = len(response['message']['content'])
        print(f'lines = {lines}')
        print(f'words = {words}')
        print(f'chars = {chars}')
        with open(resultsOutput, 'w', newline='') as csvfile:
            results_writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([model['name'], total_duration, size, lines, words, chars, topic, prompt, card, uname, date])
        # lines=$(wc --lines  ${outputDestination})
        # words=$(wc --words  ${outputDestination})
        # chars=$(wc --chars  ${outputDestination})
        # # add another line to our output results
        # echo "${model},${diff},${size},${unit},${lines},${words},${chars},${topic},${prompt},${card},${uname},${date}" |tee -a ${resultsOutput}
while_read_ollama_runner()
