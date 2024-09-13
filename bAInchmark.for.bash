#!/bin/bash
source lib.bash
if [[ $# == 0 ]]; then
  echo 'using the default topic and prompt, which can be overridden'
  usage
  sleep 1
elif [[ $# == 1 ]]; then
  usage
  exit 1
elif [[ $# == 2 ]]; then
  topic=$1
  prompt="$2"
else
  usage
  exit 1
fi

main () {
  collect_data
  check_results_destination "${resultsOutputDir}/${topic}-${date}.csv"
  echo "model,time,size,unit,topic,prompt,card,uname,date" >> ${resultsOutput}
  count_zero=0
  #while_read_ollama_runner
  for_model_ollama_runner
}

time main
