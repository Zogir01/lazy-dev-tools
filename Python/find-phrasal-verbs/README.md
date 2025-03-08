# find-phrasal-verbs
A script for finding phrasal verbs in pdf files. 
I'm going to use this tool to generate a list of the most popular verbs appearing on Polish final high school exam called "Matura".

In this script, I used a list of phrasal verbs from [this repository](https://github.com/WithEnglishWeCan/generated-english-phrasal-verbs). Many thanks to the authors for providing this valuable resource!

## Requirements
- [pypdfium2](https://github.com/pypdfium2-team/pypdfium2)

## Usage
Run this script with additional arguments, which are the next pdf files to be processed, as here:
```
python main.py example1.pdf example2.pdf
```

When the script finishes executing, you will notice that a text file with solution will be created.
