from django.shortcuts import render


def index(request):
    return render(request, 'utils/index.html')


def artii(request, keyword):
    import art
    result = art.text2art(keyword, 'ghost')
    # from IPython import embed; embed()
    context = {
        'result': result,
        'keyword': keyword,
    }
    return render(request, 'utils/artii.html', context)


def stock(request):
    pass  # TODO: 완성하기
