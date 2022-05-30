from decimal import Decimal
import pytest

from service.wd_service import deposit_check, validate_button_pressed, withdraw_check

fail_test_list = [
    {'moneytransac': 'withdraw', 'withdrawmoney':''},{'moneytransac': 'deposit', 'depositmoney':''}
    ]

@pytest.mark.parametrize("test_values", fail_test_list)
def test_validate_button_pressed_fails(test_values):
    assert validate_button_pressed(test_values) == False

def test_validate_button_pressed_success():
    assert validate_button_pressed({'moneytransac': 'withdraw', 'withdrawmoney':'234'}) == True

@pytest.mark.parametrize("test_money, test_curr_money, expected", [
    ('234', Decimal(5000.00), True), ('2', Decimal(9999998.00), False), ('9999999999', Decimal(4673.00), False),
    ('1', Decimal(9999999.00), False), ('9996000', Decimal(5000.00), False)]
)
def test_deposit_check(test_money, test_curr_money, expected):
    assert deposit_check(test_money, test_curr_money) == expected

@pytest.mark.parametrize("test_money, test_curr_money, expected", [
    ('234', Decimal(5000.00), True), ('2', Decimal(0.00), False), ('10000', Decimal(5667.00), False),
    ('20', Decimal(19), False), ('32453', Decimal(200.00), False)]
)
def test_withdraw_check(test_money, test_curr_money, expected):
    assert withdraw_check(test_money, test_curr_money) == expected