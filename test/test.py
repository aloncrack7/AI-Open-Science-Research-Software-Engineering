import unittest 
import __main__
import os

class TestMetadataExtractor(unittest.TestCase):
    
    def testNumberDocumentsGenerated(self):
        print(os.getcwd())
        selectedPapers=os.listdir("papers")

        os.system("mkdir testIn")
        for i in range(0, 2):
            os.system(f"cp papers/{selectedPapers[i]} testIn")

        __main__.extractInfo("../testIn")
        os.system("rm -rf testIn")

if __name__=='__main__':
    unittest.main()