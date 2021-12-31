from django.urls import path

from . import views

# these should be under the /session route
urlpatterns = [
    path('', views.index, name='index'),  # show list of all avail routes here
    path("/startSession", views.startSession, name="startSession"),
    path("<int:xCoord>,<int:yCoord/", views.xyCoord, name="detail"),
    path("<int:scrollEvent>/", views.scrollEvent, name="scrollEvent"),  # user scrolls mouse wheel
    path("<int:xCoord>,<int:yCoord/", views.captureTouch, name="captureTouch"),  # for tap and drag on smartphone
    path("<int:height>,<int:width/", views.logScreenHeightWidth, name="logScreenHeightWidth"),
    path("/inactive", views.inactive, name="inactive"),
    path("/conversion", views.conversionEvent, name="conversionEvent"),
    # Admin routes
    path("/admin", views.admin, name="admin")
    # ... fill in later ... get meat and potatoes first
]

# brainstorm:
# need route to get mouse x,y every n milliseconds.
# need route to get screen width and height.
# need route to capture user inactive.
# route for conversion event.
# (a maybe perhaps but not definitely) separate route that captures the viewport every n milliseconds
# frontend load should be light, under 4 kilobytes
