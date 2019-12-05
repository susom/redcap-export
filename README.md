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
contain a token and a file prefix that should be unique.

define default configuration then array of projects in the `config.yaml`

```
# default configurations
defaults:
  url: "[HOST_NAME]/api/"
  output_path: "[PATH_TO_SAVED_FILE]"
  raw_or_label: "[DEFAULT_RAW_LABEL_BOTH]"
  file_prefix: "[DEFAULT_FILE_NAME]"
  format: "[JSON_CSV_DF_XML]"
# define your projects configuration
projects:
  # Required Parameters
  - token: "[PROJECT_TOKEN]"
    # Optional Parameters
    #url: "[FILL_THIS_IF_DIFFERENT_FROM_DEFAULT_URL]"
    #file_prefix: "[FILL_THIS_IF_DIFFERENT_FROM_DEFAULT_FILE_PREFIX]"
    #   Export Optional Parameters
    #    ----------
    #    records: list
    #      array of record names specifying specific records to export.
    #      by default, all records are exported
    #    records:
    #      - name: [RECORD_ID]
    #    fields: list
    #      array of field names specifying specific fields to pull
    #      by default, all fields are exported
    #fields:
    #  - name: "[FIELD_NAME_1]"
    #  - name: "[FIELD_NAME_2]"
    #    forms: list
    #      array of form names to export. If in the web UI, the form
    #      name has a space in it, replace the space with an underscore
    #      by default, all forms are exported
    #    forms:
    #      - name: "[INSTRUMENT_NAME_1]"
    #      - name: "[INSTRUMENT_NAME_2]"
    #    events: list
    #      an array of unique event names from which to export records
    #      :note: this only applies to longitudinal projects
    events:
      - name: "[EVENT_NAME_1]"
      - name: "[EVENT_NAME_2]"
    #    raw_or_label: (``'raw'``), ``'label'``, ``'both'``
    #      export the raw coded values or labels for the options of
    #      multiple choice fields, or both
    raw_or_label: "[FILL_THIS_IF_DIFFERENT_FROM_DEFAULT_RAW_LABEL]"
    #    event_name: (``'label'``), ``'unique'``
    #      export the unique event name or the event label
    event_name: "[EVENT_UNIQUE_NAME]"
    #    format: (``'json'``), ``'csv'``, ``'xml'``, ``'df'``
    #      Format of returned data. ``'json'`` returns json-decoded
    #      objects while ``'csv'`` and ``'xml'`` return other formats.
    #      ``'df'`` will attempt to return a ``pandas.DataFrame``.
    format: "[FILL_THIS_IF_DIFFERENT_FROM_DEFAULT]"
    #    export_survey_fields: (``False``), True
    #      specifies whether or not to export the survey identifier
    #      field (e.g., "redcap_survey_identifier") or survey timestamp
    #      fields (e.g., form_name+"_timestamp") when surveys are
    #      utilized in the project.
    export_survey_fields: "[TRUE_FALSE]"
    #    export_data_access_groups: (``False``), ``True``
    #      specifies whether or not to export the
    #      ``"redcap_data_access_group"`` field when data access groups
    #      are utilized in the project.
    #      :note: This flag is only viable if the user whose token is
    #        being used to make the API request is *not* in a data
    #        access group. If the user is in a group, then this flag
    #        will revert to its default value.
    export_data_access_groups: [TRUE_FALSE]
    #    df_kwargs: dict
    #      Passed to ``pandas.read_csv`` to control construction of
    #      returned DataFrame.
    #      by default, ``{'index_col': self.def_field}``
    #    export_checkbox_labels: (``False``), ``True``
    #      specify whether to export checkbox values as their label on
    #      export.
    #    filter_logic: string
    #      specify the filterLogic to be sent to the API.
    filter_logic: "[REDCAP_FILTER_LOGIC]"
```

Execute
-------
Run following command in terminal

    $ python3 export.py
