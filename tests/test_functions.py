from utils.functions import operations, sort, cuts, data, count, number_card, name_card, is_none, format_card, description, to_count, sum_

#def test_operations():
    #assert operations() != None

#def test_sort():
    #assert sort() != None
    #assert sort() != []

#def test_cuts():
    #assert cuts() != None
    #assert len(cuts()) == 5

def test_data():
    assert data(0, [{"date":"2019-08-26T10:50:58.294041", "id":1}, {"date":"2019-04-04T23:20:05.206878", "id":2}]) != None

def test_count():
    assert count(0, [{"from": "Visa Classic 6831982476737658"}, {"to":"Visa Platinum 8990922113665229"}]) != None
    assert count(1, [{"from": "Visa Classic 6831982476737658"}, {"to":"Visa Platinum 8990922113665229"}]) == None

def test_number_card():
    assert number_card("Visa Classic 6831982476737658") != None
    assert str(number_card("Visa Classic 6831982476737658")) == "6831 98** **** 7658"

def test_name_card():
    assert name_card("Visa Classic 6831982476737658") != None
    assert str(name_card("Visa Classic 6831982476737658")) == "Visa Classic"

def test_is_none():
    assert is_none(0, [{"from": "Visa Classic 6831982476737658"}, {"to":"Visa Platinum 8990922113665229"}]) == True
    assert is_none(1, [{"from": "Visa Classic 6831982476737658"}, {"to": "Visa Platinum 8990922113665229"}]) == False

def test_format_card():
    assert format_card(0, [{"from": "Visa Classic 6831982476737658"}, {"to":"Visa Platinum 8990922113665229"}]) != None
    assert format_card(1, [{"from": "Visa Classic 6831982476737658"}, {"to": "Visa Platinum 8990922113665229"}]) == False

def test_description():
    assert description(0, [{"description":"Перевод с карты на карту"},{"description":"Перевод организации"}]) != None
    assert str(description(0, [{"description": "Перевод с карты на карту"}, {"description": "Перевод организации"}])) == "Перевод с карты на карту"

def test_to_count():
    assert to_count(0, [{"to":"Счет 72731966109147704472"},{"to":"Visa Platinum 8990922113665229"}]) != None
    assert str(to_count(0, [{"to": "Счет 72731966109147704472"}, {"to": "Visa Platinum 8990922113665229"}])) == "('Счет', '**7273')"

def test_sum_():
    assert sum_(0, [{"operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}}}, {"operationAmount": {"amount": "50870.71", "currency": {"name": "руб.", "code": "RUB"}}}]) != None
    assert str(sum_(0, [{"operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}}}, {"operationAmount": {"amount": "50870.71", "currency": {"name": "руб.", "code": "RUB"}}}])) == "('56883.54', 'USD')"

