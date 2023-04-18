from piccolo.table import Table
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod
from piccolo.columns.column_types import Timestamp

class Organization(Table, tablename="organization"):
    organization_id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )
    name = Varchar(
        length=100,
        default="",
        null=False,
        primary_key=False,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )
    tagline = Varchar(
        length=250,
        default="",
        null=True,
        primary_key=False,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )
    website = Varchar(
        length=100,
        default="",
        null=True,
        primary_key=False,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )
    email = Varchar(
        length=30,
        default="",
        null=True,
        primary_key=False,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )

class Migration(Table, tablename="migration"):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=True,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )
    name = Varchar(
        length=200,
        default="",
        null=False,
        primary_key=False,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )
    app_name = Varchar(
        length=200,
        default="",
        null=False,
        primary_key=False,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )
    ran_on = Timestamp(
        default=TimestampNow(),
        null=False,
        primary_key=False,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        db_column_name=None,
        secret=False,
    )

