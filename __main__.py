from pathlib import Path
from grobid_client_python.grobid_client.grobid_client import GrobidClient
import os
import re
from datetime import datetime
import pandas as pd
import numpy as np
import grobid_tei_xml as gtx
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Inicialize client and get the output folder for the .tei
client = GrobidClient(config_path="./config.json")
date=datetime.date(datetime.now())
time=datetime.time(datetime.now())
folderPath=f'out_{date}_{time}'

def prepareFolder():
    oldDircetory=os.popen(f"ls | grep \"out_\" | tail -n 1").read().replace("\n", "")
    os.system(f"mkdir {folderPath}")
    loadedPapers=[]

    if oldDircetory!='':
        with open(f"{oldDircetory}/loadedPapers.txt") as file:
            loadedPapers = [line.rstrip() for line in file]

    for requestPaper in os.listdir("papers"):
        fileName=re.sub(r"\.[^$]*", "", requestPaper)
        # TODO USE symbolic links
        # if fileName in loadedPapers:
        #     print(f"ln -s ./{oldDircetory}/{fileName}.tei.xml ./{folderPath}/{fileName}.tei.xml")
        #     os.system(f"ln -s ./{oldDircetory}/{fileName}.tei.xml ./{folderPath}/{fileName}.tei.xml")
        # else: 
        os.system(f"cp papers/{requestPaper} {folderPath}")

        os.system(f"echo {fileName} >> {folderPath}/loadedPapers.txt")

# Ask the server to process the .pdf  
def extractInfo():
    client.process("processFulltextDocument", folderPath, n=10)
    os.system(f"rm {folderPath}/*.pdf")

# Get the abstract of every paper
def extractAbstract():
    teis=os.listdir(folderPath)

    abstracts=""
    for i in teis:
        if not i.endswith(".txt"):
            filePath=f'{folderPath}/{i}'
            with open(filePath, 'r') as xmlFile:
                doc=gtx.parse_document_xml(xmlFile.read())
                abstracts+=doc.abstract
    
    return abstracts

# Generates word cloud 
def generateWordCloud(text):
    wordCloud = WordCloud(collocations = False, background_color = 'white').generate(text)
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def countFigures():
    teis=os.listdir(f"{folderPath}")

    counts=[0]*(len(teis)-1)
    pos=0
    for i in range(0, len(teis)):
        if not teis[i].endswith(".txt"):
            counts[pos]=int(os.popen(f"grep -o '<figure xmlns=' {folderPath}/{teis[i]} | wc -l").read().replace('\n', ''))
            pos+=1

    return counts

def genHistogram(numFigures):
    plt.hist(numFigures, density=False)
    plt.ylabel("Number of figures")
    plt.xticks(numFigures, os.listdir(f"{folderPath}").remove("loadedPapers.txt"))
    plt.show()

def getCitations():
    teis=os.listdir(f"{folderPath}")

    links=[[]]*(len(teis)-1)
    pos=0
    for i in range(0, len(teis)):
        if not teis[i].endswith(".txt"):
            filePath=f'{folderPath}/{teis[i]}'
            with open(filePath, 'r') as xmlFile:
                doc=gtx.parse_document_xml(xmlFile.read())
                links[pos]=doc.citations
            pos+=1
    
    return links
    
def main():
    prepareFolder()
    extractInfo()
    generateWordCloud(extractAbstract())
    genHistogram(countFigures())
    print(getCitations())


if __name__=="__main__":
    main()