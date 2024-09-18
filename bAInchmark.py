#!/usr/bin/env python3
import sys
import libAInchmarker
bain = libAInchmarker.bAInchmarker()
topic = bain.get_env_var('topic','godParticle')
prompt = bain.get_env_var('prompt',"write me a blog post about the god particle")
if len(sys.argv) == 3:
    topic=sys.argv[1]
    prompt=sys.argv[2]
else:
    bain.usage()
bain.while_read_ollama_runner(topic, prompt)
