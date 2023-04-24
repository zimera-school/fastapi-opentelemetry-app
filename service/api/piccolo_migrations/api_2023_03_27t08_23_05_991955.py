from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod


ID = "2023-03-27T08:23:05:991955"
VERSION = "0.109.0"
DESCRIPTION = "Delete CoParty, CoPartyCategory, and CoPartyToCoPartyCategory"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.drop_table(
        class_name="CoPartyToCoPartyCategory",
        tablename="co_party_to_co_party_category",
    )

    manager.drop_table(class_name="CoParty", tablename="co_party")

    manager.drop_table(
        class_name="CoPartyCategory", tablename="co_party_category"
    )

    return manager
