#!/usr/bin/env python3
import sys, time
import libAInchmarker
bain = libAInchmarker.bAInchmarker()
if len(sys.argv) == 3:
    topic=sys.argv[1]
    prompt=sys.argv[2]
elif len(sys.argv) == 1:
    bain.usage()
    topic = bain.get_env_var('topic','godParticle')
    prompt = bain.get_env_var('prompt',"write me a blog post about the god particle")
    time.sleep(1)
    print('ctrl-C to stop now or proceeding with the default topic and prompt')
    time.sleep(1)
    print(f'topic = {topic}'
    time.sleep(1)
    print(f'prompt = {prompt}'
    time.sleep(1)
else:
    bain.usage()
    exit(1)
bain.runner(topic, prompt)

