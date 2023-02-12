from grobid_client_python.grobid_client.grobid_client import GrobidClient
import os
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
folderPath=f'papers/out_{date}_{time}'

# Ask the server to process the .pdf  
def extractInfo():
    client.process("processFulltextDocument", "./papers", n=10)

# Save the procces .tei to the folder desiganted for it
def saveTEIs():
    os.system(f'mkdir {folderPath}')
    os.system(f'mv papers/*.tei.xml {folderPath}')

# Get the abstract of every paper
def extractAbstract():
    teis=os.listdir(f"{folderPath}")

    abstracts=""
    for i in teis:
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

    counts=[0]*len(teis)
    for i in range(0, len(teis)):
        counts[i]=int(os.popen(f"grep -o '<figure xmlns=' {folderPath}/{teis[i]} | wc -l").read().replace('\n', ''))

    return counts

def genHistogram(numFigures):
    plt.hist(numFigures, density=False)
    plt.ylabel("Number of figures")
    plt.xticks(numFigures, os.listdir(f"{folderPath}"))
    plt.show()

def getCitations():
    teis=os.listdir(f"{folderPath}")

    links=[[]]*len(teis)
    for i in range(0, len(teis)):
        filePath=f'{folderPath}/{teis[i]}'
        with open(filePath, 'r') as xmlFile:
            doc=gtx.parse_document_xml(xmlFile.read())
            links[i]=doc.citations
    
    return links
    
def main():
    extractInfo()
    saveTEIs()
    # generateWordCloud(extractAbstract())
    # genHistogram(countFigures())
    print(getCitations())


if __name__=="__main__":
    main()