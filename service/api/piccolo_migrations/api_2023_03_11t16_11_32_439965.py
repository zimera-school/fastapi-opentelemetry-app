from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2023-03-11T16:11:32:439965"
VERSION = "0.109.0"
DESCRIPTION = "beginning of migration"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    def run():
        print(f"running {ID}")

    manager.add_raw(run)

    return manager
