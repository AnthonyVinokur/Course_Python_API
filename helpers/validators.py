

def validator_status(response, status_expected):
    assert response.status == status_expected, f"Status expected : {status_expected}, but Status received -> {response.status}"

