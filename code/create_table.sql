
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
        