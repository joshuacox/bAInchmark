# bAInchmark

AI benchmarking

This is a tool to collect information on how various prompts run on all installed models in ollama.

### Usage

./bAInchmark.py "TOPIC" "PROMPT"

e.g.

./bAInchmark.py 'strawberry' 'Count the number of times that R occurs in the word "strawberry"'

The results will be in the results directory, and each individual output is saved in the output directory.

### Results

Results will be in the form of a CSV file like this:

```
model,total_duration,lines,words,chars,size,size_gib,size_gb,topic,prompt,card,uname,load_duration,eval_duration,outputDestination,prompt_eval_duration,created_at,done_reason,done,prompt_eval_count,eval_count
gemma2:latest,1.826578278,5,20,111,5443152417,5.069330723024905,5.443152417,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,1.533401239,0.238397,./output/strawberry-gemma2:latest-2024-09-18.md,0.053984,2024-09-18T23:26:45.607277799Z,stop,True,23,30
nous-hermes2-mixtral:latest,4.004348715,1,42,261,26442493141,24.62649079132825,26.442493141,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,3.147623707,0.6266,./output/strawberry-nous-hermes2-mixtral:latest-2024-09-18.md,0.106963,2024-09-18T23:26:49.613430499Z,stop,True,90,64
hermes3:latest,1.442896685,2,10,57,4661226630,4.3411055859178305,4.66122663,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,1.293326569,0.099227,./output/strawberry-hermes3:latest-2024-09-18.md,0.049499,2024-09-18T23:26:51.05780019Z,stop,True,24,19
wizard-vicuna-uncensored:30b-q8_0,12.131027372,1,8,42,34565124970,32.191281178966165,34.56512497,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,11.723425421,0.293713,./output/strawberry-wizard-vicuna-uncensored:30b-q8_0-2024-09-18.md,0.0727,2024-09-18T23:27:03.1903222Z,stop,True,27,17
command-r-plus:latest,9.286368794,2,38,212,59221118559,55.15396460797638,59.221118559,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,7.718718075,1.398633,./output/strawberry-command-r-plus:latest-2024-09-18.md,0.126389,2024-09-18T23:27:12.478244097Z,stop,True,41,51
deepseek-v2.5:latest,38.873105367,1,10,56,132912472044,123.78438566252589,132.912472044,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,37.469398762,0.970954,./output/strawberry-deepseek-v2.5:latest-2024-09-18.md,0.391868,2024-09-18T23:27:51.352899015Z,stop,True,18,17
hermes3:70b,6.030904514,2,12,63,39969747239,37.224727905355394,39.969747239,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,5.472236754,0.422205,./output/strawberry-hermes3:70b-2024-09-18.md,0.09534,2024-09-18T23:27:57.385472121Z,stop,True,24,20
hermes3:405b,81.034354965,2,10,57,228856435464,213.13916469365358,228.856435464,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,56.18620339,17.580934,./output/strawberry-hermes3:405b-2024-09-18.md,7.266327,2024-09-18T23:29:18.421488958Z,stop,True,24,19
llama3.1:405b,246.505509953,1,9,51,228856439568,213.13916851580143,228.856439568,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,228.060608636,10.617641,./output/strawberry-llama3.1:405b-2024-09-18.md,7.826393,2024-09-18T23:33:24.94560069Z,stop,True,26,14
codellama:70b-python,15.465208146,9,96,520,38872431302,36.20277280174196,38.872431302,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,12.5466549,2.823801,./output/strawberry-codellama:70b-python-2024-09-18.md,0.093999,2024-09-18T23:33:40.413185595Z,stop,True,17,137
codellama:70b-instruct,14.285902213,8,71,388,38872431643,36.202773119322956,38.872431643,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,11.776273581,2.36613,./output/strawberry-codellama:70b-instruct-2024-09-18.md,0.101962,2024-09-18T23:33:54.701022579Z,stop,True,37,115
codegemma:latest,2.715024948,3,9,53,5011852809,4.667651661671698,5.011852809,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,2.573310398,0.090746,./output/strawberry-codegemma:latest-2024-09-18.md,0.050148,2024-09-18T23:33:57.417931641Z,stop,True,40,19
codellama:70b-code,124.521314969,10,20,127,38872431302,36.20277280174196,38.872431302,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,123.485669857,0.940873,./output/strawberry-codellama:70b-code-2024-09-18.md,0.094025,2024-09-18T23:36:01.940787424Z,stop,True,17,46
deepseek-coder-v2:latest,6.02754888,11,103,561,8905126121,8.29354498628527,8.905126121,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,4.237566068,1.64612,./output/strawberry-deepseek-coder-v2:latest-2024-09-18.md,0.102905,2024-09-18T23:36:07.969919136Z,stop,True,23,164
mistral-nemo:latest,4.011230576,3,15,83,7071713232,6.586046174168587,7.071713232,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,3.746704348,0.169225,./output/strawberry-mistral-nemo:latest-2024-09-18.md,0.053884,2024-09-18T23:36:11.983011746Z,stop,True,19,25
llama3.1:latest,3.189682886,1,10,60,4661230766,4.341109437867999,4.661230766,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,3.00529343,0.087768,./output/strawberry-llama3.1:latest-2024-09-18.md,0.055841,2024-09-18T23:36:15.174541978Z,stop,True,26,17
llama3.1:70b,13.377614464,3,12,70,39969751439,37.22473181691021,39.969751439,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,12.802734046,0.422357,./output/strawberry-llama3.1:70b-2024-09-18.md,0.111341,2024-09-18T23:36:28.55362948Z,stop,True,26,20
phi3:latest,2.382761705,1,9,54,2176178401,2.0267240712419152,2.176178401,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,2.269294468,0.067734,./output/strawberry-phi3:latest-2024-09-18.md,0.04495,2024-09-18T23:36:30.937897855Z,stop,True,19,16
nous-hermes2:latest,3.460305619,1,9,53,6072407285,5.655369986779988,6.072407285,strawberry,"Count the number of times that R occurs in the word ""strawberry""",GPU 0: NVIDIA GH200 480GB (UUID: GPU-dc636aa0-5edb-4aef-5695-7aaec0212dd1),Linux gh200-sa4-1 6.8.0-1013-nvidia-64k #14-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 20 21:56:18 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux,3.247247503,0.106146,./output/strawberry-nous-hermes2:latest-2024-09-18.md,0.064913,2024-09-18T23:36:34.399955523Z,stop,True,90,16
```

### Output

Each individual response is recorded in the outpout directory and look like this:

```
# strawberry #16

### writen by llama3.1:latest

The letter 'R' appears three times in the word "strawberry".
```

### Bash conversion

This started out as a bash script and was converted to python.  The bash is left in here for now to illustrate the problem I ran into:

[issue #1](https://github.com/joshuacox/bAInchmark/issues/1)
