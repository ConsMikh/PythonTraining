# pylint: disable = no-member
'''
These two classes are actually pretty short, considering what they're doing: connecting to a
database, executing a query, formatting the results, and outputting them. The superclass
takes care of the repetitive work, but lets us easily specify those steps that vary between
tasks. Further, we can also easily change steps that are provided in the base class. 
'''

import sqlite3
class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect("sales.db")
    def construct_query(self):
        raise NotImplementedError()
    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()
    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)
    def output_results(self):
        raise NotImplementedError()


import datetime
class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
        self.query = "select * from Sales where new='true'"
    def output_results(self):
        print(self.formatted_results)


class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = (
            "select salesperson, sum(amt) "
            + " from Sales group by salesperson"
        )
    def output_results(self):
        filename = "gross_sales_{0}".format(
            datetime.date.today().strftime("%Y%m%d")
        )
        with open(filename, "w") as outfile:
            outfile.write(self.formatted_results)
