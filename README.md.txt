@http('POST', '/register')
-berfungsi untuk meregister akun dengan format json

request body
{
"username" : "<username>"
"password" : "<password>"
}

response body
add success

@http('GET', '/logout')
-berfungsi untuk menghilangkan session akun 

@http('POST', '/login')
-berfungsi untuk mendapatkan session
{
"username" : "<username>"
"password" : "<password>"
}

@http('POST', '/addnews')
-berfungsi untuk menambahkan news 

@http('PUT', '/editnews/<int:newsid>')
-berfungsi untuk mengedit news dengan id tertentu

@http('PUT', '/deletenews/<int:newsid>')
berfungsi untuk menghilangkan news dengan id tertentu

@http('GET', '/getnews')
-berfungsi untuk mendapatkan semua berita yang ada

@http('GET', '/getnewsbyid/<int:newsid>')
-berfungsi untuk mendapatkan berita dengan id tertentu
