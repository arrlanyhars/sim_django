from datetime import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse

from student_django.response import Response
from student_django.jwt import JWTAuth
from student_django.middleware import jwtRequired
from users import transformer
from users.models import Users


from django.contrib.auth.hashers import make_password # library membuat password

from django.contrib.auth.hashers import check_password # library check password

@jwtRequired # listener
def get_semua_user(request):
    if request.method == 'GET':
        user = Users.objects.filter(u_deleted_at=None,
                                    u_deleted_by=None).all()
        user = transformer.transform(user)
        return Response.ok(values=user)
    else:
        return Response.badRequest(message="Metode tidak ditemukan")

@jwtRequired
def get_user_by_id(request, id):
    if request.method == 'GET':
        user = Users.objects.filter(u_id=id).first()

        if not user: #jika user tidak ditemukan (variabel user adalah None)
            return Response.badRequest(message="Pengguna tidak ditemukan")
        
        user = transformer.singleTransform(user)
        return Response.ok(values=user)
    
# tidak membutuhkan authorization
def create_user(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        # add to database
        user = Users()
        user.u_fullname = json_data['fullname']
        user.u_nickname = json_data['nickname']
        user.u_email = json_data['email']
        user.u_whatsapp_number = json_data['whatsapp_number']
        user.u_created_at = datetime.now()
        user.u_created_by = json_data['email']

        # hash password
        user.u_password = make_password(json_data['password'])

        user.save() #save to database

        user = transformer.singleTransform(user)
        return Response.ok(values=user, message="User baru berhasil ditambahkan")
    
    else:
        return Response.badRequest(message="Metode tidak ditemukan")
    
@jwtRequired
def update_user(request, id):
    if request.method == 'PUT':
        json_data = json.loads(request.body)

        user = Users.objects.filter(u_id=id).first()

        if not user: #jika user tidak ditemukan (variabel user adalah None)
            return Response.badRequest(message="Pengguna tidak ditemukan")
        
        user.u_fullname = json_data["fullname"]
        user.u_nickname = json_data["nickname"]
        user.u_email = json_data["email"]
        user.u_updated_at = datetime.now()
        user.u_updated_by = json_data["email"]
        user.save() #save to database

        user = transformer.singleTransform(user)
        return Response.ok(values=user, message=f"User dengan ID {id} berhasil dilakukan update")
    
    else:
        return Response.badRequest(message="Metode tidak ditemukan")
    

def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        email = json_data['email']

        user = Users.objects.filter(u_email=email).first() # filtering

        if not user:
            return Response.badRequest(message='Password atau email salah.')

        if not check_password(json_data['password'], user.u_password):
            return Response.badRequest(message="Password atau email salah.")

        user = transformer.singleTransform(user)

        jwt = JWTAuth()
        user['token'] = jwt.encode({"id": user['id']})
        return Response.ok(values=user, message="Berhasil login")
    

@jwtRequired
def delete_user_by_id(request, id):
    if request.method == 'DELETE':
        json_data = json.loads(request.body)

        user = Users.objects.filter(u_id=id).first()

        if not user: #jika user tidak ditemukan (variabel user adalah None)
            return Response.badRequest(message="Pengguna tidak ditemukan")
        
        # menggunakan metode soft deleted
        user.u_deleted_at = datetime.now()
        user.u_deleted_by = json_data["email"]

        user.save() #save to database

        user = transformer.singleTransform(user)
        return Response.ok(values=user, message=f"User dengan ID {id} berhasil dihapus")
    
    else:
        return Response.badRequest(message="Metode tidak ditemukan")