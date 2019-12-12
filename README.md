# redcap-export
Python (v3) script to export REDCap project data via API using PyCap package

Installation
------------
Run following command in terminal

    $ pip3 install -r requirements.txt

Configuration
-------------

Copy the `config.yaml.example` file to `config.yaml` and edit in your favorite text editor.
 
    $ cp config.yaml.example config.yaml

The config.yaml can contain a 1 or more projects to export.  Each project must
contain a token and a file prefix that should be unique. Also you can disable any of the optional configuration by
 adding
 ```#``` at the beginning of the line. 


Execute
-------
Run following command in terminal

    $ python3 export.py
