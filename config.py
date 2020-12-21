import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.urandom(32)

    BLOB_ACCOUNT = 'famcmsprojectacct'
    BLOB_STORAGE_KEY = 'H691cktzrUl+rUGhPsxaw5ZhSu2VEY6ExigzqIOAa8X6XUVIeHXpdul6kc4KV5+4Q9Uv0Yky+2YyuIDyns5REA=='
    BLOB_CONTAINER = 'famcmsprojectstrgctnr'

    SQL_SERVER = 'fam-cms-project-sql-svr.database.windows.net'
    SQL_DATABASE = 'fam-cms-project-sql-db'
    SQL_USER_NAME = 'famroot'
    SQL_PASSWORD = 'Nyamurongi2'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "6hab8_qN_M711PUK3n4QwZytq7B.ayQc-r"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    #CLIENT_ID = "26b5a89b-d8e7-4726-a850-9ad4b6c66d4d"

    CLIENT_ID = "ffd772a9-3b40-45f1-ac97-7b0e23b7a94e"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
