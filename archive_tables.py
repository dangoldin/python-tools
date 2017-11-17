#! /usr/bin/env python

import datetime
import sys

MYSQL_HOST = 'host'
MYSQL_USER = 'user'
MYSQL_PASS = 'pass'
MYSQL_PORT = 3306
MYSQL_DB = 'db'
S3_BUCKET = 's3Bucket'

table_name = sys.argv[1]
start = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d")
end = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d")
if len(sys.argv) == 5:
    day_diff = int(sys.argv[4])
else:
    day_diff = 1

dates = []
while start < end:
    s = start.strftime('%Y-%m-%d')
    start += datetime.timedelta(days=day_diff)
    e = start.strftime('%Y-%m-%d')
    dates.append((s,e))

for s,e in dates:
    print "/usr/local/mysql/bin/mysql -h{} --port={} -u{} -p{} {} -e \"SELECT * from {} where ymd >= '{}' and ymd < '{}'\" > {}_{}_{}.csv".format(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB, table_name, s, e, table_name, s, e)
    print "gzip {}_{}_{}.csv".format(table_name, s, e)
    print "aws s3 cp {}_{}_{}.csv.gz s3://{}/{}/".format(table_name, s, e, S3_BUCKET, table_name)
    print "rm {}_{}_{}.csv.gz".format(table_name, s, e)
