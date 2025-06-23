import sys
import os
import sqlite3

def menu():
    clear_screen()
    print("\nChoose Option")
    print("1. Add Data")
    print("2. Edit Data")
    print("3. Delete Data")
    print("4. Search Data")
    print("5. Show All Data")
    print("Q. Quit")
    print(" ")
    option = input("Enter option ").lower().strip()

    if option not in ('1', '2', '3', '4', '5', 'q'):
        print("Choose a correct option.")
        press_key()
    else:
        match option:
            case "1":
                add_data_query()
            case "2":
                edit_data()
            case "3":
                delete_data()
            case "4":
                search_data()
            case "5":
                show_all_data()
            case "q":
                print("Closing program now")
                sys.exit()

def press_key():
    input("Press Enter to continue... ")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_data_query():
    clear_screen()
    print("Enter data\n")
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone: ")
    mail = input("Email: ")
    street = input("Street: ")
    street_no = input("Street number: ")
    code = input("Postcode: ")
    city = input("City: ")
    notes = input("Notes: ")

    database_add_data(name, surname, phone, mail, street, street_no, code, city, notes)
    press_key()

def database_add_data(name, surname, phone, mail, street, street_no, code, city, notes):
    with sqlite3.connect('kontakty.db') as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO kontakty (imie, nazwisko, telefon, email, ulica, numer, kod, miasto, uwagi)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, surname, phone, mail, street, street_no, code, city, notes))
        conn.commit()

def search_data():
    clear_screen()
    print("Search data - fill in known fields or leave blank\n")

    imie = input("Name: ").strip()
    nazwisko = input("Surname: ").strip()
    telefon = input("Phone: ").strip()
    email = input("Email: ").strip()
    ulica = input("Street: ").strip()
    numer = input("Street number: ").strip()
    kod = input("Postcode: ").strip()
    miasto = input("City: ").strip()
    uwagi = input("Notes: ").strip()

    conditions = []
    params = []

    if imie:
        conditions.append("imie LIKE ?")
        params.append(f"%{imie}%")
    if nazwisko:
        conditions.append("nazwisko LIKE ?")
        params.append(f"%{nazwisko}%")
    if telefon:
        conditions.append("telefon LIKE ?")
        params.append(f"%{telefon}%")
    if email:
        conditions.append("email LIKE ?")
        params.append(f"%{email}%")
    if ulica:
        conditions.append("ulica LIKE ?")
        params.append(f"%{ulica}%")
    if numer:
        conditions.append("numer LIKE ?")
        params.append(f"%{numer}%")
    if kod:
        conditions.append("kod LIKE ?")
        params.append(f"%{kod}%")
    if miasto:
        conditions.append("miasto LIKE ?")
        params.append(f"%{miasto}%")
    if uwagi:
        conditions.append("uwagi LIKE ?")
        params.append(f"%{uwagi}%")

    query = "SELECT * FROM kontakty"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    with sqlite3.connect('kontakty.db') as conn:
        cur = conn.cursor()
        cur.execute(query, params)
        results = cur.fetchall()

    clear_screen()
    if results:
        print(f"Found {len(results)} result(s):\n")
        for row in results:
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Surname: {row[2]}")
            print(f"Phone: {row[3]}")
            print(f"Email: {row[4]}")
            print(f"Street: {row[5]}")
            print(f"Street No.: {row[6]}")
            print(f"Postcode: {row[7]}")
            print(f"City: {row[8]}")
            print(f"Notes: {row[9]}")
            print("-" * 40)
    else:
        print("No results found.")

    press_key()

