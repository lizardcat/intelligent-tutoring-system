# tests/unit/test_utils.py
# import unittest
# import sys
# import os

# # Add the parent directory of 'app' to the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\Users\Admin\Downloads\IntelligentTutoringSystem\intelligent-tutoring-system  ')))
   

# from app.utils import add_numbers

# class TestUtils(unittest.TestCase):
#     def test_add_numbers(self):
#         self.assertEqual(add_numbers(2, 3), 5)
#         self.assertEqual(add_numbers(-1, 1), 0)
#         self.assertEqual(add_numbers(0, 0), 0)

# if __name__ == '__main__':
#     unittest.main()

# tests/unit/test_utils.py
# tests/unit/test_utils.py
# import unittest
# import os
# import sys

# # Add project root to Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# from intelligent_tutoring_system.utils import add_numbers

# class TestUtils(unittest.TestCase):
#     def test_add_numbers(self):
#         self.assertEqual(add_numbers(2, 3), 5)
        
# if __name__ == '__main__':
#     unittest.main()

# tests/unit/test_utils.py
# tests/unit/test_utils.py
# import unittest
# import os
# import sys

# # Add project root to Python path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# from intelligent_tutoring_system.utils import add_numbers

# class TestUtils(unittest.TestCase):
#     def test_add_numbers(self):
#         self.assertEqual(add_numbers(2, 3), 5)
        
# if __name__ == '__main__':
#     unittest.main()


import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from intelligent_tutoring_system.utils import add_numbers

class TestUtils(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

if __name__ == '__main__':
    unittest.main()