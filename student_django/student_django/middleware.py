from functools import wraps
from django.http import JsonResponse
from student_django.jwt import JWTAuth



def jwtRequired(fn):
    @wraps(fn)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return JsonResponse({'message': 'Anda belum login'}, status=401)
        
        try:
            token = auth_header.split(' ')[1]
            decode(token)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=401)
        
        return fn(request, *args, **kwargs)

    return wrapper

def decode(token):
    return JWTAuth().decode(token)