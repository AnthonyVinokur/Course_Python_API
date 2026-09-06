from playwright.sync_api import APIResponse

class Users:
    def __init__(self,api_context):
        self.api_context = api_context
        self.endpoint = '/usuarios'

    def create_users(self,nome,email,password,administrator):
         return self.api_context.post(self.endpoint,data={
                                                             'nome' : nome,
                                                             'email': email,
                                                             'password': password,
                                                             'administrador': administrator
                                                         }
                                                            )


    def list_all_users(self):
        return self.api_context.get(self.endpoint)

    def list_user(self,user_id)->APIResponse:
        return self.api_context.get(f'{self.endpoint}/{user_id}')


    def delete_user(self,user_id):
        return self.api_context.delete(f'{self.endpoint}/{user_id}')

    def change_user(self,user_id,nome,email,password,administrator):
        return self.api_context.put(f'{self.endpoint}/{user_id}',
                                    data={
                                            'nome': nome,
                                            'email': email,
                                            'password': password,
                                            'administrador': administrator
                                        })

