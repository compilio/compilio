from __future__ import unicode_literals

from django.core.management import call_command
from django.core.serializers import base, python
from django.db import migrations

fixture = 'initial_data.yaml'


# http://stackoverflow.com/a/39743581
def load_fixture(apps, schema_editor):
    # Save the old _get_model() function
    old_get_model = python._get_model

    # Define new _get_model() function here, which utilizes the apps argument to
    # get the historical version of a model. This piece of code is directly stolen
    # from django.core.serializers.python._get_model, unchanged.
    def _get_model(model_identifier):
        try:
            return apps.get_model(model_identifier)
        except (LookupError, TypeError):
            raise base.DeserializationError("Invalid model identifier: '%s'" % model_identifier)

    # Replace the _get_model() function on the module, so loaddata can utilize it.
    python._get_model = _get_model

    # Call loaddata command
    call_command('loaddata', fixture, app_label='compiler')

    # Restore old _get_model() function
    python._get_model = old_get_model


class Migration(migrations.Migration):
    dependencies = [
        ('compiler', '0011_compiler_output_files_parse_code'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
