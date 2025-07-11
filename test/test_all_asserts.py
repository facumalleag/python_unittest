import unittest

SERVER = "server a"
API = "Running"


class AllAssertTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Facu", "Facu")

    def test_assert_true_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("No soy un numero")

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(3, [2, 4, 5, 10])

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            user,
            {"first_name": "Luis", "last_name": "Martinez"}
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )

    @unittest.skip(
        "trabajo en progreso, sera habilitada nuevamente")  # permite modificar el comportamiento de una misma funcion
    def test_skip(self):
        self.assertEqual("hola", "chau")

    @unittest.skipIf(SERVER == "server a",
                     "no estamos en el sertvidor correcto")  # permite modificar el comportamiento de una misma funcion
    def test_skip_if(self):
        self.assertEqual("1", "1")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual("13", "1")

    @unittest.skipUnless(
        API == "Not Running", "La API no esta corriendo"
    )
    def test_skip_unless(self):
        self.assertEqual("1", "1")
