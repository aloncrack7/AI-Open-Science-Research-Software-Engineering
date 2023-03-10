import os
try:
    from grobid_client_python.grobid_client.grobid_client import GrobidClient
except:
    if not os.path.isdir("grobid_client_python"):
        os.system("git clone git@github.com:kermitt2/grobid_client_python.git")
    
    os.system("python3 grobid_client_python/setput install") 

    from grobid_client_python.grobid_client.grobid_client import GrobidClient
from grobid_client_python.grobid_client.grobid_client import GrobidClient 
import re
from datetime import datetime
import pandas as pd
import numpy as np
import grobid_tei_xml as gtx
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Inicialize client and get the output folder for the .tei
client = GrobidClient(config_path="./config.json")
print('Conection')
date=datetime.date(datetime.now())
time=datetime.time(datetime.now())
folderPath=f'out_{date}_{time}'

def prepareFolder(dir=folderPath):
    oldDircetory=os.popen(f"ls | grep \"out_\" | tail -n 1").read().replace("\n", "")
    os.system(f"mkdir {dir}")
    loadedPapers=[]

    if oldDircetory!='' and oldDircetory!='out_container':
        with open(f"{oldDircetory}/loadedPapers.txt") as file:
            loadedPapers = [line.rstrip() for line in file]

    for requestPaper in os.listdir("papers"):
        fileName=re.sub(r"\.[^$]*", "", requestPaper)
        # TODO USE symbolic links
        # if fileName in loadedPapers:
        #     print(f"ln -s ./{oldDircetory}/{fileName}.tei.xml ./{folderPath}/{fileName}.tei.xml")
        #     os.system(f"ln -s ./{oldDircetory}/{fileName}.tei.xml ./{folderPath}/{fileName}.tei.xml")
        # else: 
        os.system(f"cp papers/{requestPaper} {dir}")

        os.system(f"echo {fileName} >> {dir}/loadedPapers.txt")

    print('Prepare folder')

# Ask the server to process the .pdf  
def extractInfo(dir=folderPath):
    client.process("processFulltextDocument", dir, n=10)
    os.system(f"rm {dir}/*.pdf")
    print('extract info')

# Get the abstract of every paper
def extractAbstract(dir=folderPath):
    teis=os.listdir(dir)

    abstracts=""
    for i in teis:
        if not i.endswith(".txt"):
            filePath=f'{dir}/{i}'
            with open(filePath, 'r') as xmlFile:
                doc=gtx.parse_document_xml(xmlFile.read())
                abstracts+=doc.abstract
    
    print('Extract abstract')
    return abstracts

# Generates word cloud 
def generateWordCloud(text):
    wordCloud = WordCloud(collocations = False, background_color = 'white').generate(text)
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./out/wordcloud.png')
    plt.close()
    print('WordCloud')

def countFigures(dir=folderPath):
    teis=os.listdir(f"{dir}")

    counts=[0]*(len(teis)-1)
    pos=0
    for i in range(0, len(teis)):
        if not teis[i].endswith(".txt"):
            counts[pos]=int(os.popen(f"grep -o '<figure xmlns=' {dir}/{teis[i]} | wc -l").read().replace('\n', ''))
            pos+=1

    print('count figures')
    return counts

def genHistogram(numFigures, dir=folderPath):
    plt.hist(numFigures, density=False)
    plt.ylabel("Number of figures")
    plt.xticks(numFigures, os.listdir(f"{dir}").remove("loadedPapers.txt"))
    plt.savefig('./out/histogram.png')
    print('Histogram')

def getCitations(dir=folderPath):
    teis=os.listdir(f"{dir}")

    links=''
    for i in teis:
        if not i.endswith(".txt"):
            filePath=f'{dir}/{i}'
            with open(filePath, 'r') as xmlFile:
                doc=gtx.parse_document_xml(xmlFile.read())
                fullCitation=doc.citations

                for j in fullCitation:
                    if j.url!=None:
                        links+=(j.url)+' '
    
    print('get citations')
    return links[:-1]
    
