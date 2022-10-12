from gregorian_calendar import GregorianCalendar
import unittest


class TestFiveWeekends(unittest.TestCase):
    def test_oct_2010_contains_5_fridays_5_saturdays_and_5_sundays(self):
        """
        A weekend is defined as a friday, a saturday, and a sunday.
        """
        cal = GregorianCalendar()
        self.assertEqual(5, cal.count_weekends(year=2010, month=10))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
