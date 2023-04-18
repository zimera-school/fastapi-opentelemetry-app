from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Date
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.date import DateNow
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod


ID = "2023-03-28T06:12:53:024546"
VERSION = "0.109.0"
DESCRIPTION = "Add gl_period"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table("GlPeriod", tablename="gl_period")

    manager.add_column(
        table_class_name="GlPeriod",
        tablename="gl_period",
        column_name="period_id",
        db_column_name="period_id",
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
        table_class_name="GlPeriod",
        tablename="gl_period",
        column_name="period_name",
        db_column_name="period_name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 50,
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
        table_class_name="GlPeriod",
        tablename="gl_period",
        column_name="begin_period",
        db_column_name="begin_period",
        column_class_name="Date",
        column_class=Date,
        params={
            "default": DateNow(),
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
        table_class_name="GlPeriod",
        tablename="gl_period",
        column_name="end_period",
        db_column_name="end_period",
        column_class_name="Date",
        column_class=Date,
        params={
            "default": DateNow(),
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
        table_class_name="GlPeriod",
        tablename="gl_period",
        column_name="status",
        db_column_name="status",
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
