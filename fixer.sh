#!/usr/bin/bash
today=$(date -I)

countzero=0
TARGS=$(find . -iname 'esp32s3s3-2025-08-2*.md')
for i in ${TARGS}; do
  MODEL_NAME=$(head -n3 $i|tail -n1|sed 's/^### writen by //')
  mv -v $i esp32s3s3-${MODEL_NAME}-${today}-${countzero}.md
  ((countzero++))
done

