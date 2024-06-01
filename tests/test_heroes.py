"""
    Notes: This file will be used to test heroes.py
    To initialize hero you need:
    
    * asset_name: a string that contains the name of the image file. Note that
    the file must be located in the assets folder inside the project
    (Rougue-Shmup-X)
"""

from entities import heroes
from entities import attack
import pytest


test_img = "test img.png"


def test_generate_image_xy_coordenate():
    test_hero = heroes.Hero(asset_name=test_img, x=10, y=20)
    assert isinstance(test_hero.rect.x, int)
    assert isinstance(test_hero.rect.y, int)
    assert test_hero.rect.centerx == 10
    assert test_hero.rect.centery == 20

    test_hero = heroes.Hero(asset_name=test_img, x=100.5, y=200.5)
    assert isinstance(test_hero.rect.x, int)
    assert isinstance(test_hero.rect.y, int)
    assert test_hero.rect.centerx == 101
    assert test_hero.rect.centery == 201

    # the boundaries of x and y should be handled by the controller
    # as the HERO should know or care of the size of the play area



def test_generate_image_makes_valid__import_image__sprite__rect():
    test_hero = heroes.Hero(asset_name=test_img)
    assert test_hero.import_image is not None
    assert test_hero.sprite is not None
    assert test_hero.rect is not None



def test_helper_is_within_bounds():
    # This looks like a dumb way to go about it but I lack the knowledge
    # to make this look better
    test_hero = heroes.Hero(asset_name=test_img)
    with pytest.raises(
        ValueError,
        match="Error: Value width out of bounds 16 is MIN expected, 1 given.",
    ):
        test_hero._is_within_bounds(16, 128, 1, "width")

    with pytest.raises(
        ValueError,
        match="Error: Value width out of bounds 128 is MAX expected, 200 given.",
    ):
        test_hero._is_within_bounds(16, 128, 200, "width")


def test_movement_functions():
    test_hero = heroes.Hero(asset_name=test_img, x=100, y=100, movement_speed=10)
    # initial position
    assert test_hero.rect.centerx == 100
    assert test_hero.rect.centery == 100
    
    test_hero.move_forward()
    assert test_hero.rect.centerx == 100
    assert test_hero.rect.centery == 90
    
    test_hero.move_back()
    assert test_hero.rect.centerx == 100
    assert test_hero.rect.centery == 100

    test_hero.move_right()
    assert test_hero.rect.centerx == 110
    assert test_hero.rect.centery == 100
    
    test_hero.move_left()
    assert test_hero.rect.centerx == 100
    assert test_hero.rect.centery == 100



# test_shot() is difficult as Hero.shoot() depends on the game running for
# time to change and thus determine if a shot can be made...
# I don't know how to handle this at the moment
# TODO: find a way to test this more completely
def test_shoot():
    test_hero = heroes.Hero(asset_name=test_img)
    assert test_hero.shoot() is None



def test_take_damage():
    test_hero = heroes.Hero(asset_name=test_img, health=50)
    assert test_hero.current_health == 50
    assert test_hero.total_health == 50

    test_hero.take_damage(10)
    assert test_hero.current_health == 40
    assert test_hero.total_health == 50

    with pytest.raises(
        ValueError,
        match="Error: Value player damage out of bounds 1 is MIN expected, -10 given.",
    ):
        test_hero.take_damage(-10)
    
    with pytest.raises(
        ValueError,
        match="Error: Value player damage out of bounds 9999 is MAX expected, 10000 given.",
    ):
        test_hero.take_damage(10000)