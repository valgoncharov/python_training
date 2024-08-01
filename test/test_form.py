# -*- coding: utf-8 -*-
from model.location import Location

    
def test_form(app):
    app.session.open_home_page(base_url="https://demoqa.com/forms")
    app.session.choose_form_page()
    app.session.go_to_text_box_page(text_box_url="https://demoqa.com/text-box")
    app.choose_item()
    app.group.set_username(username="Ujy")
    app.group.set_email(email="val@gmail.com")
    app.group.set_address(Location(address="fsaa", address_str="acsd"))
    app.submit_the_form()


def test_form_next(app):
    app.session.open_home_page(base_url="")
    app.session.choose_form_page()
    app.session.go_to_text_box_page(text_box_url="")
    app.choose_item()
    app.group.set_username(username="")
    app.group.set_email(email="")
    app.group.set_address(Location(address="", address_str=""))
    app.submit_the_form()
