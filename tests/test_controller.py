import pytest

from src.controller import Controller


@pytest.fixture()
def controller():
    return Controller()


def test_controller_init(controller):
    # Arrange
    player = controller.player
    dealer = controller.dealer

    # Act
    controller.init_game()

    # Assert
    assert len(player.hand) == 0
    assert len(dealer.hand) == 0

    deck = dealer.deck

    controller.init_game()

    assert dealer.deck != deck
