from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import json

User = get_user_model()

@csrf_exempt
def debug_auth(request):
    """Debug endpoint to test authentication"""
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        try:
            user = User.objects.get(email=email)
            user_info = {
                'exists': True,
                'active': user.active,
                'email': user.email,
                'staff': user.staff,
                'admin': user.admin,
                'merchant': user.merchant,
            }
            
            # Test authentication
            auth_user = authenticate(username=email, password=password)
            user_info['auth_success'] = auth_user is not None
            
        except User.DoesNotExist:
            user_info = {'exists': False}
        
        return JsonResponse(user_info)
    
    return JsonResponse({'error': 'POST method required'})