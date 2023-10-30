from django.shortcuts import render

def home(request):
    return render(request, 'homeapp/home.html')

def about(request):
    context = {
        'title': "Tom's Site",
        'content': "I'm Tom and this is my site."
    }
    return render(request, 'homeapp/about.html', context)

def faq(request):
    faq_data = [
        {
            'question': "What's your name?",
            'answer': "Tom.",
        },
        {
            'question': "Where do you live?",
            'answer': "San Francisco.",
        },
        # Add more questions and answers as needed
    ]

    context = {
        'faq_data': faq_data,
    }

    return render(request, 'homeapp/faq.html', context)

def contact(request):
    contact_methods = {
        'email': 'tom@hotmail.com',
        'discord': 'tomdiscord',
        'telegram': 'tomtelegram',
        # Add more contact methods as needed
    }

    context = {
        'contact_methods': contact_methods,
    }

    return render(request, 'homeapp/contact.html', context)

