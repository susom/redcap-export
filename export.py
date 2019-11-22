import json
import redcap
from redcap import RedcapError
import time


# initiate the class
class Export:
    def process(self):
        # define api main url
        URL = "https://redcap.stanford.edu/api/"

        ts = time.time()
        # load json file contains configuration.
        with open('config.json') as json_file:
            data = json.load(json_file)

        default_url = data['defaults']['api_url']
        default_path = data['defaults']['output_path']
        default_raw_or_label = data['defaults']['raw_or_label']

        ##loop over the configuration.
        for p in data['projects']:
            # get the token
            token = p['token']

            # get api url if existed
            if "api_url" in p and p['api_url'] != '':
                url = p['api_url']
            else:
                url = default_url

            # get if label or raw  if layout not defined or has wrong value then its `raw`
            if "raw_or_label" in p and p['raw_or_label'] != '' and (
                    p['raw_or_label'] == 'raw' or p['raw_or_label'] == 'label'):
                layout = p['raw_or_label']
            else:
                layout = default_raw_or_label

            # initiate REDCap api object
            project = redcap.Project(url, token)

            # exported file name prefix.
            prefix = p['file_prefix']

            # specify fields if defined
            if "fields" in p:
                fields = p["fields"]
            else:
                fields = []

            # export all records as csv string format
            try:
                # if arm is defined then only export data for that arm.
                if "events" in p:
                    all_data = project.export_records(format='csv', raw_or_label=layout.lower(), events=p["events"],
                                                      fields=fields)
                else:
                    # export all data for that project
                    all_data = project.export_records(format='csv', raw_or_label=layout.lower(), fields=fields)
            except RedcapError:
                print("Can not export please try again")

            # open file handler
            with open(default_path + prefix + '.csv', 'w') as writeFile:
                writeFile.write(all_data)
            writeFile.close()


export = Export()
export.process()
