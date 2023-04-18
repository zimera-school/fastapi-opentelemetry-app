from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod


ID = "2023-04-10T05:49:24:114846"
VERSION = "0.109.0"
DESCRIPTION = "Add hr_employee - address"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="HrEmployee",
        tablename="hr_employee",
        column_name="address",
        db_column_name="address",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 200,
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
