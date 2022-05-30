import pytest

from service.validate_signup_service import validate_length_first_name, validate_length_last_name, validate_length_password, validate_length_username, validate_pattern_first_name, validate_pattern_last_name, validate_pattern_password, validate_pattern_username

@pytest.mark.parametrize("test_input, expected", [
    ('*****', False), ('rainbow34', True), ('sdfsd-dsfkj', False), ('cat$', False),
    ('34243', False), ('^%*&^(*%$#john', False), ('', False), ('              asdadfgdfdasd', False),
    ('             ', False)]
)
def test_validate_pattern_username(test_input, expected):
    assert validate_pattern_username(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ('*****', False), ('rainbow34#$%', True), ('sdfsd-dsfkj', False), ('cat$', False),
    ('34243', False), ('^%*&^(*%$#john', False), ('', False), ('              asdadfgdfdasd', False),
    ('             ', False)]
)
def test_validate_pattern_password(test_input, expected):
    assert validate_pattern_password(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
    ('12', False), ('a', False), ('asdhaud', True), 
    ('                                                                                                              ', False),
    ('skdfn;jlsahfopwehrflajndfopairhbfnaiohdfawsbdaifjoafjaunwirjap[f9uqw0r8erhuiqrfklasjfajakljsdjas;dhfajf;lajfk', False),
    ('asd', False)]
)
def test_validate_length_username(test_input, expected):
    assert validate_length_username(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
    ('12', False), ('a', False), ('asdhaud', True), 
    ('                                                                                                              ', False),
    ('skdfn;jlsahfopwehrflajndfopairhbfnaiohdfawsbdaifjoafjaunwirjap[f9uqw0r8erhuiqrfklasjfajakljsdjas;dhfajf;lajfk', False),
    ('asd', False)]
)
def test_validate_length_password(test_input, expected):
    assert validate_length_password(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
    ('John', True), ('13123', False), ('23sadas', False), ('3423 asdasd', False), ('Asdwq 5342', False), ('john', False), ('Asienawed#$', False), ("$#^%&((&%", False), 
    ("        ", False), ("     John", False), ("John          ", False)]
)
def test_validate_pattern_first_name(test_input, expected):
    assert validate_pattern_first_name(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
    ('Smith', True), ('13123', False), ('23sadas', False), ('3423 asdasd', False), ('Asdwq 5342', False), ('smith', False), ('Asienawed#$', False), ("$#^%&((&%", False),
    ("        ", False), ("     Smith", False), ("Smith          ", False)]
)
def test_validate_pattern_last_name(test_input, expected):
    assert validate_pattern_last_name(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
    ('ad', False), ('Karen', True), ('a', False), ('wer', False), ("akjdiaerwndaoisdyaednhaioafansoifaslfhasfhaofhasfhaosdasdahsoidfhaofhafoahfoafhaovknsxlfyharfuaiyai", False),
    ("                                                                                       sahfjsdkfhiusyfiahnrfouaihuaerhruaifaiw", False),
    ("skdfnasjfaoiufraodadnasouidc aouhafajfhaa                         aiofaonoawfnaa      ", False)]
)
def test_validate_length_first_name(test_input, expected):
    assert validate_length_first_name(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [
('ad', False), ('Care', True), ('a', False), ('wer', False), ("akjdiaerwndaoisdyaednhaioafansoifaslfhasfhaofhasfhaosdasdahsoidfhaofhafoahfoafhaovknsxlfyharfuaiyai", False),
("                                                                                       sahfjsdkfhiusyfiahnrfouaihuaerhruaifaiw", False),
("skdfnasjfaoiufraodadnasouidc aouhafajfhaa                         aiofaonoawfnaa      ", False)]
)
def test_validate_length_last_name(test_input, expected):
    assert validate_length_last_name(test_input) == expected