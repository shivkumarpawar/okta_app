# myapp/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from djangosaml2.decorators import login_required
from djangosaml2.views import assertion_consumer_service

import os

class InitiateSAMLAuthenticationView(View):
    def get(self, request, *args, **kwargs):
        # Construct the Okta SAML login URL
        okta_sso_url = os.getenv("OKTA_SAML_LOGIN_URL")
        return render(request, 'initiate_sso.html', {'okta_sso_url': okta_sso_url})

SAMLAuthenticatedView = method_decorator(login_required)(View)

class SAMLResponseHandlerView(View):
    def post(self, request, *args, **kwargs):
        # Process the SAML Response
        response = assertion_consumer_service(request)
        # Handle the response, e.g., log in the user
        return HttpResponse("SAML Response handled successfully")
