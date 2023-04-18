from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry

extensions = ["uuid-ossp"]

DB = PostgresEngine(
    config={
        "database": "fastapidb",
        "user": "umohio",
        "password": "pmohio",
        "host": "localhost",
        "port": 5432,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["api.piccolo_app"]
)
