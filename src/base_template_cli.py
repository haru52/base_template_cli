#!python

import click
from applyer import Applyer
from di_manager import DIManager

@click.command()
@click.argument('destination_path')
@click.argument('base_template_path')
def apply(destination_path, base_template_path):
    """Apply Base Template boilerplates to the destination directory."""
    di_manager = DIManager(destination_path, base_template_path)
    applyer = di_manager.getInstance('Applyer')
    applyer.apply()


if __name__ == '__main__':
    apply()
