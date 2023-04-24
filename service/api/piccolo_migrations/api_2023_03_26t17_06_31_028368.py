from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Serial
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


ID = "2023-03-26T17:06:31:028368"
VERSION = "0.109.0"
DESCRIPTION = "change table name, class name and column name for join table - CoPartyToCoPartyCategory"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.rename_table(
        old_class_name="CoPartyToCategory",
        old_tablename="co_party_to_category",
        new_class_name="CoPartyToCoPartyCategory",
        new_tablename="co_party_to_co_party_category",
    )

    manager.drop_column(
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="category_id",
        db_column_name="category_id",
    )

    manager.drop_column(
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="co_party_to_category_id",
        db_column_name="co_party_to_category_id",
    )

    manager.add_column(
        table_class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
        column_name="party_category_id",
        db_column_name="party_category_id",
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

    return manager
