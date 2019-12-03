import yaml
import redcap
from redcap import RedcapError
import datetime


class Export:
    # API url could be default or specified per project.
    url = ""

    # output path to where to save exported data
    outpu_path = ""

    # checkboxes and dropboxes represented as values, labels or both
    raw_or_label = ""

    # type out output from redcap and file type. (json,csv, xml, df)
    format = ""

    # output file name could be default or specified per project.
    file_prefix = ""

    # array of defined projects in config.yaml
    projects = []

    # data dict to be used in redcap export function.
    args = {}

    # initiate the class
    def __init__(self):
        # read config.yaml
        with open("config.yaml", 'r') as stream:
            try:
                data = yaml.safe_load(stream)

                # define default section
                self.url = data['defaults']['url']
                self.outpu_path = data['defaults']['output_path']
                self.raw_or_label = data['defaults']['raw_or_label']
                self.format = data['defaults']['format']
                self.file_prefix = data['defaults']['file_prefix']
                self.projects = data['projects']
            except yaml.YAMLError as exc:
                print(exc)

    def process(self):

        # loop over the projects array.
        for p in self.projects:
            # get the token
            try:
                self.args['token'] = p['token']
            except None:
                print("Token must be provided")

            # get api url if existed
            if "url" in p and p['url'] != '':
                self.args['url'] = p['url']
            else:
                self.args['url'] = self.url

            # get if label or raw  if layout not defined or has wrong value then its `raw`
            if "raw_or_label" in p and p['raw_or_label'] != '' and (
                    p['raw_or_label'] == 'raw' or p['raw_or_label'] == 'label'):
                self.args['raw_or_label'] = p['raw_or_label'].lower()
            else:
                self.args['raw_or_label'] = self.raw_or_label

            # check if format is defined otherwise user default one
            if "format" in p and p['format'] != '' and (
                    p['format'] == 'raw' or p['format'] == 'label' or p['format'] == 'both'):
                self.args['format'] = p['format']
            else:
                self.args['format'] = self.format

            # check if format is defined otherwise user default one
            if "export_survey_fields" in p and p['export_survey_fields'] != '' and (
                    p['export_survey_fields'] == 'True' or p['export_survey_fields'] == 'False'):
                self.args['export_survey_fields'] = p['export_survey_fields']
            else:
                self.args['export_survey_fields'] = False

            # check if export_checkbox_labels
            if "export_checkbox_labels" in p and p['export_checkbox_labels'] != '' and (
                    p['export_checkbox_labels'] == 'True' or p['export_checkbox_labels'] == 'False'):
                self.args['export_checkbox_labels'] = p['export_checkbox_labels']
            else:
                self.args['export_checkbox_labels'] = False

            # check if format is defined otherwise user default one
            if "export_data_access_groups" in p and p['export_data_access_groups'] != '' and (
                    p['export_data_access_groups'] == 'True' or p['export_data_access_groups'] == 'False'):
                self.args['export_data_access_groups'] = p['export_data_access_groups']
            else:
                self.args['export_data_access_groups'] = False

            # check if format is defined otherwise user default one
            if "filter_logic" in p and p['filter_logic'] != '':
                self.args['filter_logic'] = p['filter_logic']
            else:
                self.args['filter_logic'] = ""

            # exported file name prefix.
            # get api url if existed
            if "file_prefix" in p and p['file_prefix'] != '':
                self.args['file_prefix'] = p['file_prefix']
            else:
                self.args['file_prefix'] = self.file_prefix

                # specify fields if defined
            if "fields" in p:
                self.args['fields'] = self.__getvalues(p["fields"])
            else:
                self.args['fields'] = []

            # specify events if defined
            if "events" in p:
                self.args['events'] = self.__getvalues(p["events"])
            else:
                self.args['events'] = []

            # specify records if defined
            if "records" in p:
                self.args['records'] = self.__getvalues(p["records"])
            else:
                self.args['records'] = []

            # specify records if defined
            if "forms" in p:
                self.args['forms'] = self.__getvalues(p["forms"])
            else:
                self.args['forms'] = []

            # specify records if defined
            if "df_kwargs" in p:
                self.args['df_kwargs'] = self.__getvalues(p["df_kwargs"])
            else:
                self.args['df_kwargs'] = []

            # specify overrides events list
            if "event_name" in p:
                self.args['event_name'] = p["event_name"]
                # make sure events is empty
                self.args['events'] = []
            else:
                self.args['event_name'] = ""

            # initiate REDCap api object
            project = redcap.Project(self.args['url'], self.args['token'])
            self.__write_to_file(self.__export(project))

    # write exported data to specified file
    def __write_to_file(self, all_data):
        # open file handler

        with open(self.outpu_path + self.args['file_prefix'] + '.' + self.args['format'], 'w') as writeFile:
            writeFile.write(all_data)
        writeFile.close()
        self.__update_logfile()
        print("export completed successfully")

    # once everything is done log time to mark this as last successful update.
    def __update_logfile(self):
        with open(self.outpu_path + "last_successful_update.log", 'w') as writeFile:
            writeFile.write(str(datetime.datetime.now()))
        writeFile.close()

    # get data dictionary values because they are represented in array in yaml file
    @staticmethod
    def __getvalues(dlist):
        result = []
        for l in dlist:
            result.append(l['name'])
        return result

    # connect to REDCap API and export data based in yaml configuration for specified token
    def __export(self, project):
        # export all records as csv string format
        try:
            # if arm is defined then only export data for that arm.
            all_data = project.export_records(records=self.args['records'], fields=self.args['fields'],
                                              forms=self.args['forms'],
                                              events=self.args['events'], raw_or_label=self.args['raw_or_label'],
                                              event_name=self.args['event_name'],
                                              format=self.args['format'],
                                              export_survey_fields=self.args['export_survey_fields'],
                                              export_data_access_groups=self.args['export_data_access_groups'],
                                              df_kwargs=self.args['df_kwargs'],
                                              export_checkbox_labels=self.args['export_checkbox_labels'],
                                              filter_logic=self.args['filter_logic'])

        except RedcapError:
            print("Can not export please try again")
        return all_data


# init the object
export = Export()

# process config.yaml
export.process()
