from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from ..forms import GuestbookForm
from ..models import Guestbook

import logging
logger = logging.getLogger('pybo')

def index(request):
    """
    guestbook 목록 출력
    """

    guestbook_list = Guestbook.objects.order_by('-create_date')

    context = {'guestbook_list': guestbook_list}

    return render(request, 'pybo/guestbook.html', context)

def guestbook_create(request):
    """
    방명록 등록
    """

    # 접속자 IP 식별 Start
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # 접속자 IP 식별 End

    ip = ip.split('.')
    ip = '.'.join([ip[0], '*', ip[2], ip[3]])
    
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            guestbook = form.save(commit=False)
            # guestbook.author = request.user
            guestbook.create_date = timezone.now()
            guestbook.ip_address = ip
            guestbook.save()
            return redirect('pybo:guestbook')
    else:
        form = GuestbookForm()
    context = {'form': form}
    return render(request, 'pybo/guestbook.html', context)