from rest_framework import routers
from blogs import views as myapp_views

router = routers.DefaultRouter()
router.register(r'customs', myapp_views.CustomViewset)
router.register(r'blogposts', myapp_views.BlogPostViewset)
