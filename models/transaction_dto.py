class Transaction:
    def __init__(self, transaction_id, user_id, transaction_name, transaction_amount, transaction_debit_credit, transaction_location):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.transaction_name = transaction_name
        self.transaction_amount = transaction_amount
        self.transaction_debit_credit = transaction_debit_credit
        self.transaction_location = transaction_location

    def __repr__(self) -> str:
        return f"{self.transaction_id} - {self.user_id} - {self.transaction_name} - {self.transaction_amount} - {self.transaction_debit_credit} - {self.transaction_location}"
        