# Samples for datasets

| Command                  | Description                                                   |
| ------------------------ | ------------------------------------------------------------- |
| [`list`](#list-datasets) | List datasets from a given workspace                          |
| `query`                  | Execute a DAX query on a given dataset from a given workspace |


## List datasets

List datasets the user/service principal has access to for a certain workspace

```bash
$ pbi dataset list --workspace {WORKSPACE_ID}

DATASET ID     NAME               CONFIGURED BY      CREATED DATE
-------------  -----------------  -----------------  ------------------------
DATASET_ID_1   DATASET_NAME_1     xxx@mycompany.com  2022-05-09T08:01:09.517Z
DATASET_ID_2   DATASET_NAME_2     yyy@mycompany.com  2022-08-18T09:04:16.867Z
```

## Execute query

Executes a DAX query to a premium dataset
```bash
$ pbi dataset query "EVALUATE ROW(\"distinct\", DISTINCTCOUNT('MyTable'[MyColumn]))"

2023-10-25 18:43:47 [info     ] EVALUATE ROW("distinct", DISTINCTCOUNT('MyTable'[MyColumn])) dataset=<Dataset id='DATASET_ID', name='DATASET_NAME', group_id='WORKSPACE_ID', configured_by='xxx@mycompany.com', created_date='2023-10-12T09:51:56.407Z'>
Duration: 0.1640009580005426
{'results': [{'tables': [{'rows': [{'[distinct]': 3602}]}]}]}
```

