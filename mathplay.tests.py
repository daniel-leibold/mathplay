import unittest
from mathplay import User, play

def input(**arg):
    print("mock input")
    return "1"

class TestSum(unittest.TestCase):
    def test_user(self):
        u = User("User_name", 13, "m")
        assert u.name == "User_name"

    @unittest.skip
    def test_play(self):
        mock_user = User("mock",12,"m")
        play(mock_user)

if __name__ == "__main__":
    unittest.main()