import time
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright

from page_objects.users import Users

test_email = "1212sdftestemail@google.com"
test_password = "Password123"


# created the api_context for the tests
@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(base_url="https://serverest.dev")
        print(f"First time output at {datetime.now().strftime(":%S.%f")}")

        yield request_context
        print(f"API context created in conftest.py file at {datetime.now().strftime(":%S.%f")}")
        print(f"second time output at {datetime.now().strftime(":%S.%f")}")
       #print(f"API context created in conftest.py file at {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}")

        request_context.dispose()


# checking for the existine user
@pytest.fixture(scope="session")
def token(api_context):
    response_user = api_context.get('/usuarios')

    user = response_user.json()['usuarios']

    if any(u['email'] == test_email for u in user):
        print("User exists")
    else:
        print("User does not exists. Create the user!")
        # unique_email = f"user_{uuid.uuid4()}@example.com"
    # created the record
    response_create = api_context.post(
        url="/usuarios",
        data={
            "nome": "Anthony First",
            "email": test_email,
            "password": test_password,
            "administrador": "true"
        }
    )

    print("\n")
    print("You can login now")

    response_login = api_context.post('/login',
                                      data={
                                          "email": test_email,
                                          "password": test_password
                                      }

                                      )

    assert response_login.status == 200

    token_str = response_login.json()['authorization']

    print(f"This is a token: -> {token_str}")
    print(response_login.json())

    return token_str

@pytest.fixture
def user_service(api_context):
    return Users(api_context)
