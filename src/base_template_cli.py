#!python

import click
from di_manager import DIManager
import version_getter

context_settings = {'help_option_names': ['-h', '--help']}


@click.command(context_settings=context_settings)
@click.version_option(version=version_getter.VersionGetter.get_version(),
                      prog_name='Base Template CLI')
@click.option('-d', '--dst', default='.', help='Destination repo root path.')
@click.argument('base_template_root_path')
def apply(dst, base_template_root_path):
    """Apply Base Template boilerplates to the destination repo."""
    di_manager = DIManager(dst, base_template_root_path)
    applyer = di_manager.getInstance('Applyer')
    applyer.apply()


if __name__ == '__main__':
    apply()
