import subprocess
from os import listdir
from owlready2 import *
from os.path import isfile, join
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def getFilesFromDir( dir ):
   files = []
   for f in listdir(dir):
      if isfile(join(dir,f)):
         files.append( dir + f )
   return files

def pdfToText( file ):
   command = "python2 pdf2text.py " + file
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   text, error = process.communicate()
   text = str(text)
   return text

def searchAllFiles( files ):
   for file in files:
     print("Working on:", file)
     text = pdfToText( file )
     sentences = sent_tokenize( text )
     parts = file.split(".")
     outFile = parts[0].strip() + '_search_results.txt'
     out = open(outFile, "w")

     # loop over all the sentences checking each for ont terms
     lineCount = 1
     for sentence in sentences:
        for term in envo.classes():
           rdfsLabels = list(term.label) # list, there may be more than one label
           for label in rdfsLabels:
             if (label != ""): # ignore empty labels
               if (label in sentence):
                 out.write("'" + label + "' found at line " + str(lineCount) + "\n")
        lineCount += 1

     out.close()

# ENVO
envo = get_ontology("envo.owl").load()

# Sustainable Development Goals Interface Ontology
#sdg = get_ontology("https://raw.githubusercontent.com/SDG-InterfaceOntology/sdgio/master/sdgio.owl").load()

#dirCA = '/Users/narock/Software/git/decisions/docs/2017_CA/'
#filesCA = getFilesFromDir( dirCA )
#searchAllFiles( filesCA )

dirNY = '/Users/narock/Software/git/decisions/docs/2017_NY/'
filesNY = getFilesFromDir( dirNY )
searchAllFiles( filesNY )