def show_all_data():
    clear_screen()
    with sqlite3.connect('kontakty.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM kontakty")
        results = cur.fetchall()

    if results:
        print(f"All contacts ({len(results)}):\n")
        for row in results:
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Surname: {row[2]}")
            print(f"Phone: {row[3]}")
            print(f"Email: {row[4]}")
            print(f"Street: {row[5]}")
            print(f"Street No.: {row[6]}")
            print(f"Postcode: {row[7]}")
            print(f"City: {row[8]}")
            print(f"Notes: {row[9]}")
            print("-" * 40)
    else:
        print("No contacts in database.")
    press_key()

def delete_data():
    clear_screen()
    print("Delete data - fill in known fields or leave blank\n")

    imie = input("Name: ").strip()
    nazwisko = input("Surname: ").strip()
    telefon = input("Phone: ").strip()
    email = input("Email: ").strip()
    ulica = input("Street: ").strip()
    numer = input("Street number: ").strip()
    kod = input("Postcode: ").strip()
    miasto = input("City: ").strip()
    uwagi = input("Notes: ").strip()

    conditions = []
    params = []

    if imie:
        conditions.append("imie LIKE ?")
        params.append(f"%{imie}%")
    if nazwisko:
        conditions.append("nazwisko LIKE ?")
        params.append(f"%{nazwisko}%")
    if telefon:
        conditions.append("telefon LIKE ?")
        params.append(f"%{telefon}%")
    if email:
        conditions.append("email LIKE ?")
        params.append(f"%{email}%")
    if ulica:
        conditions.append("ulica LIKE ?")
        params.append(f"%{ulica}%")
    if numer:
        conditions.append("numer LIKE ?")
        params.append(f"%{numer}%")
    if kod:
        conditions.append("kod LIKE ?")
        params.append(f"%{kod}%")
    if miasto:
        conditions.append("miasto LIKE ?")
        params.append(f"%{miasto}%")
    if uwagi:
        conditions.append("uwagi LIKE ?")
        params.append(f"%{uwagi}%")

    query = "SELECT * FROM kontakty"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    with sqlite3.connect('kontakty.db') as conn:
        cur = conn.cursor()
        cur.execute(query, params)
        results = cur.fetchall()

    clear_screen()
    if results:
        print(f"Found {len(results)} result(s):\n")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}")

        to_delete = input('Which ID would you like to delete? (Enter "A" to delete all above): ').strip()

        with sqlite3.connect('kontakty.db') as conn:
            cur = conn.cursor()
            if to_delete.lower() == 'a':
                ids_to_delete = [row[0] for row in results]
                cur.execute(f"DELETE FROM kontakty WHERE id IN ({','.join('?'*len(ids_to_delete))})", ids_to_delete)
                print(f"{len(ids_to_delete)} records deleted.")
            else:
                try:
                    id_to_delete = int(to_delete)
                    cur.execute("DELETE FROM kontakty WHERE id = ?", (id_to_delete,))
                    if cur.rowcount > 0:
                        print(f"Record with ID {id_to_delete} deleted.")
                    else:
                        print("No record found with that ID.")
                except ValueError:
                    print("Invalid ID entered.")
            conn.commit()
    else:
        print("No results found.")

    press_key()

def edit_data():
    clear_screen()
    print("Edit data - search for record to edit\n")

    imie = input("Name: ").strip()
    nazwisko = input("Surname: ").strip()
    telefon = input("Phone: ").strip()
    email = input("Email: ").strip()
    ulica = input("Street: ").strip()
    numer = input("Street number: ").strip()
    kod = input("Postcode: ").strip()
    miasto = input("City: ").strip()
    uwagi = input("Notes: ").strip()

    conditions = []
    params = []

    if imie:
        conditions.append("imie LIKE ?")
        params.append(f"%{imie}%")
    if nazwisko:
        conditions.append("nazwisko LIKE ?")
        params.append(f"%{nazwisko}%")
    if telefon:
        conditions.append("telefon LIKE ?")
        params.append(f"%{telefon}%")
    if email:
        conditions.append("email LIKE ?")
        params.append(f"%{email}%")
    if ulica:
        conditions.append("ulica LIKE ?")
        params.append(f"%{ulica}%")
    if numer:
        conditions.append("numer LIKE ?")
        params.append(f"%{numer}%")
    if kod:
        conditions.append("kod LIKE ?")
        params.append(f"%{kod}%")
    if miasto:
        conditions.append("miasto LIKE ?")
        params.append(f"%{miasto}%")
    if uwagi:
        conditions.append("uwagi LIKE ?")
        params.append(f"%{uwagi}%")

    query = "SELECT * FROM kontakty"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    with sqlite3.connect('kontakty.db') as conn:
        cur = conn.cursor()
        cur.execute(query, params)
        results = cur.fetchall()

    clear_screen()
    if results:
        print(f"Found {len(results)} result(s):\n")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}")

        to_edit = input('Which ID would you like to edit? ').strip()
        try:
            id_to_edit = int(to_edit)
        except ValueError:
            print("Invalid ID entered.")
            press_key()
            return

        # Pobierz aktualne dane wybranego rekordu
        cur.execute("SELECT * FROM kontakty WHERE id = ?", (id_to_edit,))
        record = cur.fetchone()
        if not record:
            print("No record found with that ID.")
            press_key()
            return

        print("\nLeave field empty to keep current value.\n")
        name = input(f"Name [{record[1]}]: ").strip() or record[1]
        surname = input(f"Surname [{record[2]}]: ").strip() or record[2]
        phone = input(f"Phone [{record[3]}]: ").strip() or record[3]
        mail = input(f"Email [{record[4]}]: ").strip() or record[4]
        street = input(f"Street [{record[5]}]: ").strip() or record[5]
        street_no = input(f"Street number [{record[6]}]: ").strip() or record[6]
        code = input(f"Postcode [{record[7]}]: ").strip() or record[7]
        city = input(f"City [{record[8]}]: ").strip() or record[8]
        notes = input(f"Notes [{record[9]}]: ").strip() or record[9]

        cur.execute('''
            UPDATE kontakty SET
                imie = ?,
                nazwisko = ?,
                telefon = ?,
                email = ?,
                ulica = ?,
                numer = ?,
                kod = ?,
                miasto = ?,
                uwagi = ?
            WHERE id = ?
        ''', (name, surname, phone, mail, street, street_no, code, city, notes, id_to_edit))
        conn.commit()

        print("Record updated.")
    else:
        print("No results found.")

    press_key()

if __name__ == "__main__":
    from init_db import init_db
    init_db()
    while True:
        menu()
