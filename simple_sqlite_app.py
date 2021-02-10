import sqlite3

# defines variable for database
db = 'chainsaw_juggler_records_db.sqlite'

# creates connection to db file
def create_database():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS jugglingRecords (juggler_name TEXT UNIQUE, country TEXT, catches INT)')
    conn.close()

# add starting data
def add_starting_data():
    insert_starting_data = 'INSERT INTO jugglingRecords VALUES (?, ?, ?)'
    with sqlite3.connect(db) as conn:
        conn.execute(insert_starting_data, ("Janne Mustonen", "Finland", 98) )
        conn.execute(insert_starting_data, ("Ian Stewart", "Canada", 94) )
        conn.execute(insert_starting_data, ("Aaron Gregg", "Canada", 88) )
        conn.execute(insert_starting_data, ("Chad Taylor", "USA", 78) )
    conn.close()


# user can add a row
def add_new_row():
    print('--Add new row--')
    insert_new_user_data = 'INSERT INTO jugglingRecords VALUES (?, ?, ?)'
    # user provides info
    new_name = input('Enter record holder\'s name: ')
    new_country = input('Enter record holder\'s country: ')
    new_catches = int(input('Enter number of catches (integer only): '))
    with sqlite3.connect(db) as conn:
        # enters info user has provided
        conn.execute(insert_new_user_data, (new_name, new_country, new_catches))
    conn.close()
# user can search for record holder by name
def search_for_record():
    print('--Search for records by name--')
    juggler_name = input('Enter name to search for record: ')
    get_record_by_name = 'SELECT * FROM jugglingRecords WHERE juggler_name = ?'
    with sqlite3.connect(db) as conn:
        results = conn.execute(get_record_by_name, (juggler_name, ))
        first_row = results.fetchone()
        print(first_row)
    conn.close()
# update the number of catches for a record holder
def update_record():
    print('--Update number of catches--')
    update_number_catches = 'UPDATE jugglingRecords SET catches = ? WHERE juggler_name = ?'
    juggler_name_to_modify = input('Enter name of juggler: ')
    updated_catches = int(input('Enter new number of catches (as an integer: '))
    with sqlite3.connect(db) as conn:
        conn.execute(update_number_catches, (updated_catches, juggler_name_to_modify))
    conn.close
# delete a record by name
def delete_record():
    print('--delete record--')
    juggler_name_delete = input('Enter name of record holder for deletion: ')
    delete_one_entry = 'DELETE FROM jugglingRecords WHERE juggler_name = ?'
    with sqlite3.connect(db) as conn:
        conn.execute(delete_one_entry, (juggler_name_delete, ))
    conn.close()

def print_all_records():
    with sqlite3.connect(db) as conn:
        results = conn.execute('SELECT * FROM jugglingRecords')
        for row in results:
            print(row)

# create_database()

add_starting_data()
print_all_records()
add_new_row()
print_all_records()
search_for_record()
print_all_records()
update_record()
print_all_records()
delete_record()
print_all_records()