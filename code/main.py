import csv
import psycopg2


def create_table():
    with open("create_table.sql", "w", encoding="utf-8") as f:
        f.write(f'''
CREATE TABLE employees (
    employee_id int PRIMARY KEY,
	first_name varchar(55),
	last_name varchar(55),
	title varchar(255),
	birth_date date,
	notes varchar(855)	
);

CREATE TABLE customers (
    customer_id varchar(55) PRIMARY KEY,
	company_name varchar(255),
	contact_name varchar(255)
);

CREATE TABLE orders (
    order_id int PRIMARY KEY,
	customer_id varchar(55) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_sity varchar(255)
);
        ''')


def script():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='99493876')
    try:
        with conn:
            with conn.cursor() as cur:
                with open('employees_data.csv') as f:
                    reader = csv.reader(f)
                    count = -1
                    for s in reader:
                        count += 1
                        if count == 0:
                            continue
                        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                    (count, s[0], s[1], s[2], s[3], s[4]))

                with open('customers_data.csv') as f:
                    reader = csv.reader(f)
                    for s in reader:
                        if len(s[0]) > 5:
                            continue
                        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (s[0], s[1], s[2]))

                with open('orders_data.csv') as f:
                    reader = csv.reader(f)
                    for s in reader:
                        if s[0] == 'order_id':
                            continue
                        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (s[0], s[1], s[2], s[3], s[4]))
    finally:
        conn.close()


def main():
    # create_table()
    script()


if __name__ == '__main__':
    main()
