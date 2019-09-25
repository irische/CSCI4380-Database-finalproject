import unittest
import psycopg2
from database_f import lookupdata
from statistics import Statistics


class RestaurantDataTestCase(unittest.TestCase):
    connection_string = "host='localhost' dbname='motordb' user='motordb' password='motordb'"

    conn = psycopg2.connect(connection_string)

    def setUp(self):
        with self.conn.cursor() as cursor:
            setup_queries = open('load_data.sql', 'r').read()
            cursor.execute(setup_queries)
            self.conn.commit()

        self.service = lookupdata(self.connection_string)
        self.service = Statistics(self.connection_string)

    def tearDown(self):
        self.service = None

    def query(self, query, parameters=()):
        cursor = self.conn.cursor()
        cursor.execute(query, parameters)
        return cursor.fetchall()

    def test_connectivity(self):
        self.assertEqual(True, self.service.check_connectivity())

    def test_find_recipe(self):
        recipes = self.service.find_recipe('ham')
        self.assertEqual(len(recipes), 3)
        self.assertTrue(list(map(lambda r: r['name'], recipes)).index('Hamburger') >= 0)

        recipes = self.service.find_recipe('sandwich')
        self.assertEqual(len(recipes), 2)

        recipes = self.service.find_recipe("';DROP TABLE recipe_ingredient;COMMIT;")
        self.assertEqual(len(recipes), 0)
        self.assertEqual(22, self.query("select count(*) from recipe_ingredient")[0][0])


if __name__ == '__main__':
    unittest.main()
