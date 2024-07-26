import sqlite3

def search_database(search_string):
    conn = sqlite3.connect('assignment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, marks FROM students WHERE name LIKE ?", ('%' + search_string + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def main():
    while True:
        search_string = input("Enter a search string: ").strip()
        if not search_string:
            print("Please enter a search string")
            continue
        results = search_database(search_string)
        if not results:
            print("No matching records found.")
        else:
            total_marks = 0
            for name, marks in results:
                print(f"Name: {name}, Marks: {marks}")
                total_marks += marks
            average_marks = total_marks / len(results) if results else 0
            print(f"Total Marks: {total_marks}")
            print(f"Average Marks: {average_marks:.2f}")
        break

if __name__ == "__main__":
    main()