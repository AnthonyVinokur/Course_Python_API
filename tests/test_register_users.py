import json

import pytest

from pathlib import Path

from helpers.validators import validator_status
import uuid

saves_email = f"user_{uuid.uuid4()}@test.com"


def read_json_users():
    project_root = Path(__file__).resolve().parents[1]

    file_path = (
        project_root
        / "data"
        / "test_file_users"
        / "user.json"
    )

    with file_path.open(encoding="utf-8") as file:
        data = json.load(file)

    return data["usuarios"]


@pytest.mark.parametrize("datas",read_json_users())
def test_register_users(user_service,datas):
    response = user_service.create_users(
                nome=datas['nome'],
                email=saves_email,
                password=datas['password'],
                administrator=datas['administrator'])

    validator_status(response, datas['status_expected'])

