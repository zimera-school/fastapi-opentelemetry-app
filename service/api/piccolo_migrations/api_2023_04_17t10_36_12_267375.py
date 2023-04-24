from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod


ID = "2023-04-17T10:36:12:267375"
VERSION = "0.109.0"
DESCRIPTION = "Add inv_category"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table("InvCategory", tablename="inv_category")

    manager.add_column(
        table_class_name="InvCategory",
        tablename="inv_category",
        column_name="inv_category_id",
        db_column_name="inv_category_id",
        column_class_name="Serial",
        column_class=Serial,
        params={
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
        table_class_name="InvCategory",
        tablename="inv_category",
        column_name="inv_category_name",
        db_column_name="inv_category_name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 150,
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
