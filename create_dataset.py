import pickle
import cPickle
import numpy
import os
import re
import sys
import csv, scandir
import tika
# import unidecode

import unicodedata

from nltk.stem.snowball import SnowballStemmer
import string

from tika import parser
tika.TikaClientOnly = True


# sys.exit("done")


# sys.path.append( "../tools/" )
from parse_text import parseOutText

label_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0
import codecs
import sys
# Set default encoding to 'UTF-8' instead of 'ascii'
# http://stackoverflow.com/questions/11741574/how-to-set-the-default-encoding-to-utf-8-in-python
# Bad things might happen though
reload(sys)
sys.setdefaultencoding("UTF8")

download_directory = '../source_file/files/'

output_files = '../output_file/'

from datetime import datetime
print "start: " , datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def strip_accents(text):
  """
  Strip accents from input String.

  :param text: The input string.
  :type text: String.

  :returns: The processed String.
  :rtype: String.
  """
  try:
      text = unicode(text, 'utf-8')
  except NameError: # unicode is a default on python 3
      pass
  text = unicodedata.normalize('NFD', text)
  text = text.encode('ascii', 'ignore')
  text = text.decode("utf-8")
  return str(text)

with open('../source_file/sa1_6_list.csv', 'r') as sa_list:
  sa_list_reader = csv.reader(sa_list, delimiter=' ', quotechar='|')
  for sa_id in sa_list_reader:

    # downloaded_files_dir = os.path.join(download_directory + ''.join(sa_id))
    downloaded_files_dir = os.path.join(output_files + ''.join(sa_id))

    if os.path.exists(downloaded_files_dir):
      de = scandir.scandir(downloaded_files_dir)
      while 1:
          try:
              d = de.next()
              print d.path

              f = codecs.open(d.path, "r")
              # f = codecs.open('../output_file/6016827/b42fa85a91f3bef406f922908692c6a9.docx_meta.json', "r")
              f.seek(0)  ### go back to beginning of file (annoying)
              content = f.read()
              # print content
              # print "\n\n-----------------\n\n"

              words = ""
              if len(content) > 1:

                text_string = content.translate(string.maketrans("", ""), string.punctuation)
                # text_string =  stripNonAlphaNum(text_string)
                # text_string =  ' '.join(text_string)
                text_string = strip_accents(text_string)

                word_list = text_string.split()

                # remove only non alpha words from the string
                word_list=[i for i in word_list if i.isalpha()]

                # stemming
                stemmer = SnowballStemmer("english")
                stem_word_list = [stemmer.stem(word) for word in word_list]
                # words = (" " . join(stem_word_list))
                # print stem_word_list


                # # remove stopwords
                from nltk.corpus import stopwords
                filtered_words = [word for word in stem_word_list if word not in stopwords.words('english')]
                # print filtered_words

                # sys.exit('-random utf-8 check')


                words = (" " . join(filtered_words))
                # print words
                word_data.append(words)
                label_data.append(''.join(sa_id))

                # print words

          except StopIteration as _:
              break

      # sys.exit('--stopped after first iteration--')


pickle.dump( word_data, open("word_data.pkl", "w") )
pickle.dump( label_data, open("document_subject_area.pkl", "w") )
print "--data set created--"
print "end: " , datetime.now().strftime("%Y-%m-%d %H:%M:%S")
