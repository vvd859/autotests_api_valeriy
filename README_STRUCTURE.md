--/
--├── application.py
--├── checkers/
│   ├── checkers_helper.py
│   ├── station_types.py
│   └── stations.py
├── clients/
│   ├── api_helper.py
│   ├── devices.py
│   ├── flatgramms.py
│   ├── regions.py
│   ├── stations.py
│   └── stations_types.py
├── config.py
├── conftest.py
├── helpers/
│   ├── __init__.py
│   ├── helper.py
│   └── validSchema.py
├── Modules/
│   ├── App/
│   │   ├── __init__.py
│   │   ├── db/
│   │   │   └── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── station_type.py
│   │       └── stations.py
│   ├── docker-compose.yml
│   ├── DockerApp/
│   ├── Dockerfile.app
│   ├── DockerPg/
│   │   ├── Dockerfile.pg
│   │   └── init.sql
│   ├── main.py
│   ├── pg.dump
│   └── requirements.txt
├── Py_test.yaml
├── PyTest.postman_collection.json
├── README.md
├── README_STATION_TYPES.md
├── README_STATIONS.md
├── README_STRUCTURE.md
├── schemas/
│   ├── client_types.json
│   ├── datas.json
│   ├── empty.json
│   ├── events.json
│   ├── files.json
│   ├── logs.json
│   ├── numbers.json
│   ├── packs.json
│   ├── services.json
│   ├── station_types.json
│   ├── stations.json
│   └── statuses.json
├── struct.py
├── struct.txt
└── tests/
    ├── device/
    │   └── test_open_device_by_id.py
    ├── regions/
    │   └── test_get_configs_regions.py
    ├── station_types/
    │   └── test_station_types.py
    ├── stations/
    │   └── test_stations.py
    └── test_validation_schemas.py
