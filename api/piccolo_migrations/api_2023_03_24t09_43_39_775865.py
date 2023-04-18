from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod


ID = "2023-03-24T09:43:39:775865"
VERSION = "0.109.0"
DESCRIPTION = "Create pm_role"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table("PmRole", tablename="pm_role")

    manager.add_column(
        table_class_name="PmRole",
        tablename="pm_role",
        column_name="project_role_id",
        db_column_name="project_role_id",
        column_class_name="Serial",
        column_class=Serial,
        params={
            "default": 0,
            "null": False,
            "primary_key": True,
            "unique": False,
            "index": True,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="PmRole",
        tablename="pm_role",
        column_name="project_role_name",
        db_column_name="project_role_name",
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
