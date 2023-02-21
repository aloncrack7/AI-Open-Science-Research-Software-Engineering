import os
import imp

try:
    from grobid_client_python.grobid_client.grobid_client import GrobidClient
except:
    if not os.path.isdir("grobid_client_python"):
        os.system("git clone git@github.com:kermitt2/grobid_client_python.git")
    
    os.system("python3 grobid_client_python/setput install") 

    from grobid_client_python.grobid_client.grobid_client import GrobidClient