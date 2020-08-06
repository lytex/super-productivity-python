import pandas as pd
import json
import random
import string
import datetime

int(datetime.datetime.now().timestamp())  

def generate_id():
    return (''.join(random.choice(string.ascii_letters+string.digits+'_-')
                        for _ in range(random.choice(range(9,11)))))

with open('1.json') as f:
    j = json.loads(f.read())

## TODO Buscar los ids en 3.json y ponerlo en todos los sitios en los que está

id = generate_id()
project_id = 'VqTvrMl6c'
j['task']['ids'].append(id)
j['project']['entities'][project_id]['taskIds'].append(id)

j['task']['entities'][id] = {
    'id': id,
    'projectId': project_id,
    'subTaskIds': [],
    'timeSpentOnDay': {},
    'timeSpent': 0,
    'timeEstimate': 0,
    'isDone': False,
    'doneOn': None,
    'title': 'Tarea de prueba',
    'notes': '',
    'tagIds': [],
    'parentId': None,
    'reminderId': None,
    'created': int(datetime.datetime.now().timestamp()*1000),
    'repeatCfgId': None,
    '_showSubTasksMode': 2,
    'attachments': [],
    'issueId': None,
    'issuePoints': None,
    'issueType': None,
    'issueAttachmentNr': None,
    'issueLastUpdated': None,
    'issueWasUpdated': None
}

with open('2.json', 'w') as f:
    json.dump(j, f)
