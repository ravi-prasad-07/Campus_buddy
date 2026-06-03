
from flask import Flask, render_template, jsonify, request
import sqlite3
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

DB_PATH = 'camp.db'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def floor_map_for_location(loc):
    if not loc: return None
    s = loc.upper()
    # Match common floor keywords
    if 'FIRST FLOOR' in s or 'FIRST' in s:
        return '/static/images/first.jpg'
    if 'SECOND FLOOR' in s or 'SECOND' in s:
        return '/static/images/second.jpg'
    if 'THIRD FLOOR' in s or 'THIRD' in s:
        return '/static/images/third.jpg'
    if 'FOURTH FLOOR' in s or 'FOURTH' in s:
        return '/static/images/fourth.jpg'
    if 'FIFTH FLOOR' in s or 'FIFTH' in s:
        return '/static/images/fifth.jpg'
    if 'GROUND' in s:
        return '/static/images/ground.jpg'
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/classrooms")
def api_classrooms():
    try:
        conn = get_db()
        cur = conn.execute("SELECT * FROM classrooms ORDER BY type, name")
        data = [dict(row) for row in cur.fetchall()]
        for r in data:
            r['map_image'] = floor_map_for_location(r.get('address') or r.get('location'))
        conn.close()
        return jsonify(data)
    except Exception as e:
        print(f"Error in classrooms: {e}")
        return jsonify([])

@app.route("/api/facilities")
def api_facilities():
    try:
        conn = get_db()
        cur = conn.execute("SELECT * FROM facilities ORDER BY type, name")
        data = [dict(row) for row in cur.fetchall()]
        for r in data:
            r['map_image'] = floor_map_for_location(r.get('location'))
        conn.close()
        return jsonify(data)
    except Exception as e:
        print(f"Error in facilities: {e}")
        return jsonify([])

@app.route("/api/offices")
def api_offices():
    try:
        conn = get_db()
        cur = conn.execute("SELECT * FROM offices ORDER BY name")
        data = [dict(row) for row in cur.fetchall()]
        for r in data:
            r['map_image'] = floor_map_for_location(r.get('location'))
        conn.close()
        return jsonify(data)
    except Exception as e:
        print(f"Error in offices: {e}")
        return jsonify([])

@app.route("/api/staff_rooms")
def api_staffrooms():
    try:
        conn = get_db()
        cur = conn.execute("SELECT * FROM staff_rooms ORDER BY name")
        data = [dict(row) for row in cur.fetchall()]
        for r in data:
            r['map_image'] = floor_map_for_location(r.get('location'))
        conn.close()
        return jsonify(data)
    except Exception as e:
        print(f"Error in staff_rooms: {e}")
        return jsonify([])

@app.route("/api/search", methods=['POST'])
def api_search():
    try:
        q = request.json.get('query', '').strip().lower()
        conn = get_db()
        results = {
            'classrooms': [],
            'facilities': [],
            'offices': [],
            'staff_rooms': []
        }

        if q:
            # Classrooms
            cur = conn.execute(
                "SELECT * FROM classrooms WHERE LOWER(name) LIKE ? OR LOWER(address) LIKE ? OR LOWER(type) LIKE ?",
                (f'%{q}%', f'%{q}%', f'%{q}%')
            )
            rows = [dict(row) for row in cur.fetchall()]
            for r in rows:
                r['map_image'] = floor_map_for_location(r.get('address') or r.get('location'))
            results['classrooms'] = rows

            # Facilities
            cur = conn.execute(
                "SELECT * FROM facilities WHERE LOWER(name) LIKE ? OR LOWER(location) LIKE ? OR LOWER(type) LIKE ?",
                (f'%{q}%', f'%{q}%', f'%{q}%')
            )
            rows = [dict(row) for row in cur.fetchall()]
            for r in rows:
                r['map_image'] = floor_map_for_location(r.get('location'))
            results['facilities'] = rows

            # Offices
            cur = conn.execute(
                "SELECT * FROM offices WHERE LOWER(name) LIKE ? OR LOWER(location) LIKE ?",
                (f'%{q}%', f'%{q}%')
            )
            rows = [dict(row) for row in cur.fetchall()]
            for r in rows:
                r['map_image'] = floor_map_for_location(r.get('location'))
            results['offices'] = rows

            # Staff rooms
            cur = conn.execute(
                "SELECT * FROM staff_rooms WHERE LOWER(name) LIKE ? OR LOWER(location) LIKE ?",
                (f'%{q}%', f'%{q}%')
            )
            rows = [dict(row) for row in cur.fetchall()]
            for r in rows:
                r['map_image'] = floor_map_for_location(r.get('location'))
            results['staff_rooms'] = rows

        conn.close()
        return jsonify(results)
    except Exception as e:
        print(f"Error in search: {e}")
        return jsonify({'classrooms': [], 'facilities': [], 'offices': [], 'staff_rooms': []}), 500

if __name__ == "__main__":
    # If DB doesn't exist, optionally instruct user to run init_db.py
    if not os.path.exists(DB_PATH):
        print("Database not found. Run `python init_db.py` to create camp.db with sample data.")
    app.run(debug=True)
