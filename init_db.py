
import sqlite3

def init_db():
    conn = sqlite3.connect('camp.db')
    c = conn.cursor()

    # Create tables if not exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS classrooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            type TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS facilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            type TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS offices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS staff_rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')

    # Clear previous data for clean re-run
    c.execute('DELETE FROM classrooms')
    c.execute('DELETE FROM facilities')
    c.execute('DELETE FROM offices')
    c.execute('DELETE FROM staff_rooms')

    # Data (shortened sample - you can expand or reuse your original lists)
    classrooms = [
        ('LT 201', 'FIRST FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 202', 'FIRST FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 301', 'SECOND FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 302', 'SECOND FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 401', 'THIRD FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 402', 'THIRD FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 501', 'FOURTH FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 502', 'FOURTH FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 601', 'FIFTH FLOOR FRONT WING', 'LECTURE HALL'),
        ('LT 602', 'FIFTH FLOOR FRONT WING', 'LECTURE HALL'),

        ('CR 101', 'GROUND FLOOR BACK WING', 'CLASSROOM'),
        ('CR 102', 'GROUND FLOOR BACK WING', 'CLASSROOM'),
        ('CR 103', 'GROUND FLOOR BACK WING', 'CLASSROOM'),
        ('CR 104', 'GROUND FLOOR BACK WING', 'CLASSROOM'),
        ('CR 105', 'GROUND FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 201', 'FIRST FLOOR BACK WING', 'CLASSROOM'),
        ('CR 202', 'FIRST FLOOR BACK WING', 'CLASSROOM'),
        ('CR 203', 'FIRST FLOOR BACK WING', 'CLASSROOM'),
        ('CR 204', 'FIRST FLOOR BACK WING', 'CLASSROOM'),
        ('CR 205', 'FIRST FLOOR BACK WING', 'CLASSROOM'),
        ('CR 206', 'FIRST FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 207', 'FIRST FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 301', 'SECOND FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 302', 'SECOND FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 303', 'SECOND FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 304', 'SECOND FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 305', 'SECOND FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 401', 'THIRD FLOOR BACK WING', 'CLASSROOM'),
        ('CR 402', 'THIRD FLOOR BACK WING', 'CLASSROOM'),
        ('CR 403', 'THIRD FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 404', 'THIRD FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 405', 'THIRD FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 406', 'THIRD FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 501', 'FOURTH FLOOR BACK WING', 'CLASSROOM'),
        ('CR 502', 'FOURTH FLOOR BACK WING', 'CLASSROOM'),
        ('CR 503', 'FOURTH FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 504', 'FOURTH FLOOR FRONT WING', 'CLASSROOM'),
        ('CR 601', 'FIFTH FLOOR BACK WING', 'CLASSROOM'),
        ('CR 602', 'FIFTH FLOOR BACK WING', 'CLASSROOM'),
        ('CR 603', 'FIFTH FLOOR BACK WING', 'CLASSROOM'),
        ('CR 604', 'FIFTH FLOOR BACK WING', 'CLASSROOM'),
        ('CR 605', 'FIFTH FLOOR BACK WING', 'CLASSROOM'),
        ('CR 606', 'FIFTH FLOOR FRONT WING', 'CLASSROOM'),
        ('LAB 1', 'GROUND FLOOR BACK WING', 'LAB'),
        ('LAB 2', 'FIRST FLOOR BACK WING', 'LAB'),
        ('LAB 3', 'SECOND FLOOR BACK WING', 'LAB'),
        ('LAB 4', 'THIRD FLOOR BACK WING', 'LAB'),
        ('LAB 5', 'FOURTH FLOOR BACK WING', 'LAB'),
        ('LAB 6', 'FIFTH FLOOR BACK WING', 'LAB'),
        ('LAB 7', 'THIRD FLOOR BACK WING', 'LAB'),
        ('LAB 8', 'SECOND FLOOR BACK WING', 'LAB'),
        ('LAB 9', 'FIRST FLOOR BACK WING', 'LAB'),
        ('LAB 10', 'GROUND FLOOR BACK WING', 'LAB'),
        ('UBUNTU LAB', 'GROUND FLOOR FRONT WING', 'LAB'),
        ('TCL 1', 'FIRST FLOOR FRONT WING', 'LAB'),
        ('TCL 2', 'SECOND FLOOR FRONT WING', 'LAB'),
        ('MICROPROCESSOR LAB', 'THIRD FLOOR BACK WING', 'LAB'),
        ('LOGIC LAB', 'BASEMENT', 'LAB'),
        ('ELECTRONICS LAB', 'THIRD FLOOR BACK WING', 'LAB'),
        ('ELECTRICAL LAB', 'THIRD FLOOR BACK WING', 'LAB'),
        ('CHEMISTRY LAB', 'FOURTH FLOOR BACK WING', 'LAB'),
        ('PHYSICS LAB', 'FOURTH FLOOR BACK WING', 'LAB'),
        ('IAPT LAB', 'FOURTH FLOOR BACK WING', 'LAB'),
        ('WORKSHOP', 'BASEMENT', 'LAB'),
        ('MECHANICAL LAB', 'BASEMENT', 'LAB'),
        ('FASHION DESIGNING LAB', 'BASEMENT', 'LAB'),
        ('MANUAL DRAWING LAB', 'BASEMENT', 'LAB'),
        ('CIVIL LAB', 'BASEMENT', 'LAB'),
        ('BOSCH LAB', 'GROUND FLOOR FRONT WING', 'LAB'),
        ('VENUE 2', 'GROUND FLOOR FRONT WING', 'LAB'),
        ('PHARMACEUTICAL CHEMISTRY-1 LAB', 'SECOND FLOOR BACK WING', 'LAB'),
        ('PHARMACEUTICAL CHEMISTRY-2 LAB', 'GROUND FLOOR BACK WING', 'LAB'),
        ('PHARMACEUTICS-1 LAB', 'SECOND FLOOR BACK WING', 'LAB'),
        ('PHARMACEUTICS-2 LAB', 'SECOND FLOOR BACK WING', 'LAB'),
        ('PHARMACOLOGY-1 LAB', 'SECOND FLOOR BACK WING', 'LAB'),
        ('PHARMACOGNOSY-1 LAB', 'SECOND FLOOR BACK WING', 'LAB'),
        ('MAC LAB-2', 'THIRD FLOOR FRONT WING', 'LAB'),
        ('MAC LAB-1', 'GROUND FLOOR FRONT WING', 'LAB'),
        ('FINE ARTS LAB', 'SECOND FLOOR FRONT WING', 'LAB'),
        ('VISUAL ARTS LAB', 'SECOND FLOOR FRONT WING', 'LAB'),
        ('GC LAB-1', 'FOURTH FLOOR FRONT WING', 'LAB'),
        ('GC LAB-2', 'FOURTH FLOOR FRONT WING', 'LAB'),
        ('MOOT COURT', 'FIFTH FLOOR BACK WING', 'COURT'),
        ('NEW AUDI', 'FIFTH FLOOR FRONT WING', 'AUDITORIUM'),
        ('KP NAUTIYAL', 'FIFTH FLOOR FRONT WING', 'AUDITORIUM'),
    ]

    facilities = [
        ('LIBRARY', 'GROUND FLOOR FRONT WING', 'library'),
        ('MAIN LIBRARY', 'FIRST FLOOR FRONT WING', 'library'),
        ('TUCK SHOP', 'NEAR GATE NO.1', 'shop'),
        ('CAFETERIA', 'BASEMENT', 'cafeteria'),
        ('SPORTS ARENA', 'NEAR GATE NO.2', 'sports'),
        ('FEES CELL', 'BASEMENT', 'administrative'),
        ('EXAM CELL', 'BASEMENT', 'administrative'),
        ('PLACEMENT DEPARTMENT', 'GROUND FLOOR FRONT WING', 'administrative'),
        ('RESEARCH AND DEVELOPMENT CELL', 'GROUND FLOOR FRONT WING', 'administrative'),
        ('MI ROOM', 'GROUND FLOOR FRONT WING', 'healthcare'),
        ('SERVER ROOM', 'FIRST FLOOR FRONT WING', 'technical'),
        ('STUDENTS COUNSELLOR', 'SECOND FLOOR FRONT WING', 'counselling'),
        ('ERP CELL', 'GROUND FLOOR FRONT WING', 'administrative'),
        ('ADMISSION CELL', 'GROUND FLOOR FRONT WING', 'administrative'),
        ('MEETING HALL', 'GROUND FLOOR FRONT WING', 'hall'),
        ('SEMINAR HALL', 'GROUND FLOOR FRONT WING', 'hall'),
        ('PARKING', 'BASEMENT', 'parking'),
    ]

    offices = [
        ('PRESIDENT OFFICE', 'SECOND FLOOR FRONT WING'),
        ('VICE CHANCELLOR OFFICE', 'SECOND FLOOR FRONT WING'),
        ('REGISTRAR OFFICE', 'GROUND FLOOR FRONT WING'),
        ('HOD OFFICE PDP DEPARTMENT', 'THIRD FLOOR FRONT WING'),
        ('HOD OFFICE CSE DEPARTMENT', 'THIRD FLOOR FRONT WING'),
        ('HOD OFFICE FASHION DESIGNING DEPARTMENT', 'THIRD FLOOR FRONT WING'),
        ('HOD OFFICE DEPARTMENT OF HUMANITIES', 'FIRST FLOOR FRONT WING'),
        ('HOD OFFICE DEPARTMENT OF SCHOOL AND MANAGEMENT', 'SECOND FLOOR BACK WING'),
    ]

    staff_rooms = [
        ('NEW HALL STAFF ROOM', 'SECOND FLOOR FRONT WING'),
        ('MASS MEDIA AND COMMUNICATION STAFF ROOM', 'SECOND FLOOR FRONT WING'),
        ('SCHOOL OF PHARMACY STAFF ROOM', 'SECOND FLOOR FRONT WING'),
        ('SCHOOL OF COMPUTING STAFF ROOM', 'THIRD FLOOR FRONT WING'),
        ('COMPUTER SCIENCE AND ENGINEERING STAFF ROOM', 'THIRD FLOOR FRONT WING'),
        ('PDP STAFF ROOM', 'FIFTH FLOOR FRONT WING'),
        ('SCHOOL OF LAW STAFF ROOM', 'FIFTH FLOOR FRONT WING'),
        ('MECHANICAL DEPARTMENT STAFF ROOM', 'FIFTH FLOOR FRONT WING'),
    ]

    c.executemany('INSERT INTO classrooms (name, address, type) VALUES (?, ?, ?)', classrooms)
    c.executemany('INSERT INTO facilities (name, location, type) VALUES (?, ?, ?)', facilities)
    c.executemany('INSERT INTO offices (name, location) VALUES (?, ?)', offices)
    c.executemany('INSERT INTO staff_rooms (name, location) VALUES (?, ?)', staff_rooms)

    conn.commit()
    conn.close()

    print('Database initialized.')

if __name__ == "__main__":
    init_db()