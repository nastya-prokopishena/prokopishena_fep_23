from fastapi import FastAPI, Request, HTTPException
from schemas.BankInfo import BankInfo
from schemas.BankCustomer import BankCustomer, PersonalInfo
from schemas.Credit_Cart import GoldenCreditCard, CorporateCreditCard
from cryptography.fernet import Fernet

app = FastAPI()

encryption_key = Fernet.generate_key()

golden_card = GoldenCreditCard(
    client="Прокопішена Анастасія",
    account_number="91028374651923213",
    credit_limit=10000.0,
    grace_period=40,
    cvv="111",
    encryption_key=encryption_key
)

corporate_card = CorporateCreditCard(
    client="Швалінська Валерія",
    account_number="56473892015518436",
    credit_limit=3000.0,
    grace_period=25,
    cvv="444",
    encryption_key=encryption_key
)

golden_card_details = golden_card.give_details()
corporate_card_details = corporate_card.give_details()

bank_info = BankInfo(
    bank_name="Bank",
    holder_name="Прокопішена Анастасія",
    accounts_number=["91028374651923213", "56473892015518436"],
    credit_history={
        'golden_card': {
            'account_number': golden_card_details['account_number'],
            'credit_limit': golden_card_details['credit_limit'],
            'grace_period': golden_card_details['grace_period'],
        },
        'corporate_card': {
            'account_number': corporate_card_details['account_number'],
            'credit_limit': corporate_card_details['credit_limit'],
            'grace_period': corporate_card_details['grace_period'],
        },
    }
)

personal_info = PersonalInfo()

bank_customer = BankCustomer(
    personal_info=personal_info,
    bank_details=bank_info
)


@app.post("/enhanced_credit_card")
def get_enhanced_credit_card():
    return {"enhanced_credit_card_details": golden_card.give_details()}


@app.post("/bank_customer")
def get_bank_customer():
    return {"bank_customer_details": bank_customer.give_details()}
