"""recruit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from questionnaire.views import SurveyViewSet, IterationViewSet, QuestionViewSet, AnswerOptionViewSet, AnswerViewSet

# Create the root router
router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'iterations', IterationViewSet)

# Nested routers for establishing hierarchical relationships
# Nested routes for questions under surveys
surveys_router = NestedDefaultRouter(router, r'surveys', lookup='survey')
surveys_router.register(r'questions', QuestionViewSet,
                        basename='survey-questions')

# Nested routes for answer options under questions
questions_router = NestedDefaultRouter(
    surveys_router, r'questions', lookup='question')
questions_router.register(
    r'answeroptions', AnswerOptionViewSet, basename='question-answeroptions')

# Nested routes for answers under iterations
iterations_router = NestedDefaultRouter(
    router, r'iterations', lookup='iteration')
iterations_router.register(r'answers', AnswerViewSet,
                           basename='iteration-answers')


# Define URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel route
    path('', include(router.urls)),  # Include routes from the root router
    path('', include(surveys_router.urls)),
    path('', include(questions_router.urls)),
    path('', include(iterations_router.urls)),
]
