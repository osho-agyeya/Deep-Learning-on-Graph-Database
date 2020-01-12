import json
overrides = dict()

# There are too many layers and too many files to this config system
overrides.update(**{
    'local': {
        "neo4j_url": "bolt://localhost",
        "neo4j_user": "neo4j",
        "neo4j_password": "neo4j"
    },
    'remote': {
        'neo4j_url': 'bolt://796bafef-staging.databases.neo4j.io',
        'neo4j_user': 'readonly',
        'neo4j_password': '0s3DGA6Zq'
    },
    'floyd': { # Todo: implement me?
        'neo4j_url': 'bolt://796bafef-staging.databases.neo4j.io',
        'neo4j_user': 'readonly',
        'neo4j_password': '0s3DGA6Zq'
    },
})

try:
    with open('./config/local_overrides.json') as f:
        overrides.update(json.load(f))
except Exception:
    pass