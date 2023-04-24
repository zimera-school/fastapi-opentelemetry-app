from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class GlCoa(Table, tablename="gl_coa"):
    coa_id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


class GlSubCoa(Table, tablename="gl_sub_coa"):
    sub_coa_id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


ID = "2023-04-13T22:28:42:103764"
VERSION = "0.109.0"
DESCRIPTION = "Add GL - CoA, SubCoA, Account"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table("GlCoa", tablename="gl_coa")

    manager.add_table("GlAccount", tablename="gl_account")

    manager.add_table("GlSubCoa", tablename="gl_sub_coa")

    manager.add_column(
        table_class_name="GlCoa",
        tablename="gl_coa",
        column_name="coa_id",
        db_column_name="coa_id",
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
        table_class_name="GlCoa",
        tablename="gl_coa",
        column_name="coa_code",
        db_column_name="coa_code",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 10,
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
        table_class_name="GlCoa",
        tablename="gl_coa",
        column_name="coa_name",
        db_column_name="coa_name",
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
        table_class_name="GlAccount",
        tablename="gl_account",
        column_name="account_id",
        db_column_name="account_id",
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
        table_class_name="GlAccount",
        tablename="gl_account",
        column_name="account_code",
        db_column_name="account_code",
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
        table_class_name="GlAccount",
        tablename="gl_account",
        column_name="sub_coa_id",
        db_column_name="sub_coa_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": GlSubCoa,
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
        table_class_name="GlAccount",
        tablename="gl_account",
        column_name="account_name",
        db_column_name="account_name",
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
        table_class_name="GlSubCoa",
        tablename="gl_sub_coa",
        column_name="sub_coa_id",
        db_column_name="sub_coa_id",
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
        table_class_name="GlSubCoa",
        tablename="gl_sub_coa",
        column_name="coa_id",
        db_column_name="coa_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": GlCoa,
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
        table_class_name="GlSubCoa",
        tablename="gl_sub_coa",
        column_name="sub_coa_code",
        db_column_name="sub_coa_code",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 10,
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
        table_class_name="GlSubCoa",
        tablename="gl_sub_coa",
        column_name="sub_coa_name",
        db_column_name="sub_coa_name",
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

    return manager
