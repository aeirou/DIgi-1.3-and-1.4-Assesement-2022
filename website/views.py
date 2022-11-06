#the routes - where the visitor can go into
from flask import Blueprint, render_template, redirect, request, url_for, flash
from sqlalchemy import desc
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
        dop = request.form.get('dop')
        isbn = request.form.get('isbn')
        desc = request.form.get('desc')

        book = Book(title=title, author=author,dop=dop,isbn=isbn, desc=desc)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('views.books')) #redirects to the book page

    return render_template('lend.html')

@views.route('/search/<path:searchterm>')
def search(searchterm):
  term = "%{}%".format(searchterm)

  search = Book.query.filter((Book.id.like(term)) | (Book.title.like(term)) | (Book.author.like(term)) | (Book.dop.like(term)) |(Book.isbn.like(term))).all()
  
  return render_template('search.html', results=search, searchterm=searchterm)

@views.route('/books')
def books():
    books = Book.query.limit(4).all() #orders the books by its title (alphabetical)
    return render_template('books.html', books=books)

@views.route('/borrow_book/<path:booktitle>' ,  methods=['GET', 'POST'])
def borrow_book(booktitle):
  title = "%{}%".format(booktitle)

  if request.method == 'POST':
      fname = request.form.get('fname')
      lname = request.form.get('lname')
      email = request.form.get('email')
      ph_number = request.form.get('phn_num')

      borrower = Borrower(fname=fname, lname=lname, email=email, ph_number=ph_number)
      db.session.add(borrower)
      db.session.commit()

  # list = db.session.query(Borrowed_Books, Book)\
  #   .filter(Borrowed_Books.id_borrower == borrower.id)\
  #   .outerjoin(Borrowed_Books, Borrowed_Books.id_book == Book.id)\
  #   .add_columns(Book.id, Book.title, Book.author)\
  #   .filter(Book.id == Borrowed_Books.id_book).all()

  return render_template('borrow_book.html', title=title)

@views.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete(book_id):
  book = Book.query.get_or_404(book_id)

  if request.method == 'POST':
      book = Book.query.filter_by(id=Book.id).first()
      db.session.delete(book)
      db.session.commit()

      # if len(id) == 0:
      #   if len(title) > 150:
      #     flash('Title exceeds character limit!', category='error')
      #   elif len(title) < 2:
      #     flash('Title must be greater than 2 characters!', category='error')
      #   elif len(author) < 3:
      #     flash('Author must be greater than 3 characters!', category='error')
      #   elif len(author) > 256:
      #     flash('Author exceeds character limit!', category='error')
      #   elif title == book.title and author == book.author:
      #     flash('Please edit to continue!', category='error')


      return redirect(url_for('views.books')) #redirects to the book page

  return render_template('delete.html')

@views.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):

  book = Book.query.get_or_404(book_id)
   
  if request.method == 'POST':
      title = request.form.get('title')
      author = request.form.get('author')
      dop = request.form.get('dop')
      isbn = request.form.get('isbn')
      desc = request.form.get('desc')

      book.title = title 
      book.author = author
      book.dop = dop
      book.isbn = isbn
      book.desc = desc

      db.session.add(book)
      db.session.commit()
      return redirect(url_for('views.books')) #redirects to the book page

  return render_template('edit.html', book=book)
 
# @app.route('/error')
# def error():
#     return render_template('error.html')
