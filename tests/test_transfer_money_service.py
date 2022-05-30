import pytest

from service.transfer_money_service import validate_username

@pytest.mark.parametrize("test_input, expected", [
    ('*****', False), ('rainbow34', True), ('sdfsd-dsfkj', False), ('cat$', False),
    ('34243', False), ('^%*&^(*%$#john', False), ('', False), ('              asdadfgdfdasd', False),
    ('             ', False), ('fjkhdopsfhp0ashnfpodfpasifhaoipfhnsfmfjsdnfapjfaihnfiashfapifhsodhfoafdsfsfajf9udsafof', False),
    ('fd', False), ('                ', False)]
)
def test_validate_pattern_username(test_input, expected):
    assert validate_username(test_input) == expected