from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import Boolean
from piccolo.columns.column_types import Date
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.date import DateNow
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class CoOrganization(Table, tablename="co_organization"):
    organization_id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


ID = "2023-03-23T11:30:02:253763"
VERSION = "0.109.0"
DESCRIPTION = "Add CoBranch, 1-M CoOrganization-CoBranch"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table("CoBranch", tablename="co_branch")

    manager.add_column(
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="branch_id",
        db_column_name="branch_id",
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="organization_id",
        db_column_name="organization_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": CoOrganization,
            "on_delete": OnDelete.no_action,
            "on_update": OnUpdate.no_action,
            "target_column": None,
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="branch_name",
        db_column_name="branch_name",
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="city",
        db_column_name="city",
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="post_code",
        db_column_name="post_code",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 5,
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="phone",
        db_column_name="phone",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 20,
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="email",
        db_column_name="email",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 30,
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="address",
        db_column_name="address",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 500,
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="active",
        db_column_name="active",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="date_started",
        db_column_name="date_started",
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
        table_class_name="CoBranch",
        tablename="co_branch",
        column_name="date_ended",
        db_column_name="date_ended",
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

    return manager
