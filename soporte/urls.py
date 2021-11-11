from django.urls    import path
from .views         import PersonaSoporteListCreate, PersonaSoporteUpdateDelete, PQRListCreate, PQRUpdateDelete

urlpatterns = [
    path('persona-soporte/',            PersonaSoporteListCreate.as_view()),
    #.as_view() -> para clases

    # en el delete no hay body, por eso utilizamos el URL PARAMS
    path('persona-soporte/<int:pk>',    PersonaSoporteUpdateDelete.as_view()),
    # pk = primary key, se debe llamar asi por que ya es una clase diseñada(sobreescrita)

    path('pqr/',                    PQRUpdateDelete.as_view()),
    path('pqr/<int:pk>',            PQRUpdateDelete.as_view())
]