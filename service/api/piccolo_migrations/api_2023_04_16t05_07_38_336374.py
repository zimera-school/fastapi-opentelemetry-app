from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2023-04-16T05:07:38:336374"
VERSION = "0.109.0"
DESCRIPTION = "Delete specialaccount"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.drop_table(
        class_name="GlSpecialAccount", tablename="gl_special_account"
    )

    return manager
