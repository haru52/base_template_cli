#!python

import click

from di_manager import DIManager

import version_getter


context_settings = {'help_option_names': ['-h', '--help']}
target_dirs_help = "Target directories to copy (e.g., .husky, \
.github/ISSUE_TEMPLATE). If you don't specify this option, this command \
copies all files of Base Template to the destination repo. If you want to \
copy only root files, use --only-root option."


def validate_options(target_dirs, only_root):
    if len(target_dirs) > 0 and only_root:
        raise click.BadParameter(
            '--target-dirs and --only-root options cannot be used together.')


@click.command(context_settings=context_settings)
@click.version_option(version=version_getter.VersionGetter.get_version(),
                      prog_name='Base Template CLI')
@click.option('-d', '--dst', default='.', help='Destination repo root path.')
@click.option('-t', '--target-dirs', multiple=True, help=target_dirs_help)
@click.option('-r', '--only-root', is_flag=True,
              help='Copy only root directory files of Base Template repo.')
@click.argument('base_template_root_path')
def apply(dst, target_dirs, only_root, base_template_root_path):
    """Apply (Copy) Base Template boilerplates to the destination repo."""
    validate_options(target_dirs, only_root)

    di_manager = DIManager(
        dst,
        base_template_root_path,
        target_dirs,
        only_root)
    applyer = di_manager.getInstance('Applyer')
    applyer.apply()


if __name__ == '__main__':
    apply()
