# python-tools
Random Python scripts I've written over the years to automate things that got too annoying to do manually.

# Installation
You should be able to just copy the repository and run the files. Note that some of them may only work on Unix based systems.

# Usage

## backup.py
`` bash
python backup.py
```

This generates a series of shell commands that can be used to back up a time series MySQL table. I haven't expanded it yet to take options from the command line but it should be straightforward to modify the script.

## django_template_hierarchy.py
``` bash
python django_template_hierarchy_py /var/www/djangoproject/
```

This should give you a quick view of the hierarchy of the Django template "includes" and "extends" commands in your project. The neat thing is that this is recursive so you can quickly see which template files affect others. For example:
``` python
{ 'templates/base.html': {'templates/aux.html': {'templates/about.html': {},
                                                 'templates/press.html': {}}},
  'templates/error.html': {'templates/404.html': {}, 'templates/500.html': {}},
  'templates/home.html': {'templates/registration/registration_form.html': {},
                         'templates/registration/registration_home.html': {},
                         'templates/registration/registration_submitted.html': {}}
}
```

## levenshtein.py

Found this [script online](http://hetland.org/coding/python/levenshtein.py) and was using for some analysis.

## mysql_to_utf8.py

Another quick script I found [online](http://stackoverflow.com/questions/2108824/mysql-incorrect-string-value-error-when-save-unicode-string-in-django/11597447#11597447) to help convert a MySQL database to UTF8.

# License

Copyright 2015 Dan Goldin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.%
