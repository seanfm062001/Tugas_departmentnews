import json
from nameko.rpc import RpcProxy
from nameko.web.handlers import http

from werkzeug.wrappers import Response
import uuid

from dependencies import SessionProvider


from itertools import permutations 
from itertools import combinations

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'data/news'


if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)




class GatewayService:
    name = 'gateway'

    user_rpc = RpcProxy('user_service')
    session_provider = SessionProvider()

    @http('POST', '/register')
    def add_user(self, request):
        result = request.json
        user = result ["username"]
        kunci = result ["password"]
        nambahroom = self.user_rpc.add_user(user,kunci)
        return nambahroom

    @http('GET', '/logout')
    def logout_user(self, request):
        cookies = request.cookies
        if cookies:
            response = Response('success')
            response.delete_cookie('SESSID')
            self.session_provider.delete_session(cookies['SESSID'])
            return response
        else:
            response = Response('You need to Login First')
            return response

    @http('POST', '/login')
    def check_user(self, request):
        result = request.json
        user_data = {
            'username': result['username'],
            'password': result['password']
        }
        cekuser = self.user_rpc.check_user(user_data)
        if cekuser== 1 :
            session_id = self.session_provider.set_session(user_data)
            response = Response(str(user_data))
            response.set_cookie('SESSID', session_id)
            return response
        
        else :
             return "username atau password salah"

    @http('POST', '/addnews')
    def add_news(self, request):
        cookies = request.cookies
        if cookies:
            arrnamafile = []
            files = request.files.getlist('file')
            for file in files:
                app = Flask(__name__)
                app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                arrnamafile.append(filename)
                
            add_news = self.user_rpc.add_news(arrnamafile, request.form['text'])
            return add_news

        else:
            response = Response('You need to Login First')
            return response

    @http('PUT', '/editnews/<int:newsid>')
    def edit_news(self, request,newsid):
        cookies = request.cookies
        if cookies:
            idnews = newsid
            arrnamafile = []
            files = request.files.getlist('file')
            for file in files:
                app = Flask(__name__)
                app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                arrnamafile.append(filename)
                
            edit_news = self.user_rpc.edit_news(arrnamafile, request.form['text'],idnews)
            return edit_news
        else:
            response = Response('You need to Login First')
            return response

    @http('PUT', '/deletenews/<int:newsid>')
    def delete_news(self, request,newsid):
        cookies = request.cookies
        if cookies:
            idnews = newsid
            delete_news = self.user_rpc.delete_news(idnews)
            return delete_news
        else:
            response = Response('You need to Login First')
            return response

    @http('GET', '/getnews')
    def get_news(self,request):
        get_news = self.user_rpc.get_news()
        response = Response(
            json.dumps(get_news),
            mimetype='application/json'
        )
        return response

    @http('GET', '/getnewsbyid/<int:newsid>')
    def get_newsbyid(self,request,newsid):
        get_newsbyid = self.user_rpc.get_newsbyid(newsid)
        response = Response(
            json.dumps(get_newsbyid),
            mimetype='application/json'
        )
        return response

    # @http('POST', '/permutation')
    # def permutation_user(self, request):
    #     cookies = request.cookies
    #     if cookies:
    #         result = request.json
    #         user_data = {
    #             'str': result['str']
    #         }
    #         hasil = ""
    #         a = user_data['str']
    #         p = permutations(a) 
    #         for j in list(p): 
    #             hasil+= str(j)
    #         return hasil
    #     else:
    #         response = Response('You need to Login First')
    #         return response
        
    # @http('POST', '/combination')
    # def combination_user(self, request):
    #     cookies = request.cookies
    #     hasil = ""
    #     if cookies:
    #         result = request.json
    #         user_data = {
    #             'str': result['str'],
    #             'combination': result['combination']
    #         }
    #         letters = user_data['str']
    #         combination=user_data['combination']
    #         a = combinations(letters,combination ) 
    #         y = [' '.join(i) for i in a]
    #         return str(y)
           
    #     else:
    #         response = Response('You need to Login First')
    #         return response
   

    # @http('GET', '/room')
    # def get_rooms(self, request):
    #     rooms = self.hotel_rpc.get_all_room()
    #     return json.dumps(rooms)

    # @http('GET', '/room/<int:nomer>')
    # def get_numroom(self, request, nomer):
    #     roomss = self.hotel_rpc.get_numroom(nomer)
    #     return json.dumps(roomss)

    # @http('POST', '/room')
    # def add_room(self, request):
    #     result = request.json
    #     roomtype = result ["id_room_type"]
    #     roomnumber = result ["room_number"]
    #     status = result["status"]
    #     nambahroom = self.hotel_rpc.add_room(roomtype,roomnumber,status)
    #     return nambahroom


    # @http('PUT', '/room/<int:nomor>')
    # def update_room(self, request ,nomor):
    #     perbarui = self.hotel_rpc.update_room(nomor)
    #     return json.dumps(perbarui)
    
    # @http('DELETE', '/room/<int:numur>')
    # def delete_room(self, request ,numur):
    #     hilang = self.hotel_rpc.delete_room(numur)
    #     return hilang
    