import pytest
from playwright.sync_api import sync_playwright


def test_list_users(api_context):
    response = api_context.get("/usuarios")

    print(response.status)
    print(response.json())

    assert response.status == 200

    data = response.json()
    for i in data:
        print(i)
        print(data)
    assert len(data) > 0



