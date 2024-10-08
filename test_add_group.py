# -*- coding: utf-8 -*-
import pytest
from group import Group
from new_application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="fqwefaef", header="faewf", footer="faf"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
