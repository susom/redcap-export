import json
import redcap
import time
#define api main url
URL = "https://redcap.stanford.edu//api/"

ts = time.time()
#load json file contains configuration.
with open('config.json') as json_file:
    data = json.load(json_file)

##loop over the configuration.
for p in data['projects']:
    token = p['token']
    path = p['path']
    layout = p['layout']
    #if layout not defined or has wrong value then its `raw`
    if layout == '' or (layout != 'raw' and layout != 'label'):
        layout = 'raw'

    #initiate REDCap api object
    project = redcap.Project(URL, token)

    #export all records as csv string format
    all_data = project.export_records(format='csv', raw_or_label=layout.lower())

    #open file handler
    with open(path + 'projects_' + str(ts) + '.csv', 'w') as writeFile:
        writeFile.write(all_data)
    writeFile.close()
