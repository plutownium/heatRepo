from django.urls import path

from . import views

# these should be under the /session route
urlpatterns = [
    # ex: /heat/index/
    path('index/', views.index, name='index'),  # show list of all avail routes here
    path('index2/', views.index2, name='index2'),  # show list of all avail routes here
    path('index3/', views.index3, name='index3'),  # show list of all avail routes here
    path("startSession/", views.startSession, name="startSession"),
    path("<int:xCoord>,<int:yCoord/", views.logXYCoord, name="logXYCoord"),
    path("<int:scrollEvent>/", views.scrollEvent, name="scrollEvent"),  # user scrolls mouse wheel
    path("<int:xCoord>,<int:yCoord/", views.captureTouch, name="captureTouch"),  # for tap and drag on smartphone
    path("<int:height>,<int:width/", views.logScreenHeightWidth, name="logScreenHeightWidth"),
    path("inactive/", views.inactiveSession, name="inactiveSession"),
    path("conversion/", views.logConversionEvent, name="logConversionEvent"),
    # Admin routes
    # path("/admin", views.admin, name="admin"),
    # ... fill in later ... get meat and potatoes first
    # Client view routes
    # path("/", views.userView, name="userView")
    # need: a) way to see heatmaps b) way to see user sessions' play by play (live video kinda)
    # c) way for users to leave notes to other people like what Figma has
]

# brainstorm:
# need route to get mouse x,y every n milliseconds.
# need route to get screen width and height.
# need route to capture user inactive.
# route for conversion event.
# (a maybe perhaps but not definitely) separate route that captures the viewport every n milliseconds
# frontend load should be light, under 4 kilobytes
