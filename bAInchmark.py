#!/usr/bin/env python3
import sys
import libAInchmark as bain
topic = bain.get_env_var('topic','godParticle')
prompt = bain.get_env_var('prompt',"write me a blog post about the god particle")
#prompt = get_env_var('prompt',"what is two plus three?")
#prompt = get_env_var('prompt',"write me a hikou about snowboarding?")
if len(sys.argv) == 3:
    topic=sys.argv[1]
    prompt=sys.argv[2]
else:
    bain.usage()
print(topic)
print(prompt)
bain.while_read_ollama_runner(topic, prompt)
