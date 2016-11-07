import csv, os, scandir,sys

download_directory = '../source_file/files/'
output_directory = '../output_file/'

from datetime import datetime
print "start: " , datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('../source_file/sa1_6_list.csv', 'r') as sa_list:
    sa_list_reader = csv.reader(sa_list, delimiter=' ', quotechar='|')
    for sa_id in sa_list_reader:
        # print 'source_file_directory' . join(sa_id)
        downloaded_files_dir = os.path.join(download_directory + ''.join(sa_id))
        target_directory = os.path.join(output_directory + ''.join(sa_id))



        if os.path.exists(downloaded_files_dir):
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            de = scandir.scandir(downloaded_files_dir)
            while 1:
                try:
                    d = de.next()
                    # print d.path
                    os.system("tika-python -o " + target_directory + " parse text " + d.path)
                    # print words

                except StopIteration as _:
                    break

        print ''.join(sa_id) + " end: " , datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # sys.exit('break on first parse')







# import os
# os.system('tika-python -o ../output_file/ parse text ../source_file/files/6016827/01cf0cdf2946eae21c4df389332385a0.doc > /tmp/abhitesh.txt')

# #!/usr/bin/env python
# import tika
# from tika import parser
# tika.TikaClientOnly = True

# filepath = '../source_file/bio_tech.txt'
# #!/usr/bin/env python
# from tika import language
# print(language.from_file(filepath))

# parsed = parser.from_file(filepath)
# print(parsed["metadata"])
# print(parsed["content"])
