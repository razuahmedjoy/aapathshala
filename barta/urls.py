from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from barta.views import Bartahome,SinglePost,CategoryPost,allSingleNotice


urlpatterns = [
    path('',Bartahome,name='bartahome'  ),
    path('all_notice/',allSingleNotice,name='all_notice'  ),
    
    path('<slug:catslug>/',CategoryPost,name='categorypost'  ),
    path('<slug:catslug>/<int:id>/',SinglePost,name='singlepost'  ),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)