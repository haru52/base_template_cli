#!python

import click

from di_manager import DIManager

import version_getter

context_settings = {'help_option_names': ['-h', '--help']}
dirs_help = "Target directories to copy (e.g., .husky, \
.github/ISSUE_TEMPLATE). If you don't specify this option, this command \
copies all files of Base Template to the destination repo."


@click.command(context_settings=context_settings)
@click.version_option(version=version_getter.VersionGetter.get_version(),
                      prog_name='Base Template CLI')
@click.option('-d', '--dst', default='.', help='Destination repo root path.')
@click.option('--dirs', multiple=True, help=dirs_help)
@click.argument('base_template_root_path')
def apply(dst, dirs, base_template_root_path):
    """Apply (Copy) Base Template boilerplates to the destination repo."""
    di_manager = DIManager(dst, base_template_root_path, dirs)
    applyer = di_manager.getInstance('Applyer')
    applyer.apply()


if __name__ == '__main__':
    apply()
