# myapp/urls.py

from django.urls import path
from .views import InitiateSAMLAuthenticationView, SAMLAuthenticatedView, SAMLResponseHandlerView

urlpatterns = [
    path('sso/initiate/', InitiateSAMLAuthenticationView.as_view(), name='initiate_saml_authentication'),
    path('sso/authenticated/', SAMLAuthenticatedView.as_view(), name='saml_authenticated_view'),
    path('sso/response/', SAMLResponseHandlerView.as_view(), name='saml_response_handler'),
]
