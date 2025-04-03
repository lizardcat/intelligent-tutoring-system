# # tests/integration/test_views.py
# import unittest
# import os
# import sys

# # Add project root to Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# from intelligent_tutoring_system.app import create_app

# class TestViews(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app()
#         self.client = self.app.test_client()

#     def test_home_page(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

# if __name__ == '__main__':
#     unittest.main()

# import unittest
# import os

# from intelligent_tutoring_system.app import create_app

# class TestViews(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app()
#         self.client = self.app.test_client()

#     def test_home_page(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

# if __name__ == '__main__':
#     unittest.main()



# import unittest
# from intelligent_tutoring_system.app import create_app

# class TestViews(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app()  # This should return a valid Flask app instance
#         self.client = self.app.test_client()

#     def test_home_page(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#     def setUp(self):
#         try:
#             self.app = create_app()
#         except Exception as e:
#             print("Error creating app:", e)
#             self.app = None
#         if self.app:
#             self.client = self.app.test_client()

# import unittest
# from intelligent_tutoring_system.app import create_app

# class TestViews(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app()  # This should return a valid Flask app instance
#         self.client = self.app.test_client()

#     def test_home_page(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

import unittest
from intelligent_tutoring_system.app import create_app

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app()  # This should return a valid Flask app instance
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get('/')  # Ensure this matches the route defined
        self.assertEqual(response.status_code, 200)