# services/users/project/tests/test_users.py

import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Pruebas para el servicio de usuarios."""

    def test_users(self):
        """Asegúrese de que la ruta /ping se comporte correctamente."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
    	"""Ensure a new user can be added to the database."""
    	with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'Noluccia',
                    'email': 'luciariquelme51@gmail.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('luciariquelme51@gmail.com was added!', data['message'])
            self.assertIn('success', data['status'])

if __name__ == '__main__':
    unittest.main()
