import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    print(f'Testing with number: {number}')
    assert number > 0, "Number should not be zero"

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9), (-1, 1)])
def test_several_numbers(number: int, expected: int):
    print(f'Testing with number: {number}, expected: {expected}')
    assert number ** 2 == expected, "Square of the number should match the expected value"

@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'safari'])
@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0, "The length of the string should be greater than 0"

@pytest.fixture(params=['chromium', 'firefox', 'safari'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser):
    print(f'Opening browser: {browser}')
    assert browser in ['chromium', 'firefox', 'safari'], "Browser should be one of the specified options"

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # @pytest.mark.parametrize("user", ["Alice", "Zara"])
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"User with operations: {user}")

    # @pytest.mark.parametrize("user", ["Alice", "Zara"])
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

# @pytest.mark.parametrize(
#     "phone_number",
#     ["+1234567890", "+0987654321", "+1122334455"],
#     ids=[
#         "User has money on the bank account",
#         "User has no money on the bank account",
#         "User has a credit limit on the bank account"
#     ]
# )
# def test_identifier(phone_number: str):
#     pass

users = {
    "+1234567890": "User has money on the bank account",
    "+0987654321": "User has no money on the bank account",
    "+1122334455": "User has a credit limit on the bank account"
}

# def format_phone_number(phone_number: str) -> str:
#     return f'{phone_number}: {users[phone_number]}'

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    # ids=format_phone_number # method above
    ids = lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifier(phone_number: str):
    pass

