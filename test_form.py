# -*- coding: utf-8 -*-
import pytest
from location import Location
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_form(app):
    app.open_home_page(base_url="https://demoqa.com/forms")
    app.choose_form_page()
    app.go_to_text_box_page(text_box_url="https://demoqa.com/text-box")
    app.choose_item()
    app.set_username(username="Ujy")
    app.set_email(email="val@gmail.com")
    app.set_address(Location(address="fsaa", address_str="acsd"))
    app.submit_the_form()


def test_form_next(app):
    app.open_home_page(base_url="")
    app.choose_form_page()
    app.go_to_text_box_page(text_box_url="")
    app.choose_item()
    app.set_username(username="")
    app.set_email(email="")
    app.set_address(Location(address="", address_str=""))
    app.submit_the_form()