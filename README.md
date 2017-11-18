# python-tools

Random Python scripts I've written over the years to automate things that got too annoying to do manually.

# Installation

For most of these you should be able to just copy the repository and run the files. Some will require the dependencies specificed in requirements.txt.

# Usage

## backup.py
``` bash
$ python backup.py

$ python backup.py > backup.sh
$ sh backup.sh
```

This generates a series of shell commands that can be used to back up a time series MySQL table. I haven't expanded it yet to take options from the command line but it should be straightforward to modify the script.

## django_template_hierarchy.py
``` bash
$ python django_template_hierarchy_py /var/www/djangoproject/
```

This should give you a quick view of the hierarchy of the Django template "includes" and "extends" commands in your project. The neat thing is that this is recursive so you can quickly see which template files are dependent on others. For example:

```
{ 'templates/base.html': {'templates/aux.html': {'templates/about.html': {},
                                                 'templates/press.html': {}}},
  'templates/error.html': {'templates/404.html': {}, 'templates/500.html': {}},
  'templates/home.html': {'templates/registration/registration_form.html': {},
                         'templates/registration/registration_home.html': {},
                         'templates/registration/registration_submitted.html': {}}
}
```

## levenshtein.py

Found this [function online](http://hetland.org/coding/python/levenshtein.py) and was using for some analysis.

## mysql_to_utf8.py

Another script I [found online](http://stackoverflow.com/questions/2108824/mysql-incorrect-string-value-error-when-save-unicode-string-in-django/11597447#11597447) to help convert a MySQL database to UTF8.

## generate_password.py

Simple utility to generate variable length passwords. By default it will generate random strings of 32 characters which can be override from the command line.

``` bash
$ python generate_password.py
S1wWUn3X2JMl5rlKrxMZrpGoU8MZsRMg
$ python generate_password.py
t67AAoFj0v7VuN5jqoAKppGkJ3d0mArUyTPQB9cBvx6OE99Jn1r4jNYqGsWBIUiD
```

## strip_tags.py

Remove the HTML tags from a given file.

``` bash
$ python strip_tags.py file.html
```

## ec2_to_csv.py

Generate a CSV file with your EC2 instance data.

``` bash
$ python ec2_to_csv.py
$ python ec2_to_csv.py out.csv
```

## json_csv.py

Generate a CSV file from a JSON file. This is meant to be a more generic version of ec2_to_csv.py but is still a work in progress since it hasn't been heavily tested and probably doesn't work for complex use cases.

``` bash
$ python json_csv.py instances-small.json Reservations.Instances.PublicDnsName,Reservations.Instances.PrivateDnsName
```

## plotter.py

Accepts tab delimited data via stdin and generates a simple chart. It unfortunately has a dependency on matplotlib but at some point I'll try to clean that up.

``` bash
$ pbpaste | ./plotter.py
```

## analyze_aws_details.py

Load the AWS usage details log file and generate some charts to highlight where the usage is coming from.

``` bash
$ python analyze_aws_details.py awsfile.csv
```

## analyze_history.py

Go through the specified file which should be in the form of the history command output and see the most frequent commands used.

``` bash
$ history > hist
$ python analyze_history.py hist
```

## date_replace.py

Oftentimes I need to generate a set of commands where each one is a day of a date range. This script automates that.

``` bash
$ python date_replace.py "DELETE FROM table where ymd = '{{ YMD }}';" 2017-10-01 2017-11-01
```

## prepend_append.py

Rather than keep trying to relearn the syntax for sed this is a simple script to prepend and append strings to every line in a file.

``` bash
$ python prepend_append.py filename.csv "StartOfLine" "EndOfLine"
```

## archive_tables.py

A pretty hacky script to archive tables as csv files to S3 by date range. The last argument is the day "step" and for small tables it can be large while large tables should keep it at 1 so only one day is archived at a time. To avoid having a long argument list some of the info is hardcoded in the file but it can be simplified.

``` bash
$ python archive_tables.py table_name 2012-08-09 2013-01-13 28
```
