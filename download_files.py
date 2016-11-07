import boto3
import csv
import sys
import hmac
import os,time
import urllib
import urlparse
# read source files for each SA
# Download all the files from s3 in resp. directories.
reload(sys)
sys.setdefaultencoding("UTF8")

# reading from ~/.aws/credentials
s3 = boto3.resource('s3')
s3_bucket = 'prod-whiteboard-client-files'
bucket = s3.Bucket(s3_bucket)

source_file_directory = '../source_file/file_list/'
download_directory = '../source_file/files/'
max_sa_download_count = 5

download_sa_count = 0
with open('../source_file/sa1_6_list.csv', 'r') as sa_list:
    sa_list_reader = csv.reader(sa_list, delimiter=' ', quotechar='|')
    for sa_id in sa_list_reader:
        # print 'source_file_directory' . join(sa_id)
        sa_id_file_list = '{dir}{filename}.csv'.format(dir=source_file_directory, filename=''.join(sa_id))
        if not os.path.exists(sa_id_file_list):
            continue


        target_directory =  download_directory + ''.join(sa_id) + "/"

        # if folder already exists , skip the sa - assuming the existing sa has been downloaded completely
        if os.path.exists(target_directory):
            print "skipped :" , ''.join(sa_id)
            continue

        # download only 10 sa folders at a time
        if(download_sa_count == max_sa_download_count):
            sys.exit('Max count reached for download')
        download_sa_count = download_sa_count+1

        print sa_id_file_list

        # f = open(sa_id_file_list, mode = 'rb',encoding = 'utf-8') # opens the csv file
        f = open(sa_id_file_list, 'rb')
        try:
            reader = csv.reader(f)  # creates the reader object
            for row in reader:   # iterates the rows of the file in orders
                s3_file_path =  ''.join(row)
                # print s3_file_path
                filename = s3_file_path.split('/')
                file_name, file_ext = os.path.splitext(filename[len(filename) -1])
                # print file_name, file_ext


                m = hmac.new(sa_id_file_list, s3_file_path)
                download_file_name = m.hexdigest()

                # target_directory =  download_directory + ''.join(sa_id) + "/"

                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)



                s3_file_name = [filename[0] , filename[1] , urllib.quote(filename[2])]
                download_s3_file_path = '/'.join(s3_file_name)

                print 'Downloading: ', download_s3_file_path,
                bucket.download_file(s3_file_path, target_directory + download_file_name + file_ext)
                print " " + download_file_name + ":Done","\n"

        finally:
            f.close()      # closing

        print "sleeping for 1 sec \n"
        # time.sleep(1)
        # sys.exit("Error message")


# import boto3
# s3 = boto3.resource('s3')
# s3_bucket = 'prod-whiteboard-client-files'
# bucket = s3.Bucket(s3_bucket)
# bucket.download_file(s3_file_path, local_file_path)
