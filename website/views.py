#the routes - where the visitor can go into
from flask import Blueprint, render_template, redirect, request, url_for, flash
from . import db
from .models import Book, Borrowed_Books, Borrower

views = Blueprint('views', __name__) #Blueprint is not an actual application - needs to be registered

@views.route('/', methods=['GET', 'POST'])
def home():
  books = Book.query.limit(4).all()

  if request.method == 'POST':
    term = request.form.get('search') #takes what the person is searching

    return redirect(url_for('views.search', searchterm=term)) #redirects them to the page to see what they searched for
  
   

  return render_template('home.html' , books=books)

@views.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')

        book = Book(title=title, author=author, isbn=isbn)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('views.books')) #redirects to the book page

    return render_template('lend.html')

@views.route('/search/<path:searchterm>')
def search(searchterm):
  term = "%{}%".format(searchterm)

  search = Book.query.filter(Book.title.like(term)) | (Book.author.like(term)) | (Book.isbn.like(term)).all()
  
  return render_template('search.html', results=search, searchterm=searchterm)


@views.route('/books')
def books():
    books = Book.query.limit(4).all() #orders the books by its title (alphabetical)
    return render_template('books.html', books=books)

@views.route('/borrow_book' ,  methods=['GET', 'POST'])
def borrow_book():
  if request.method == 'POST':
      fname = request.form.get('fname')
      lname = request.form.get('lname')
      email = request.form.get('email')
      ph_number = request.form.get('phn_num')

      borrower = Borrower(fname=fname, lname=lname, email=email, ph_number=ph_number)
      db.session.add(borrower)
      db.session.commit()

  list = db.session.query(Borrowed_Books, Book)\
    .filter(Borrowed_Books.id_borrower == borrower.id)\
    .outerjoin(Borrowed_Books, Borrowed_Books.id_book == Book.id)\
    .add_columns(Book.id, Book.title, Book.author)\
    .filter(Book.id == Borrowed_Books.id_book).all()

  return render_template('borrow_book.html', list=list)

@views.route('/delete', methods=['GET', 'POST'])
def delete():
  if request.method == 'POST':
      title = request.form.get('title')
      author = request.form.get('author')
      isbn = request.form.get('isbn')

      book = Book.query.filter_by(title = title).filter_by(author = author).filter_by(isbn = isbn).first()
      db.session.delete(book)
      db.session.commit()
      return redirect(url_for('views.books')) #redirects to the book page

  return render_template('delete.html')

@views.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):

  book = Book.query.get_or_404(book_id)
   
  if request.method == 'POST':
      title = request.form.get('title')
      author = request.form.get('author')
      isbn = request.form.get('isbn')

      book.title = title 
      book.author = author
      book.isbn = isbn

      db.session.add(book)
      db.session.commit()

  return render_template('edit.html', book=book)

# @app.route('/home')
# def search():
#     return render_template('search.html')


# @app.route('/error')
# def error():
#     return render_template('error.html')
