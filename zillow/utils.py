from http.cookies import SimpleCookie

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.48114179541014%2C%22east%22%3A-80.01353620458983%2C%22south%22%3A25.617982377529394%2C%22north%22%3A25.927153253975412%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D'

def cookie_parser():
    cookie_string = 'zguid=23|%244c648293-8caf-49c2-a489-28058a01e2bd; zgsession=1|4783f76b-3077-4f61-a614-1214e4973a8e; _ga=GA1.2.1110083792.1594869676; _gid=GA1.2.1529546432.1594869676; zjs_user_id=null; zjs_anonymous_id=%224c648293-8caf-49c2-a489-28058a01e2bd%22; _pxvid=69c461dc-c713-11ea-88be-0242ac120005; _gcl_au=1.1.1703082868.1594869680; KruxPixel=true; DoubleClickSession=true; _pin_unauth=dWlkPU9EQTJOR1poTXpRdFpXUTRNeTAwTkdZd0xUa3paREV0TWpNeFlqVm1aREJsWTJVMA; KruxAddition=true; g_state={"i_p":1594877171734,"i_l":1}; JSESSIONID=7B1DC22A98293952A862316CE43DF848; GASession=true; search=6|1597465412350%7Crect%3D26.08143576798618%252C-79.82436536718748%252C25.463095740992443%252C-80.67031263281248%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D0%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0912700%09%09%09%09%09%09; _uetsid=df9818d4-154d-a645-dcb6-d28330dfe611; _uetvid=73de39ea-b442-0542-4866-08544a9a9c56; AWSALB=5dBASUVPsrfK7Ra/ujGrxrVVtKnKnIYsausOea2ppmKLV9T6j8QYkxG+kOkixYe7wRzA9Vpvg10eDcJCSHhgE4lLJ7zuMCPICGe9/XQqgf612DbG1yH/XFNO1B4d; AWSALBCORS=5dBASUVPsrfK7Ra/ujGrxrVVtKnKnIYsausOea2ppmKLV9T6j8QYkxG+kOkixYe7wRzA9Vpvg10eDcJCSHhgE4lLJ7zuMCPICGe9/XQqgf612DbG1yH/XFNO1B4d; _px3=9e0de2d2d7d4c1ee428d4a7e259334adb8a479b74800b798c3f16ad2106dd45b:dh5KY9uRNAdXJq5kuOvWd4+yLc6b9nhYgGBUarIQvGn/rlDsVZZ7YPHiLtI90cQ8HpDtn1k4NhLSpByaMVztkw==:1000:zdblLekDcdIARBpLAfcat1EZKKLOCffLl8oDLM/ZB7aT2xaddeCPxJ9snz+2uuaY4snAeCMRzbbPckIOT0DSUzNzMaXR7bzRXpKcqpwZSsTD5DT1Vv6USFScSkRrun4UEMTs9V6aqpBYvX1U33hCNIUFqGz5hHNHZkup0Z1xIxM='
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies
