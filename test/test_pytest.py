import pytest
from src.bank_account import BankAccount

@pytest.mark.parametrize("ammount, expected",[
     (100,1100),
     (3000,4000),
     (4500,5500),
])
def test_deposit_multiple_ammounts(ammount,expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(ammount)
    assert(new_balance== expected)


def test_sum():
    a=2
    b=6
    assert a + b== 8

@pytest.mark.parametrize(
    "initial_balance, deposit_amount, expected_result, expect_exception",
    [
        (1000, -100, None, ValueError),     # Negative deposit - should raise ValueError
        (500, 200, 700, None),              # Positive deposit - should succeed
        (0, 0, 0, None),                    # Zero deposit - no change
    ]
)
def test_deposit_parametrized(initial_balance, deposit_amount, expected_result, expect_exception):
    account = BankAccount(balance=initial_balance, log_file=None)  # disable logging for testing
    if expect_exception:
        with pytest.raises(expect_exception):
            account.deposit(deposit_amount)
    else:
        result = account.deposit(deposit_amount)
        assert result == expected_result