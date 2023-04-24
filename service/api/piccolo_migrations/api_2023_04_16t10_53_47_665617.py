from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2023-04-16T10:53:47:665617"
VERSION = "0.109.0"
DESCRIPTION = "Renama cdiff -> csh (cash short and over)"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.rename_column(
        table_class_name="GlSpecialAccount",
        tablename="gl_special_account",
        old_column_name="cdiff_acc_id",
        new_column_name="cso_acc_id",
        old_db_column_name="cdiff_acc_id",
        new_db_column_name="cso_acc_id",
    )

    return manager
