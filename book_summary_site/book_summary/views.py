from django.shortcuts import render


def post_list(request):
    return render(request,'book_summary/post_list.html',{})

def book_list(request):
    return render(request,'book_summary/book_list.html',{})

def book_detail(request):
    return render(request,'book_summary/book_detail.html',{})