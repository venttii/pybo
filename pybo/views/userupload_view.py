from ..models import Board, HitCount
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from ..forms import BoardForm

import logging
logger = logging.getLogger('pybo')

def index(request):
    """
    유저업로드 목록 출력
    """
    
    logger.info('유저업로드')

    board_list = Board.objects.order_by('-create_date')

    paginator = Paginator(board_list, 10) # 15개씩 보여주기
    board_list = paginator.get_page(1)

    print(board_list)
    
    context = { 'board_list': board_list}
    return render(request, 'pybo/userupload.html', context)

def detail(request, userupload_id):
    """
    유저업로드 상세 페이지 출력
    """

    # 접속자 IP 식별 Start
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # 접속자 IP 식별 End

    
    try:
        # ip주소와 게시글 번호로 기록을 조회함
        board = Board.objects.get(pk=userupload_id)
        hits = HitCount.objects.get(ip=ip, post=board)
    except Exception as e:
        print(e)
        hits = HitCount(ip=ip, post=board)
        Board.objects.filter(pk=board.id).update(view_count=board.view_count + 1)
        hits.date = timezone.now()
        hits.save()
    else:
        if not hits.date == timezone.now().date():
            Board.objects.filter(id=board.id).update(view_count=board.view_count + 1)
            hits.date = timezone.now()
            hits.save()
        # 날짜가 같은 경우
        else:
            print(str(ip) + ' has already hit this post.\n\n')

    logger.info('유저업로드 상세페이지')
    board = get_object_or_404(Board, pk=userupload_id)
    logger.info(board)
    context = {'board': board}
    return render(request, 'pybo/userupload_detail.html', context)

@login_required(login_url='common:login')
def userupload_create(request):
    """
    유저업로드 등록
    """

    # 접속자 IP 식별 Start
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # 접속자 IP 식별 End

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.create_date = timezone.now()
            board.ip = ip
            board.save()
            return redirect('pybo:userupload')
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'pybo/board_form.html', context)