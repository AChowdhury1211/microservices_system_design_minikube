import os , requests

def login(request):
    auth = request.authorization
    if not auth:
        return None, ("Missing Credentials", 401)
    basic_Auth = (auth.username, auth.password)
    
    reponse = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login", auth = basic_Auth
    )
    
    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)