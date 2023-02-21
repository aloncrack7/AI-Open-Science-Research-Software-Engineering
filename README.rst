
Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering
=========================================================================

Repository for Artificial Intelligence And Open Science In Research Software Engineering subject


.. image:: https://readthedocs.org/projects/ai-open-science-research-software-engineering/badge/?version=latest
   :target: https://ai-open-science-research-software-engineering.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
   :target: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
   :alt: Python


.. image:: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
   :target: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
   :alt: GitHub


`Licence (CC0-1.0 license) <https://github.com/aloncrack7/Artificial-Intelligence-And-Open-Science-In-Research-Software-Engineering/blob/main/LICENCE.md>`_
---------------------------------------------------------------------------------------------------------------------------------------------------------------


.. image:: https://licensebuttons.net/l/zero/1.0/80x15.png
   :target: http://creativecommons.org/publicdomain/zero/1.0/
   :alt: License: CC0-1.0


Citation
--------

APA
^^^

.. code-block:: text

   García Velasco, A. Artificial Intelligence And Open Science In Research Software Engineering [Computer software]. https://github.com/aloncrack7/AI-Open-Science-Research-Software-Engineering

BibTex
^^^^^^

.. code-block:: text

   @software{Garcia_Velasco_Artificial_Intelligence_And,
   author = {García Velasco, Alonso},
   license = {CC0-1.0},
   title = {{Artificial Intelligence And Open Science In Research Software Engineering}},
   url = {https://github.com/aloncrack7/AI-Open-Science-Research-Software-Engineering}
   }

Server instalation
------------------

.. code-block:: bash

   docker pull lfoppiano/grobid:0.7.2

.. code-block:: bash

   docker run --rm -p 8070:8070 -p 8081:8071 lfoppiano/grobid:0.7.2

Client instalation
------------------


* Run clientInstallation.sh wich uses python venv to make a virtual env for the project

.. code-block:: bash

   ./clientInstalationVenv.sh


* tkinter is also need it for the word clouds

.. code-block:: bash

   sudo apt install python3-tk

What does the clien instalation do
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* It creates a virtual enviroment, activates, downloads the latest version of pip and proceeds to install al requirements. After that clones the grobid client form the repository an installs it.

.. code-block:: bash

   python3 -m venv AIOSRSE
   source AIOSRSE/bin/activate
   python3 -m pip install --upgrade pip
   pip install -r requiremets.txt

   git clone https://github.com/kermitt2/grobid_client_python
   cd grobid_client_python
   python3 setup.py install

   cd ..

Running the program
-------------------


* Make sure you have the client and the server properly installed

.. code-block:: bash

   python3 __main__.py
