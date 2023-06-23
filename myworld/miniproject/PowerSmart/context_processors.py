from .models import USERS

def user_details(request):
    if 'id' in request.session:
        i = request.session['id']
        udet = USERS.objects.get(id=i)
        return {'fname': udet.FirstName, 'lname': udet.LastName}
    return {}
