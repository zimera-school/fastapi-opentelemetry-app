from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod


ID = "2023-03-26T17:14:22:329772"
VERSION = "0.109.0"
DESCRIPTION = "Add primary key for CoPartyToCoPartyCategory"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
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

    return manager
