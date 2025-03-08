# zrobić możliwośc przekazania kolejnych argumentów jako pliki .pdf lub przekazanie pliku tekstowego z ścieżkami do plików .pdf

import pypdfium2 as pdfium
import urllib.request
import urllib.response
import json
import sys
import os

def main():
    pdf_paths= list()
    matches = dict()
    arg_cnt = len(sys.argv)

    for i in range(1, arg_cnt):
        arg = sys.argv[i]

        # split text into filename (index = 0) , filetype (index = 1) 
        # and check is filetype correct
        if os.path.splitext(arg)[1] != '.pdf':
            print(f'invalid argument: {arg}')
        else:
            pdf_paths.append(arg)

    if len(pdf_paths) == 0:
        print(f'run script with additional arguments (i.e. paths to pdf files)')
        return

    with open("results.txt", "w", encoding="utf-8") as result_file:
        for pdf_path in pdf_paths:
            pdf = pdfium.PdfDocument(pdf_path)

            # open http connetion to remote file with phrasal verbs
            url = "https://raw.githubusercontent.com/Zogir01/generated-english-phrasal-verbs/master/phrasal.verbs.build.json"
            response = urllib.request.urlopen(url)

            # load json from http response
            json_file = json.loads(response.read()) 

            # loaded json is dictionary, with keys representing phrasal verbs
            for verb in json_file.keys():

                # initialize dictionary matches with key = phrasal verb, value = initial count (0)
                matches.update({verb : 0})

            for page in pdf:

                # convert pdf page to text
                textpage = page.get_textpage()

                for word in matches.keys():

                    # start searching process
                    searcher = textpage.search(word, match_case=False, match_whole_word=True)

                    # count as long as it searches
                    while searcher.get_next() is not None:
                        matches[word] += 1

            # save results
            #
            result_file.write(f"path: {pdf_path}, pages: {len(pdf)}, version: {pdf.get_version()}")
            result_file.write("\n------------------------------------\n")

            for key, value in matches.items():

                # skip those that did not occur
                if value != 0:
                    result_file.write(f"{key}: {value}\n")

            result_file.write("\n------------------------------------\n")

if __name__ == '__main__':
    main()