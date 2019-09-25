import psycopg2

class lookupdata:

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)


    def find_victim(self, victim_id):
        cursor = self.conn.cursor()
        cursor.execute("select * from victim where lower(case_IID) like %s;", [victim_id])
        c = cursor.fetchall()
        if len(c) == 0:
            return None
        return [c[0][2], c[0][3], c[0][4], c[0][5]]

    def find_injury(self, case_iid):
        cursor = self.conn.cursor()
        cursor.execute("select * from injury where lower(case_IID) like %s;", [case_iid])
        c = cursor.fetchall()
        if len(c) == 0:
            return None
        return [c[0][1], c[0][2], c[0][3], c[0][4]]

    def find_vehicle(self, case_vid):
        cursor = self.conn.cursor()
        cursor.execute("select * from vehicle where lower(case_VID) like %s;", [case_vid])
        c = cursor.fetchall()
        if len(c) == 0:
            return None
        return [c[0][1], c[0][2], c[0][3], c[0][4], c[0][5], c[0][6], c[0][7]]

    def find_event(self, case_vid):
        cursor = self.conn.cursor()
        cursor.execute("select * from event where lower(case_VID) like %s;", [case_vid])
        c = cursor.fetchall()
        if len(c) == 0:
            return None
        return [c[0][1], c[0][2], c[0][3], c[0][4], c[0][5], c[0][6], c[0][7]]



