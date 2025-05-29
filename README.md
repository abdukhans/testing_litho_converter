# testing_litho_converter

## How to use this repo

This repo is meant only to test the code in the [LithoConverter](https://github.com/abdukhans/LithoConverter) library.

## How to run the code
The code needs the ``LITHO_CSVS`` folder and the ``Data`` folder. The ``Data`` folder is not included in this repo so you must create it. 

First step is to create an empty ``Data`` folder, in the same working directory as ``tests.py``.

Next you need to download the actual data itself. You need to get this data from the mineral google drive. Below are links to the datasets in the google drive. Download each of the files below and put it in the ``Data`` folder since that is where ``tests.py`` assumes they will be.

* [British Columbia Dataset](https://drive.google.com/file/d/1w3o7Kgcfr0BVokaCVfzc_IMppXZIdzE-/view?usp=drive_link)

* [Ontario Dataset](https://drive.google.com/file/d/1xmbvik3PC9nESo1hC68uM5fkDH17h8gA/view?usp=drive_link)

* [USGS Dataset](https://drive.google.com/file/d/1-W5O5qW9ftCAW5eLzJcKlzgiQzSy1sli/view?usp=drive_link)

* [SARIG Keyword Dataset](https://drive.google.com/file/d/1CQnFdJmVR4dJDl_MhEMRwk22crEjLKuv/view?usp=drive_link)


## Warning !
Running the ``tests.py`` may end up crashing your system. When running this on my machine it took up an extra 17GB of RAM!!!!!!!!!! This is why it just crashes on machines that don't have as much memory. This is clearly a problem that needs to be fixed. If you want to run this script you may have to reduce the number of rows the  BinVectorMarker generates on. To do this  I would recommend commenting out lines 25 to 31 inclusive. This reduces the number of sample descriptions rows that it translates to binary vectors to 10,000. Uncommenting these lines makes the number of rows it has to translate 1.3 million!!!! which may just crash your system, so just proceed with caution.    