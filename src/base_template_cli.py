import click
from applyer import Applyer

@click.command()
@click.argument('destination_path')
@click.argument('base_template_path')
def apply(destination_path, base_template_path):
    """Apply Base Template boilerplates to the destination directory."""
    applyer = Applyer(destination_path, base_template_path)
    applyer.apply()


if __name__ == '__main__':
    apply()
