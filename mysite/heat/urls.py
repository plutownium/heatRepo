from django.urls import path

from . import views

# these should be under the /session route
urlpatterns = [
    # ex: /heat/index/
    # path('index/', views.index, name='index'),  # show list of all avail routes here
    # path('index2/', views.index2, name='index2'),  # show list of all avail routes here
    path('createUser/', views.create_user, name='create_user'),  # show list of all avail routes here
    path("startSession/<int:user_id>/<str:ip>/<int:width>/<int:height>",
         views.start_session, name="startSession"),
    path("<int:xCoord>,<int:yCoord/", views.log_x_y_coord, name="logXYCoord"),
    path("<int:scrollEvent>/", views.scroll_event, name="scrollEvent"),  # user scrolls mouse wheel
    path("<int:xCoord>,<int:yCoord/", views.capture_touch, name="capture_touch"),  # for tap and drag on smartphone
    path("log_screen_height_width/<int:height>/<int:width/",
         views.log_screen_height_width,
         name="log_screen_height_width"),
    path("inactive/<int:user_id>/<int:inactiveAt>", views.inactive_session, name="inactiveSession"),
    path("conversion/<int:user_id>/<int:conversionId>", views.log_conversion_event, name="logConversionEvent"),
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
