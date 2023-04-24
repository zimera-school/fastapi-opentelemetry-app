from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod


ID = "2023-04-14T09:52:30:702727"
VERSION = "0.109.0"
DESCRIPTION = "Add coa_classification column to gl_coa"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="GlCoa",
        tablename="gl_coa",
        column_name="coa_classification",
        db_column_name="coa_classification",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 1,
            "default": "",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    return manager
