#!/usr/bin/python

import datetime

start = datetime.datetime.strptime("2012-11-16", "%Y-%m-%d")
end = datetime.datetime.strptime("2013-10-25", "%Y-%m-%d")

table_name = 'sql_table_name_here';

dates = []
while start < end:
    s = start.strftime('%Y-%m-%d')
    start += datetime.timedelta(days=1)
    e = start.strftime('%Y-%m-%d')
    dates.append((s,e))

HOST = 'host'
PORT = '3306'
USER = 'user'
PASS = 'password'
DB = 'database'
DATE_FIELD = 'ymd' # Maybe timestamp? datetime?
S3_FOLDER = 's3_backup_folder'

for s,e in dates:
    if True:
        print "/usr/local/mysql/bin/mysql -h{} --port={} -u{} -p{} {} -e \"SELECT * from {} where {} >= '{}' and {} < '{}'\" > {}_{}_{}.csv".format(HOST, PORT, USER, PASS, DB, table_name, DATE_FIELD, s, DATE_FIELD, e, table_name, s, e)
        print "gzip {}_{}_{}.csv".format(table_name, s, e)
        print "aws s3 cp {}_{}_{}.csv.gz s3://{}/{}/".format(table_name, s, e, S3_FOLDER, table_name)
        print "rm {}_{}_{}.csv.gz".format(table_name, s, e)
