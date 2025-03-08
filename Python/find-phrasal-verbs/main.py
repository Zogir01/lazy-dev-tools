import pypdfium2 as pdfium
import urllib.request
import json
import sys
import os
from collections import defaultdict

PHRASAL_VERBS_URL = "https://raw.githubusercontent.com/Zogir01/generated-english-phrasal-verbs/master/phrasal.verbs.build.json"
RESULT_FILE = "result.json"

def main():
    pdf_paths= list()
    matches = defaultdict(int)
    arg_cnt = len(sys.argv)

    # process arguments
    for i in range(1, arg_cnt):
        arg = sys.argv[i]

        if len(sys.argv < 2):
            print("Provide at least one PDF file as an argument.")
            return

        # split text into filename (index = 0) , filetype (index = 1) 
        # and check is filetype correct
        if os.path.isfile() and os.path.splitext(arg)[1] != '.pdf':
            print(f'Invalid argument: {arg}')
        else:
            pdf_paths.append(arg)

    if not pdf_paths:
        print(f'No valid PDF files found.')
        return
    
    # open http connetion to remote file with phrasal verbs
    response = urllib.request.urlopen(PHRASAL_VERBS_URL)

    # load json from http response. This object is dictionary 
    # with keys representing phrasal verbs
    json_file = json.loads(response.read()) 

    for pdf_path in pdf_paths:
        pdf = pdfium.PdfDocument(pdf_path)

        for page in pdf:
            # convert pdf page to text
            textpage = page.get_textpage()

            for verb in json_file.keys():
                # start searching process
                searcher = textpage.search(verb, match_case=False, match_whole_word=True)

                # count as long as it searches
                while searcher.get_next() is not None:
                    # increment word counter
                    matches[verb] += 1

    # json serialization
    json_object = json.dumps(obj = matches, indent = 4)

    # save json object to file
    with open(RESULT_FILE, "w") as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    main()