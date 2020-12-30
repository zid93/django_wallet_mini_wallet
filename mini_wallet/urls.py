"""mini_wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from mini_wallet.core import views
from mini_wallet import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/v1/init/$', views.initAccount.as_view(), name='generate-token'),
    url(r'^api/v1/wallet/$', views.statusWallet.as_view(), name='status-wallet'),
    url(r'^api/v1/wallet/deposit/$', views.depositBalance.as_view(), name='deposit-balance'),
    url(r'^api/v1/wallet/withdrawals/$', views.withdrawBalance.as_view(), name='withdraw-balance'),
]
