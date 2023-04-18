from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import DoublePrecision
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod


ID = "2023-03-29T07:42:04:122604"
VERSION = "0.109.0"
DESCRIPTION = "Add hr_{occupation, marriage_status, job_status}"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table("HrMarriageStatus", tablename="hr_marriage_status")

    manager.add_table("HrJobStatus", tablename="hr_job_status")

    manager.add_table("HrOccupation", tablename="hr_occupation")

    manager.add_column(
        table_class_name="HrMarriageStatus",
        tablename="hr_marriage_status",
        column_name="marriage_status_id",
        db_column_name="marriage_status_id",
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
        table_class_name="HrMarriageStatus",
        tablename="hr_marriage_status",
        column_name="marriage_status_name",
        db_column_name="marriage_status_name",
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
        table_class_name="HrJobStatus",
        tablename="hr_job_status",
        column_name="job_status_id",
        db_column_name="job_status_id",
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
        table_class_name="HrJobStatus",
        tablename="hr_job_status",
        column_name="job_status_name",
        db_column_name="job_status_name",
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
        table_class_name="HrOccupation",
        tablename="hr_occupation",
        column_name="occupation_id",
        db_column_name="occupation_id",
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
        table_class_name="HrOccupation",
        tablename="hr_occupation",
        column_name="occupation_name",
        db_column_name="occupation_name",
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
        table_class_name="HrOccupation",
        tablename="hr_occupation",
        column_name="salary",
        db_column_name="salary",
        column_class_name="DoublePrecision",
        column_class=DoublePrecision,
        params={
            "default": 0.0,
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
