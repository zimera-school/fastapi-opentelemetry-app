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


class GlAccount(Table, tablename="gl_account"):
    account_id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


ID = "2023-04-16T14:45:22:940530"
VERSION = "0.109.0"
DESCRIPTION = (
    "Add prje (project expense) and prjr (project revenue) to special_account"
)


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="GlSpecialAccount",
        tablename="gl_special_account",
        column_name="prje_acc_id",
        db_column_name="prje_acc_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": GlAccount,
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
        table_class_name="GlSpecialAccount",
        tablename="gl_special_account",
        column_name="prjr_acc_id",
        db_column_name="prjr_acc_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": GlAccount,
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

    return manager
