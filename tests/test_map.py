import contextlib

import psycopg2
import pytest

from src.dpuser import users


class Cursor(contextlib.AbstractContextManager):
    """ Mock of psycopg2.Cursor
    """
    def __exit__(self, *args, **kwargs):
        return None

    def execute(self, *args, **kwargs):
        pass


class Connection(contextlib.AbstractContextManager):
    """ Mock of psycopg2.Connection
    """
    def __exit__(self, *args, **kwargs):
        return None

    def cursor(self):
        return Cursor()

    def close(self):
        self.closed = True


@pytest.fixture(autouse=True)
def dbconn(monkeypatch):
    """ Patch psycopg2's internal ``_connect``, so we can borrow as much
    argument validation of ``connect`` as possible.
    """
    # after this patch, connect should return an instance of the above
    monkeypatch.setattr(
        psycopg2, '_connect', lambda *args, **kwargs: Connection()
    )


@pytest.fixture(scope='function')
def dbconnection():
    return users._DBConnection(
        dbname='test', user='test', password='test', host='test'
    )


@pytest.fixture(scope='function')
def dbconnection_bad_cursor():
    dbconnection = users._DBConnection(
        dbname='test', user='test', password='test', host='test'
    )

    class BadCursor():
        def execute(self, query):
            raise psycopg2.DatabaseError()

    dbconnection._conn.cursor = lambda: BadCursor()
    return dbconnection


def test_dbconnection__is_usable(dbconnection, dbconnection_bad_cursor):
    assert dbconnection._is_usable() is True
    assert dbconnection_bad_cursor._is_usable() is False


def test_dbconnection__connection(dbconnection):
    # test disfunctional connection
    with pytest.raises(psycopg2.DatabaseError):
        dbconnection._is_usable = lambda *args: False
        with dbconnection._connection() as conn:
            assert conn is dbconnection._conn
            raise psycopg2.DatabaseError()
        assert dbconnection._conn is None
        assert getattr(dbconnection, 'closed')
    # test reconnect
    with dbconnection._connection() as conn:
        assert conn is dbconnection._conn


def test_dbconnection_transaction_cursor(dbconnection):
    with dbconnection.transaction_cursor() as cur:
        assert isinstance(cur, Cursor)


def test_dbconnection_cursor(dbconnection):
    with dbconnection.cursor() as cur:
        assert isinstance(cur, Cursor)
