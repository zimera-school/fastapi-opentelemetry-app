from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import Date
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.date import DateNow
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class CoParty(Table, tablename="co_party"):
    party_id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


class CoPartyCategory(Table, tablename="co_party_category"):
    party_category_id = Serial(
        default=0,
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


ID = "2023-03-27T07:21:25:223136"
VERSION = "0.109.0"
DESCRIPTION = "Recreate CoPartyToCoPartyCategory"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table(
        "CoPartyToCoPartyCategory", tablename="co_party_to_co_party_category"
    )

    manager.add_column(
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="co_party_to_co_party_category_id",
        db_column_name="co_party_to_co_party_category_id",
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
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="party_category_id",
        db_column_name="party_category_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": CoPartyCategory,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
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
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="party_id",
        db_column_name="party_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": CoParty,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
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
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="since",
        db_column_name="since",
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
