#!/usr/bin/env bash
set -eu
# These variables can be overridden by env
: ${date:=$(date -I)}
: ${outputDir:=output}
: ${resultsOutputDir:=results}
: ${topic:='godParticle'}
: ${prompt:="write me a blog post about the god particle"}

usage () {
  echo "Don't forget the quotes!"
  echo 'usage:'
  echo "$0 'topic' 'prompt'"
}

collect_data () {
  # collect some machine data
  uname=$(uname -a)
  card=$(nvidia-smi -L|tr '\n' '-')
}

check_output_destination () {
  echo 'check_output_destination'
  mkdir -p ${outputDir}
  outputDestination=$1
  if [[ -f ${outputDestination} ]]; then
    outputDestination=${outputDir}/${topic}-${date}-$(date +%s).md
  fi
  if [[ -f ${outputDestination} ]]; then
    outputDestination=${outputDir}/${topic}-${date}-$(date +%s.%N).md
  fi
  if [[ -f ${outputDestination} ]]; then
    echo 'something is wrong will not overwrite output'
    exit 1
  fi
}
make_header () {
  # make a md header like so:
  # $topic #$countzero
  ### written by $model
  echo "# ${topic} #$count_zero" | tee -a ${outputDestination}
  echo "" | tee -a ${outputDestination}
  echo "### writen by ${model}" | tee -a ${outputDestination}
  echo "" | tee -a ${outputDestination}
}

while_read_ollama_runner () {
  ollama_list=$(ollama list|awk '{print $1","$3","$4}'|tail -n +2)
  while IFS="," read -r model size unit
  do
    common_runner
  done <<< "$ollama_list"
}

common_runner () {
  echo ${model} ${size} ${unit} ${topic} ${prompt}
  ((++count_zero))
  check_output_destination "${outputDir}/${topic}-${model}-${date}.md"
  make_header
  # time our run
  time1=$(date +%s.%N)
  ollama run ${model}  "${prompt}" | tee -a ${outputDestination}
  time2=$(date +%s.%N)
  diff=$(echo "scale=40;${time2} - ${time1}" | bc)
  lines=$(wc --lines  ${outputDestination})
  words=$(wc --words  ${outputDestination})
  chars=$(wc --chars  ${outputDestination})
  # add another line to our output results
  echo "${model},${diff},${size},${unit},${lines},${words},${chars},${topic},${prompt},${card},${uname},${date}" |tee -a ${resultsOutput}
}

check_results_destination () {
  mkdir -p ${resultsOutputDir}
  resultsOutput=$1
  if [[ -f ${resultsOutput} ]]; then
    resultsOutput=${resultsOutputDir}/${topic}-${date}-$(date +%s).csv
  fi
  if [[ -f ${resultsOutput} ]]; then
    resultsOutput=${resultsOutputDir}/${topic}-${date}-$(date +%s.%N).csv
  fi
  if [[ -f ${resultsOutput} ]]; then
    echo 'something is wrong will not overwrite results'
    exit 1
  fi
  echo "model,time,size,lines,words,chars,unit,topic,prompt,card,uname,date" >> ${resultsOutput}
}

for_model_ollama_runner () {
  ollama_list=$(ollama list|awk '{print $1}'|tail -n +2)
  for model in $ollama_list
  do 
    size=$(ollama list|grep ${model}|awk '{print $3}')
    unit=$(ollama list|grep ${model}|awk '{print $4}')
    common_runner
  done
}
