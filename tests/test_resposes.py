import pytest
from playwright.sync_api import sync_playwright



def test_request_response(api_context):


        response = api_context.get("/usuarios")
        assert response.status == 200

        headers  = response.headers
        print(f"the headers are {headers}")

        for key,value in headers.items():
            print(f"{key:<25} : {value}")


        body = response.json()
        assert isinstance(body['usuarios'],list)
