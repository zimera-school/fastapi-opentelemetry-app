from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import DoublePrecision
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod


ID = "2023-03-29T05:51:10:131317"
VERSION = "0.109.0"
DESCRIPTION = "Add hr_revenue"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table("HrRevenue", tablename="hr_revenue")

    manager.add_column(
        table_class_name="HrRevenue",
        tablename="hr_revenue",
        column_name="revenue_id",
        db_column_name="revenue_id",
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
        table_class_name="HrRevenue",
        tablename="hr_revenue",
        column_name="revenue_name",
        db_column_name="revenue_name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
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

    manager.add_column(
        table_class_name="HrRevenue",
        tablename="hr_revenue",
        column_name="amount",
        db_column_name="amount",
        column_class_name="DoublePrecision",
        column_class=DoublePrecision,
        params={
            "default": 0.0,
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
