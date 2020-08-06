import pandas as pd
import json

def parse_sp_json(path):
    with open(path) as f:
        j = json.loads(f.read())

    tasks = pd.DataFrame()
    for k in j['taskArchive']['entities'].keys():
        tasks = pd.concat([tasks, pd.Series(j['taskArchive']['entities'][k])], axis=1)
    tasks = tasks.T.reset_index(drop=True)
    
    metrics = get_entities('metric', j)
    improvements = get_entities('improvement', j)
    obstructions = get_entities('obstruction', j)

    return tasks, metrics, improvements, obstructions


def get_entities(key, j):
    df = pd.DataFrame()
    for project in j[key].keys():
        project_df = j[key][project]['entities']
        for k, v in project_df.items():
            assert k == v['id']
            df = pd.concat([df, pd.Series(v)], axis=1)
    df = df.T.reset_index(drop=True)
    return df



tasks, metrics, improvements, obstructions = parse_sp_json('super-productivity-backup.json')