#!/usr/bin/env python
import sys
import libAInchmark as bain
if len(sys.argv) == 3:
    topic=sys.argv[1]
    prompt=sys.argv[2]
    exit(0)
else:
    bain.usage()
    for i in sys.argv:
        print(i)
    print(sys.argv)
    exit(0)
bain.while_read_ollama_runner()
