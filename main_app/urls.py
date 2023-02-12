from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.search_results_of_student, name='search_results'),
    path('add/qmemo/<int:sid>', views.add_q_memorize, name='add_q_memo'),
    path('add/qtest', views.add_q_test, name='add_q_test'),
    path('prelogout', views.before_logout, name='before_logout'), 
    path('create/note', views.create_memorizing_note, name='create_note'), 
    path('delete/note/<int:nid>', views.del_note, name='delete_note'), 
    path('master/activity/list', views.MessagesList.as_view(), name='master_activity'),
    path('master/activity/delete/<int:pk>', views.MessageDelete.as_view(), name='master_activity_delete'),
    path('coming/search', views.search_coming, name='search_coming'),
    path('coming/search/result', views.search_results_of_student_coming, name='search_results_coming'),
    path('coming/add', views.add_coming, name='add_coming'),
    path('coming/list', views.ComingList.as_view(), name='list_coming'),
    path('coming/delete/<int:pk>', views.ComingDelete.as_view(), name='delete_coming'),
    path('control', views.main_admin, name='admin_main'),
    path('control/settings/<int:pk>', views.AdminSettingsSiteView.as_view(), name='admin_site_settings'),
    path('control/awqaf', views.awqaf_admin, name='admin_awqaf'),
    path('control/activities', views.admin_activity_master, name='admin_master_activities'),
    path('control/coming', views.admin_coming_list, name='admin_coming_list'),
    path('control/activities/delete/<int:pk>', views.DeleteMessageAdminPanel.as_view(), name='admin_delete_activity'),
    path('control/coming/delete/<int:pk>', views.DeleteComingAdminPanel.as_view(), name='admin_delete_coming'),
    path('control/master', views.master_list_admin, name='admin_master_list'),
    path('control/master/<int:mid>', views.master_edit_permissions, name='admin_master_permission_edit'),
    path('control/points/log', views.admin_editing_points_log, name='admin_editing_points_log'),
    path('control/specializations', views.admin_specializations, name='admin_specializations'),
    path('points', views.editing_points, name='editing_points'),
    path('points/json', views.editing_points_json, name='editing_points_json'),
    path('points/log', views.editing_points_log, name='editing_points_log'),
    path('points/delete/add/<int:aid>', views.deleting_editing_points_add, name='editing_points_delete_add'),
    path('points/delete/remove/<int:rid>', views.deleting_editing_points_remove, name='editing_points_delete_remove'),
    path('reports/student', views.students_reports, name='reports_all_students'),
    path('money/delete', views.deleting_money, name='money_deleting'),
]