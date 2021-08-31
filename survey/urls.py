from django.urls import path

from survey import api


app_name = 'survey'
urlpatterns = [
    path('login/', api.login, name='login'),
    # Опросы (surveys)
    path('survey/create/', api.survey_create, name='survey_create'),
    path('survey/update/<int:survey_id>/', api.survey_update, name='survey_update'),
    path('survey/view/', api.survey_view, name='survey_view'),
    path('survey/view/active/', api.active_survey_view, name='active_survey_view'),
    # Вопрос (question)
    path('question/create/', api.question_create, name='question_create'),
    path('question/update/<int:question_id>/', api.question_update, name='question_update'),
    # Выбор (choice)
    path('choice/create/', api.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', api.choice_update, name='choice_update'),
    # Ответ (answer)
    path('answer/create/', api.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', api.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', api.answer_update, name='answer_update')

]

