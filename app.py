from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Initial list of available books
available_books = ["Python Crash Course", "Clean Code", "The Pragmatic Programmer", "Agile Estimating and Planning"]
borrowed_books = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agile Library Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; }
        h1 { color: #333; }
        .container { display: flex; gap: 20px; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); flex: 1; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 8px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; }
        input[type="text"] { width: 70%; padding: 8px; margin-right: 5px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 8px 12px; background-color: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button.borrow { background-color: #007bff; }
        button:hover { opacity: 0.9; }
        .badge { background: #e0e0e0; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; }
    </style>
</head>
<body>
    <h1>📚 Library Management System (Agile Web Edition)</h1>
    <p><em>Project Managed via Agile & GitHub Kanban Board</em></p>

    <!-- Add Book Form -->
    <div class="card" style="margin-bottom: 20px;">
        <h3>Add a New Book</h3>
        <form action="/add" method="POST">
            <input type="text" name="book_title" placeholder="Enter book title..." required>
            <button type="submit">Add Book</button>
        </form>
    </div>

    <div class="container">
        <!-- Available Books Column -->
        <div class="card">
            <h3>Available Books ({{ available_books|length }})</h3>
            <ul>
                {% for book in available_books %}
                <li>
                    <span>{{ book }}</span>
                    <form action="/borrow" method="POST" style="margin: 0;">
                        <input type="hidden" name="book_title" value="{{ book }}">
                        <button type="submit" class="borrow">Borrow</button>
                    </form>
                </li>
                {% else %}
                <li><em>No books currently available.</em></li>
                {% endfor %}
            </ul>
        </div>

        <!-- Borrowed Books Column -->
        <div class="card">
            <h3>Borrowed Books ({{ borrowed_books|length }})</h3>
            <ul>
                {% for book in borrowed_books %}
                <li>
                    <span>{{ book }}</span>
                    <form action="/return" method="POST" style="margin: 0;">
                        <input type="hidden" name="book_title" value="{{ book }}">
                        <button type="submit">Return</button>
                    </form>
                </li>
                {% else %}
                <li><em>No books borrowed yet.</em></li>
                {% endfor %}
            </ul>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, available_books=available_books, borrowed_books=borrowed_books)

@app.route('/add', methods=['POST'])
def add_book():
    book = request.form.get('book_title')
    if book and book.strip():
        available_books.append(book.strip())
    return redirect(url_for('home'))

@app.route('/borrow', methods=['POST'])
def borrow_book():
    book = request.form.get('book_title')
    if book in available_books:
        available_books.remove(book)
        borrowed_books.append(book)
    return redirect(url_for('home'))

@app.route('/return', methods=['POST'])
def return_book():
    book = request.form.get('book_title')
    if book in borrowed_books:
        borrowed_books.remove(book)
        available_books.append(book)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)