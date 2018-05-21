import warnings
from django.apps import AppConfig
from django.db.backends.signals import connection_created

warning_given = False


def setrole_connection(connection, **kwargs):
    """
    Execute `SET ROLE` statement in the current connecitonself.
    Args:
        connection(obj): Instance of <tenant_schemas.postgresql_backend.base.DatabaseWrapper>
    """
    global warning_given
    role = None

    if "set_role" in connection.settings_dict:
        role = connection.settings_dict["set_role"]
    elif "SET_ROLE" in connection.settings_dict:
        role = connection.settings_dict["SET_ROLE"]

    if role:
        connection.cursor().execute("SET ROLE %s", (role,))
    else:
        if not warning_given:
            warnings.warn("""SET_ROLE value is missing in settings.DATABASE""")
            warning_given = True  # Once is enough


class DjangoPostgreSQLSetRoleApp(AppConfig):
    name = "postgresql_setrole"

    def ready(self):
        """
        Call setrole_conneciton function when connection_created action taken place.
        """
        connection_created.connect(receiver=setrole_connection)


default_app_config = 'postgresql_setrole.DjangoPostgreSQLSetRoleApp'
