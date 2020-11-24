path('pages/<int:pk>/delete/',
         pages_views.delete_pages,
         name='delete_pages'),