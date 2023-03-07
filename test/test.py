import unittest 
from func.func import *
import os

class TestMetadataExtractor(unittest.TestCase):

    def testNumberDocumentsGenerated(self):
        os.system("rm -rf ./testIn")
        selectedPapers=os.listdir("papers")

        os.system("mkdir testIn")
        for i in range(0, 2):
            os.system(f"cp papers/{selectedPapers[i]} testIn")
        os.system("cp papers/jukebox.pdf ./testIn")

        extractInfo("./testIn")

        num=0
        for i in os.listdir("./testIn"):
            num+=1
        assert num==3

    def testNumberCitations(self):
        os.system("rm -rf ./testIn2")
        selectedPapers=os.listdir("papers")

        os.system("mkdir testIn2")
        for i in range(0, 2):
            os.system(f"cp papers/{selectedPapers[i]} testIn2")
        os.system("cp papers/jukebox.pdf ./testIn2")

        extractInfo("./testIn2")

        assert getCitations("./testIn2").count(' ')+1==3

    def testNumberCitations(self):
        os.system("rm -rf ./testIn3")
        selectedPapers=os.listdir("papers")

        os.system("mkdir testIn3")
        for i in range(0, 2):
            os.system(f"cp papers/{selectedPapers[i]} testIn3")
        os.system("cp papers/jukebox.pdf ./testIn3")

        extractInfo("./testIn3")
        generateWordCloud(extractAbstract("./testIn3"))

        assert os.path.isfile("./out/wordcloud.png")==True

if __name__=='__main__':
    unittest.main()
    os.system("rm -rf ./testIn")
    os.system("rm -rf ./testIn2")
    os.system("rm -rf ./testIn3")

