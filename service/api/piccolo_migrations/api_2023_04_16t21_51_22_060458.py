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


class HrEmployee(Table, tablename="hr_employee"):
    emp_id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


class PmProject(Table, tablename="pm_project"):
    project_id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


class PmRole(Table, tablename="pm_role"):
    project_role_id = Serial(
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


ID = "2023-04-16T21:51:22:060458"
VERSION = "0.109.0"
DESCRIPTION = "Add join table hr_employee - pm_project: i project can have many employee, one employee can be in many projects"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="api", description=DESCRIPTION
    )

    manager.add_table(
        "HrEmployeeToPmProject", tablename="hr_employee_to_pm_project"
    )

    manager.add_column(
        table_class_name="HrEmployeeToPmProject",
        tablename="hr_employee_to_pm_project",
        column_name="hr_employee_to_pm_project_id",
        db_column_name="hr_employee_to_pm_project_id",
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
        table_class_name="HrEmployeeToPmProject",
        tablename="hr_employee_to_pm_project",
        column_name="project_id",
        db_column_name="project_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": PmProject,
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
        table_class_name="HrEmployeeToPmProject",
        tablename="hr_employee_to_pm_project",
        column_name="emp_id",
        db_column_name="emp_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": HrEmployee,
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
        table_class_name="HrEmployeeToPmProject",
        tablename="hr_employee_to_pm_project",
        column_name="project_role_id",
        db_column_name="project_role_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": PmRole,
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
        table_class_name="HrEmployeeToPmProject",
        tablename="hr_employee_to_pm_project",
        column_name="loa_number",
        db_column_name="loa_number",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 150,
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
        table_class_name="HrEmployeeToPmProject",
        tablename="hr_employee_to_pm_project",
        column_name="loa_date",
        db_column_name="loa_date",
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

    manager.add_column(
        table_class_name="HrEmployeeToPmProject",
        tablename="hr_employee_to_pm_project",
        column_name="report_to_project_role_id",
        db_column_name="report_to_project_role_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": PmRole,
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
        table_class_name="HrEmployeeToPmProject",
        tablename="hr_employee_to_pm_project",
        column_name="report_to_emp_id",
        db_column_name="report_to_emp_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": HrEmployee,
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
