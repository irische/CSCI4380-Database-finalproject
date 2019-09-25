import psycopg2


class Statistics:
    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    def check_connectivity(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM victim LIMIT 1")
        records = cursor.fetchall()
        return len(records) == 1

    def count_safety_equipment(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT safety_equip,COUNT(safety_equip) FROM event\
                       GROUP BY safety_equip ORDER BY COUNT(safety_equip) DESC")
        c = cursor.fetchall()
        return c

    def count_make_top10(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT vehicle_make,COUNT(vehicle_make) FROM vehicle \
            GROUP BY vehicle_make ORDER BY COUNT(vehicle_make) DESC LIMIT 10")
        c = cursor.fetchall()
        return c

    def count_vehicle_year_top10(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT vehicle_year,COUNT(vehicle_year) FROM vehicle\
             GROUP BY vehicle_year ORDER BY COUNT(vehicle_year) DESC LIMIT 10")
        c = cursor.fetchall()
        return c

    def count_victim_age(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT sum(case when age >=10 and age <20 then 1 else 0 end) as range1,\
            sum(case when age >=20 and age <30 then 1 else 0 end) as range2,\
            sum(case when age >=30 and age <40 then 1 else 0 end) as range3,\
            sum(case when age >=40 and age <50 then 1 else 0 end) as range4,\
            sum(case when age >=50 and age <60 then 1 else 0 end) as range5,\
            sum(case when age >=60 and age <70 then 1 else 0 end) as range6,\
            sum(case when age >=70 and age <80 then 1 else 0 end) as range7,\
            sum(case when age >=80 and age <90 then 1 else 0 end) as range8,\
            sum(case when age >=90 and age <100 then 1 else 0 end) as range9 FROM victim")
        c = cursor.fetchall()
        result = []
        for i in range(9):
            string = "Age {} to {}".format((i + 1) * 10, (i + 1) * 10 + 10)
            result.append([string, c[0][i]])
        return result

    def count_action_prior(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT action_prior,COUNT(action_prior) FROM event\
             GROUP BY action_prior ORDER BY COUNT(action_prior) DESC")
        c = cursor.fetchall()
        return c


    def count_event_type(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT event_type,COUNT(event_type) FROM event\
             GROUP BY event_type ORDER BY COUNT(event_type) DESC")
        c = cursor.fetchall()
        return c
    



