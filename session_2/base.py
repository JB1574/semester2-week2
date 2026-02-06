import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def main():

    db = get_connection()

    db.close()

def list_product_categories(db):
    query = '''
            SELECT category,product_id FROM 
            products
            '''
    cursor = db.execute(query)
    for category in products:
         print(f"ID: {catgegory[0]}\tName: {category[1]}")
    
def count_total_customers(db):
    query = '''
            SELECT COUNT(customer_id) AS total_customers
            FROM customers
            '''
    cursor = db.execute(query)
    for customer_id in cursor:
        Print(f"Total customers  ")

def show_orders_per_customer(db):
    choice = -1
    while(choice < 1 ):
        choice = input("Enter customer email: ")
    try:
        choice = input(choice)
    except:
        choice =-1

    query = '''
            SELECT orders.order_id FROM
            orders
            JOIN customers ON orders.customer_id = customers .customer_id
            '''
        cursor =db.execute(query,(choice,))
def displa
if __name__=="__main__":
    main()
