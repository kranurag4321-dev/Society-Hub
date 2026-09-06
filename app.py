from flask import Flask, request, jsonify, render_template, g, session, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='.')
app.secret_key = 'bhsujshjshsydhkkjhjhoney9390' 

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('society.db')
        db.row_factory = sqlite3.Row 
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
        
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute("SELECT title, content FROM notices ORDER BY date_posted DESC")
    db_notices = cursor.fetchall()
    
    cursor.execute("SELECT * FROM tickets WHERE flat_number = ? ORDER BY date_created DESC", (session['user'],))
    db_tickets = cursor.fetchall()

    
    cursor.execute("SELECT * FROM visitors WHERE flat_number = ? ORDER BY timestamp DESC", (session['user'],))
    db_visitors = cursor.fetchall()
    
    return render_template('secretry.html', notices=db_notices, current_user=session['user'], tickets=db_tickets, visitors=db_visitors)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE flat_number = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        if user:
            session['user'] = user['flat_number']
            session['role'] = user['role']
            
            if user['role'] == 'secretary':
                return redirect(url_for('admin_panel'))
            elif user['role'] == 'guard':
                return redirect(url_for('guard_terminal'))
                
            return redirect(url_for('home'))
        else:
            return "<script>alert('Invalid credentials!'); window.location.href='/login';</script>"
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('login'))

@app.route('/guard')
def guard_terminal():
    if 'role' not in session or session['role'] != 'guard':
        return "<script>alert('RESTRICTED: Guard clearance required.'); window.location.href='/';</script>"
    return render_template('guard.html')

@app.route('/log_visitor', methods=['POST'])
def log_visitor():
    if 'role' not in session or session['role'] != 'guard':
        return redirect(url_for('login'))
        
    visitor = request.form['visitor_name']
    flat = request.form['flat_number']
    status = request.form['status']
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO visitors (visitor_name, flat_number, status) VALUES (?, ?, ?)", (visitor, flat, status))
    db.commit()
    
    return f"<script>alert('Visitor {status}: {visitor}'); window.location.href='/guard';</script>"


@app.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    if 'user' not in session: return redirect(url_for('login'))
    db = get_db(); cursor = db.cursor()
    cursor.execute("INSERT INTO tickets (flat_number, issue_type, description) VALUES (?, ?, ?)", (session['user'], request.form['issue_type'], request.form['description']))
    db.commit()
    return "<script>alert('Ticket logged!'); window.location.href='/';</script>"

@app.route('/resolve_ticket', methods=['POST'])
def resolve_ticket():
    if 'role' not in session or session['role'] != 'secretary': return redirect(url_for('login'))
    db = get_db(); cursor = db.cursor()
    cursor.execute("UPDATE tickets SET status = 'Resolved' WHERE id = ?", (request.form['ticket_id'],))
    db.commit()
    return "<script>alert('Ticket Resolved!'); window.location.href='/admin';</script>"

@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if 'role' not in session or session['role'] != 'secretary': return redirect(url_for('login'))
    db = get_db(); cursor = db.cursor()
    if request.method == 'POST':
        cursor.execute("INSERT INTO notices (title, content) VALUES (?, ?)", (request.form['title'], request.form['content']))
        db.commit()
        return "<script>alert('Notice posted!'); window.location.href='/admin';</script>"
    cursor.execute("SELECT * FROM tickets ORDER BY date_created DESC")
    return render_template('admin.html', tickets=cursor.fetchall())

@app.route('/api/alert', methods=['POST'])
def handle_alert():
    try:
        data = request.get_json(force=True) 
        print(f"\n*** EMERGENCY: {data.get('type')} at {session.get('user')} ***\n")
        return jsonify({"status": "success", "message": "Security notified."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)