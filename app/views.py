from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from django.contrib import messages
import requests
from app.models import *
from django.db.models import Q




def Index(request):
    data = Book.objects.all()
    return render(request, 'index.html', {'data':data})


def BookEdit(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        instance = get_object_or_404(Book, pk=book_id)
        instance.bookid = request.POST.get('bookid')
        instance.title = request.POST.get('title')
        instance.author = request.POST.get('author')
        instance.Average_Rating = request.POST.get('Average_Rating')
        instance.isbn = request.POST.get('isbn')
        instance.Isbn13 = request.POST.get('Isbn13')
        instance.Language_Code = request.POST.get('Language_Code')
        instance.Num_page = request.POST.get('Num_page')
        instance.Ratings_Count = request.POST.get('Ratings_Count')
        instance.Text_Reviews_Count = request.POST.get('Text_Reviews_Count')
        instance.Publication_Date = request.POST.get('Publication_Date')
        instance.publisher = request.POST.get('publisher')
        instance.save()
        messages.success(request, f'Book {instance.bookid} as been update successfully.')
        return redirect('index')


def BookDelete(request):
    if request.method == 'POST':
        id = request.POST.get('book_id')
        book = Book.objects.get(pk=id)
        book.delete()
        messages.success(request, f'Book {book.bookid} has been deleted.')
        return redirect('index')


def APIData(request):
    if request.method == 'POST':
        bookid = request.POST.get('bookid')
        url = "https://frappe.io/api/method/frappe-library?page=2&title=and"
        response = requests.get(url)
        json_data = response.json()
        data = json_data['message']
        for i in data:
            if i['bookID'] == bookid:
                reg = Book(
                    bookid = i['bookID'],
                    title = i['title'],
                    author = i['authors'],
                    Average_Rating = i['average_rating'],
                    isbn = i['isbn'],
                    Isbn13 = i['isbn13'],
                    Language_Code = i['language_code'],
                    Num_page = i['  num_pages'],
                    Ratings_Count = i['ratings_count'],
                    Text_Reviews_Count = i['text_reviews_count'],
                    Publication_Date = i['publication_date'],
                    publisher = i['publisher'],
                )
                reg.save()
        messages.success(request, f'Book ({bookid}) has been added successfully.')
        return redirect('apidata')
    else:
        url = "https://frappe.io/api/method/frappe-library?page=2&title=and"
        response = requests.get(url)
        json_data = response.json()
        data = json_data['message']
        return render(request, 'api_data.html', {'data':data})


def SearchBooks(request):
    query = request.GET.get('q')
    results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'index.html', {'data':results, 'query':query})



def Members(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        debt = request.POST.get('debt')
        reg = Member(name=name, email=email, debt=debt)
        reg.save()
        messages.success(request, 'Member has been registered.')
        return redirect('members')
    else:
        data = Member.objects.all()
        context = {'data':data}
        return render(request, 'member.html', context)



def Transactions(request):
    if request.method == 'POST':
        member = request.POST.get('member')
        member_id = Member.objects.get(pk=member)
        book = request.POST.get('book')
        book_id = Book.objects.get(pk=book)
        issue_date = request.POST.get('issue_date')
        return_date = request.POST.get('return_date')
        rent_fee = request.POST.get('rent_fee')
        reg = Transaction(
            member = member_id,
            book = book_id,
            issue_date = issue_date,
            return_date = return_date,
            rent_fee = rent_fee
        )
        reg.save()
        messages.success(request, 'Transactions are successfully added.')
        return redirect('transaction')
    else:
        books = Book.objects.all()
        member = Member.objects.all()
        transaction = Transaction.objects.all()
        return render(request, 'transactions.html', {'books':books, 'members':member, 'transactions':transaction})


def EditTransactions(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        member = request.POST.get('member')
        book = request.POST.get('book')
        issue_date = request.POST.get('issue_date')
        return_date = request.POST.get('return_date')
        rent_fee = request.POST.get('rent_fee')
        book_id = Book.objects.get(pk=book)
        member_id = Member.objects.get(pk=member)
        instance = get_object_or_404(Transaction, pk=id)
        instance.member = member_id
        instance.book = book_id
        instance.issue_date = issue_date
        instance.return_date = return_date
        instance.rent_fee = rent_fee
        instance.save()
        messages.success(request, 'Transaction Data has been edited.')
        return redirect('transaction')
    

def TransactionDelete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        trans = Transaction.objects.get(pk=id)
        trans.delete()
        messages.success(request, f'Data has been deleted.')
        return redirect('transaction')