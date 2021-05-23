import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def error_400(request, exception):
    logger.error("Error 400: [%s]" % exception)
    return render(request, 'error.html', {
        'error_code': 400,
        'error_text': 'A sua requisição possui alguma coisa errada!',
    }, status=400)


def error_401(request, exception):
    logger.error("Error 401: [%s]" % exception)
    return render(request, 'error.html', {
        'error_code': 401,
        'error_text': 'Você não possui autorização para acessar essa página!',
    }, status=401)


def error_403(request, exception):
    logger.error("Error 403: [%s]" % exception)
    return render(request, 'error.html', {
        'error_code': 403,
        'error_text': 'Você não possui autorização para acessar essa página!',
    }, status=403)


def error_404(request, exception):
    logger.error("Error 404: [%s]" % exception)
    return render(request, 'error.html', {
        'error_code': 404,
        'error_text': 'Página não foi encontrada!',
    }, status=404)


def error_500(request):
    return render(request, 'error.html', {
        'error_code': 500,
        'error_text': 'Aconteceu um erro interno no servidor!',
    }, status=500)


def error_503(request):
    return render(request, 'error.html', {
        'error_code': 503,
        'error_text': 'Nosso serviço não está disponível no momento!',
    }, status=503)