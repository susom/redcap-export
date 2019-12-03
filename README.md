# redcap-export
Python script to export REDCap project data via API using PyCap package   one more test using classic projec 

Installation
------------
 Run following command in terminal

    $ pip install -r requirements.txt

Configuration
-------------

define json object for each project you want to export. 

```
{
  "defaults": {
    "api_url": "[DEFAULT_API_URL]",
    "output_path": "[DEFAULT_OUT_PATH]",
    "raw_or_label": "[RAW_OR_LABEL]"
  },
  "projects": [
    {
      "token" : "[PROJECT_API_TOKEN]",
      "api_url": "[SPECIFY_URL_IF_DIFFERENT_THAN_DEFAULT_ONE]",
      "file_prefix" : "[FILE_PREFIX]",
      "raw_or_label" : "[DEFINE_THIS_IF_DIFFERENT_THAN_DEFAULT_RAW_OR_LABLE]",
      "events" : [
        "[ARRAY_OF_UNIQUE_REDCAP_EVENTS_NAMES]"
      ],
      "fields": [
        "[ARRAY_OF_UNIQUE_FIELDS_NAMES]"
      ]
    }
  ]
}
```

Execute
-------
Run following command in terminal

    $ python export.py
