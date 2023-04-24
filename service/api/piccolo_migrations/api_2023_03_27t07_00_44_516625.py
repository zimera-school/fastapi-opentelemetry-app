from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
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


ID = "2023-03-27T07:00:44:516625"
VERSION = "0.109.0"
DESCRIPTION = "Fixed FK constraints in CoPartyToCoPartyCategorya"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.alter_column(
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="party_id",
        db_column_name="party_id",
        params={"references": CoParty},
        old_params={"references": CoPartyCategory},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
    )

    manager.alter_column(
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="party_category_id",
        db_column_name="party_category_id",
        params={"references": CoPartyCategory},
        old_params={"references": CoParty},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
    )

    return manager
