import unittest
from unittest import mock
from unittest.mock import patch
from unittest import TestCase

from io import StringIO
from mathplay import User, greeting, play
class TestMathPlay(TestCase):
    def setUp(self) -> None:
        self.mock_user = User("Name", 5, "m")

    def test_user_ctor_and_name(self):
        u = User("User_name", 13, "m")
        assert u.name == "User_name"

    def test_greeting_should_return_user(self):
        with patch('builtins.input') as fake_in:
            fake_in.side_effect = ["User", "m", 5]
            user = greeting()
            assert user.name == "User"
            assert user.age == 5
            assert user.gender == "m"

    def test_play_cancel_should_output_schade(self):
        with patch('builtins.input') as fake_input, patch('sys.stdout', new=StringIO()) as fake_out:
            fake_input.side_effect = ["c"] # c for cancel
            play(self.mock_user)
            out = fake_out.getvalue().strip()
        assert "SCHADE, dass Du aufhören willst!" in out

    def test_play_random_3_plus_3_should_be_in_output(self):
        with patch('mathplay.randrange', return_value=3), patch('builtins.input') as fake_input, patch('sys.stdout', new=StringIO()) as fake_out:
            fake_input.side_effect = ["c"]
            play(self.mock_user)
            out = fake_out.getvalue().strip()
        assert "Runde 1: Was ist das Ergebnis aus 3 ➕ 3 ?" in out

    def test_play_random_2_plus_2_should_return_hurra(self):
        with patch('mathplay.randrange', return_value=2), patch('builtins.input') as fake_input, patch('sys.stdout', new=StringIO()) as fake_out:
            fake_input.side_effect = ["4", "c"]
            play(self.mock_user)
            out = fake_out.getvalue().strip()
        assert "Hurra!!! Das stimmt!" in out

    def test_play_bump_to_round3_should_return_runde_3(self):
        with patch('builtins.input') as fake_input, patch('sys.stdout', new=StringIO()) as fake_out:
            fake_input.side_effect = ["1","2","c"]
            play(self.mock_user)
            out = fake_out.getvalue().strip()
        assert "Runde 3" in out

    def test_play_after_5_rounds_stat_should_be_shown(self):
        with patch('builtins.input') as fake_input, patch('sys.stdout', new=StringIO()) as fake_out:
            fake_input.side_effect = ["1","2","3","4","5","c"]
            play(self.mock_user)
            out = fake_out.getvalue().strip()
        assert "Erfolgsquote" in out
        assert "Fehlerquote" in out

    def test_play_3_correct_rounds_should_show_100_percent_success(self):
        with patch('mathplay.randrange') as fake_random, patch('builtins.input') as fake_input, patch('sys.stdout', new=StringIO()) as fake_out:
            fake_random.side_effect = [1,1,2,2,3,3,1,1,1,1,1,1]
            fake_input.side_effect = ["2","4","6","2","2","c"]
            play(self.mock_user)
            out = fake_out.getvalue().strip()
        assert "Erfolgsquote 👍: 100.00%" in out
        assert "Wow... Super Erfolgsrate Name!!!" in out

if __name__ == "__main__":
    unittest.main()