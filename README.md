# redcap-export
Python script to export REDCap project data via API using PyCap package

Installation
------------
 

    ``$ pip install -r requirements.txt``

Configuration
-------------

define json object for each project you want to export. 

```
{
      "token" : "[API_PROJECT_TOKEN]",
      "path" : "[PATH_WHERE_TO_SAVE_FILE]",
      "layout" : "[FOR_DROPDOWN_AND_CHECKBOXES_SPECIFY_RAW_OR_LABEL]"
}
```
