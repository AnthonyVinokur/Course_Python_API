import uuid

from helpers.validators import validator_status
from page_objects.users import Users
from helpers import  validators


def test_crud_user(api_context):
    service = Users(api_context=api_context)
    update_email = f"updated_{uuid.uuid4()}@gmail.com"
    unique_email = f"anthony_{uuid.uuid4()}@gmail.com"

    response_created = service.create_users(
        nome="Anthony crud",
        email=unique_email,
        password="password123",
        administrator="true"
    )

    print(response_created.status)
    print(response_created.json())

    #assert response_created.status == 201
    validator_status(response_created,201)

    user_id = response_created.json()['_id']

    response_read = service.list_user(user_id = user_id)

    assert response_read.status == 200


    response_update = service.change_user(user_id=user_id,
                                          nome="Anthony crud updated",
                                          email= update_email,
                                          password="password123",
                                          administrator="true"
                                          )

    #assert response_update.status == 200
    validator_status(response_update, 200)
    print(response_update.json()['message'])
    assert  response_update.json()['message'] == 'Registro alterado com sucesso'

    response_delete = service.delete_user(user_id = user_id)
    print(response_delete.json()['message'])
    validator_status(response_delete, 200)
    #assert response_delete.status == 200



