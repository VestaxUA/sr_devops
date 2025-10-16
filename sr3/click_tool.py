import click

@click.group()
def cli():
    """Проста CLI-утиліта на Click."""
    pass

@cli.command()
@click.option('--name', required=True, help='Вкажіть ім’я користувача.')
def say(name):
    """Виводить ім’я, якщо воно не починається на p/P."""
    if name.lower().startswith('p'):
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)

if __name__ == '__main__':
    cli()