import unittest
from app import create_app
from app.routes.users import users_bp

app = create_app('development')
app.register_blueprint(users_bp, name='users_test')


class TestUsersAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.client = app.test_client()

    def test_get_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        # Verificar se a resposta contém uma lista de usuários
        data = response.get_json()
        self.assertIn('users', data)
        self.assertIsInstance(data['users'], list)

    def test_create_user(self):
        user_data = {
            'name': 'John Doe',
            'password': '123456',
            'email': 'john@example.com'
        }
        response = self.client.post('/users', json=user_data)
        if response.status_code == 201:
            # Verificar se a mensagem de resposta é correta
            data = response.get_json()
            self.assertIn('message', data)
            self.assertEqual(data['message'], 'User created successfully')
        elif response.status_code == 409:
            # Verificar se a mensagem de resposta é correta para o caso de usuário já existente
            data = response.get_json()
            self.assertIn('message', data)
            self.assertEqual(data['message'], 'User already exists')
        else:
            self.fail(f"Unexpected status code: {response.status_code}")

    def test_get_user(self):
        user_id = 1
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        # Verificar se a resposta contém os detalhes do usuário correto
        data = response.get_json()
        self.assertEqual(data['id'], user_id)
        self.assertEqual(data['name'], 'John Doe')

    def test_get_nonexistent_user(self):
        user_id = 999
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 404)
        # Verificar se a mensagem de resposta é correta
        data = response.get_json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'User not found')


if __name__ == '__main__':
    unittest.main()
