from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    WholesalerProfile, 
    IoTNode, 
    CropBatch, 
    SensorLog,
    Listing,
    Transaction
)
from .serializers import (
    WholesalerProfileSerializer, 
    IoTNodeSerializer, 
    CropBatchSerializer, 
    SensorLogSerializer,
    ListingSerializer,
    TransactionSerializer
)

# --- EXISTING CORE VIEWSETS ---

class WholesalerProfileViewSet(viewsets.ModelViewSet):
    queryset = WholesalerProfile.objects.all()
    serializer_class = WholesalerProfileSerializer

class IoTNodeViewSet(viewsets.ModelViewSet):
    queryset = IoTNode.objects.all()
    serializer_class = IoTNodeSerializer

class CropBatchViewSet(viewsets.ModelViewSet):
    queryset = CropBatch.objects.all()
    serializer_class = CropBatchSerializer

class SensorLogViewSet(viewsets.ModelViewSet):
    queryset = SensorLog.objects.all()
    serializer_class = SensorLogSerializer

# --- NEW MARKETPLACE VIEWSETS ---

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-id') # Show newest first
    serializer_class = TransactionSerializer


# --- NEW PASSWORD RESET VIEWS (BREVO INTEGRATION) ---

@api_view(['POST'])
@permission_classes([AllowAny]) # Anyone can request a reset
def request_password_reset(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # We still return 'success' so hackers can't use this to check if an email exists in your system!
        return Response({'message': 'If an account with this email exists, a reset link has been sent.'}, status=status.HTTP_200_OK)

    # 1. Generate unique security tokens
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = PasswordResetTokenGenerator().make_token(user)
    
    # 2. Build the link that points to your React frontend
    reset_link = f"http://localhost:5173/reset-password/{uidb64}/{token}"

    # 3. Send the email using Brevo
    try:
        send_mail(
            subject="AgriResQ - Password Reset Request",
            message=f"Hello {user.first_name or user.username},\n\nYou requested a password reset for your AgriResQ account.\nClick the link below to set a new password:\n\n{reset_link}\n\nIf you did not request this, please ignore this email.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
    except Exception as e:
        print("Brevo Email Error:", e)
        return Response({'error': 'Failed to send email. Check Django console.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'message': 'If an account with this email exists, a reset link has been sent.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password_confirm(request):
    # Get the tokens and the new password sent by the React frontend
    uidb64 = request.data.get('uidb64')
    token = request.data.get('token')
    new_password = request.data.get('password')

    if not uidb64 or not token or not new_password:
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    # 1. Decode the User ID from the URL
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # 2. Verify the security token is valid for this specific user
    if user is not None and PasswordResetTokenGenerator().check_token(user, token):
        # 3. Update the database!
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'The reset link is invalid or has expired.'}, status=status.HTTP_400_BAD_REQUEST)