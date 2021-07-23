# Past Paper Extractor (A Level)
#### - Sulav Sapkota

This is an open source command line application built to extract past papers of A Levels. I personally found it tedious to visit site and download each file manually so I developed this tool that can help you download maximum past papers with just one line in terminal. Read the instructions below to use the tool.

## Downloading

- Click the green 'CODE' button and press download zip.
- or, if you have git installed in your device, go to terminal and type `git clone https://github.com/SulavSapkota2060/MyStocksBackend.git`
This will clone the repository in your local drive.
  

## Installing
Once you finish downloading, you need to install some dependencies which will help the tool run. 
Make sure you have Python installed. Go to the cloned directory and run
`pip3 install -r requirements.txt` in terminal.

## Running the tool
Now you can run the tool.
Run `python3 main.py --help` 

It will give you all the help commands.

Variables:

- Subject `--subject` or `-s` *Required
- Year `--year` or `-y` *Required
- Paper Type `--paper_type` or `-pt` *Optional

Syntax:

`python3 main.py --subject Physics --year 2020 --paper_type qp`

This will download all the past question papers of 2020 and store them in this directory `~/Documents/PastPapers/Physics/2020/qp`

*Note: If you don't add paper type then all the papers of given year will be downloaded in different folders as per the paper type.


*Though it seems a little tough to execute, I might convert this into a desktop application in near future to make it easier for students to download past papers.*

**CONTRIBUTIONS OPEN**

*Make a pull request with appropriate changes, and it will be accepted.*