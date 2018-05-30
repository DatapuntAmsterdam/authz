import sys
import click
import psycopg2
from .users import Users

@click.group()
@click.option('--debug', is_flag=True)
@click.option('--psql-host', default='localhost', type=str, envvar='DB_HOST')
@click.option('--psql-port', default=5432, type=int, envvar='DB_PORT')
@click.option('--psql-db', default='authz', type=str, envvar='DB_DATABASE')
@click.option('--psql-user', default='authuser', type=str, envvar='DB_USER')
@click.option('--psql-password', default='authpassword', type=str, prompt=True, hide_input=True, envvar='DB_PASS')
@click.pass_context
def cli(ctx, debug, psql_host, psql_port, psql_db, psql_user, psql_password):
    try:
        users = Users(
            host=psql_host,
            port=psql_port,
            dbname=psql_db,
            user=psql_user,
            password=psql_password
        )
    except psycopg2.OperationalError as e:
        print("ERROR: Could not connect to the database")
        if debug:
            raise
        sys.exit(1)
    # create the tables if they don't exist
    users.create()
    ctx.users = users


@cli.command()
@click.argument('user', type=str)
@click.argument('password', type=str)
@click.pass_context
def add(ctx, user, password):
    users = ctx.parent.users
    try:
        users.add(user, password)
    except KeyError:
        print("ERROR: User already exists")
        sys.exit(1)


@cli.command()
@click.argument('user', type=str)
@click.argument('password', type=str)
@click.pass_context
def set(ctx, user, password):
    users = ctx.parent.users
    try:
        users.set(user, password)
    except KeyError:
        print(crayons.red("User doesn't exist"))
        sys.exit(1)


@cli.command()
@click.argument('user', type=str)
@click.argument('password', type=str)
@click.pass_context
def remove(ctx, user):
    users = ctx.parent.users
    try:
        users.remove(user)
    except KeyError:
        print("User doesn't exist")
        sys.exit(1)


if __name__ == '__main__':
    cli()
