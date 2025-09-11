from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

import fjorddemo.app.views
import libfjordweb.views
from libfjordweb.urls import urlpatterns

handler500 = "libfjordweb.views.handler500"

urlpatterns += [
    re_path(r"^$", fjorddemo.app.views.index, name="index"),
    re_path(r"^new_json$", fjorddemo.app.views.NewJSONInput.as_view(), name="new_json"),
    re_path(
        r"^data/([\w\-]+)$", fjorddemo.app.views.ExploreView.as_view(), name="explore"
    ),
    re_path(
        r"^data/([\w\-]+)/processing_status_api$",
        libfjordweb.views.ExploreDataProcessingStatusAPIView.as_view(),
        name="explore_processing_status_api$",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
