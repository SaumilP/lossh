from lossh.lossh import ls
from lossh.lossh import remote_user
from click.testing import CliRunner

cli = CliRunner()


def test_ls():
    cli.invoke(ls)


def test_remove_user():
    cli.invoke(remove_user, ["lossh0"])
