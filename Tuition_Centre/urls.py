
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),

    #**************************************staff module*****************************************
    #**************************************     Amal   *****************************************

    re_path(r'^$', views.Software, name='Software'),
    re_path(r'^Staff_dashboard$', views.Staff_dashboard, name='Staff_dashboard'),
    re_path(r'^Staff_index/$', views.Staff_index, name='Staff_index'),
   
    re_path(r'^Staff_accsetting/$', views.Staff_accsetting, name='Staff_accsetting'),
    re_path(r'^Staff_accsettingimagechange/$', views.Staff_accsettingimagechange, name='Staff_accsettingimagechange'),
    re_path(r'^Staff_changepwd/$', views.Staff_changepwd, name='Staff_changepwd'),
    re_path(r'^Staff_attendance/$', views.Staff_attendance, name='Staff_attendance'),
    re_path(r'^Staff_attandance/$', views.Staff_attendancesort, name='Staff_attendancesort'),
    re_path(r'^Staff_reportissues/$', views.Staff_reportissues, name='Staff_reportissues'),
    re_path(r'^Staff_reportedissue/$', views.Staff_reportedissue, name='Staff_reportedissue'),
    re_path(r'^Staff_reportanissue/$', views.Staff_reportanissue, name='Staff_reportanissue'),
    re_path(r'^Staff_issuereportsstudents/$', views.Staff_issuereportsstudents, name='Staff_issuereportsstudents'),
    re_path(r'^Staffreplyview/$', views.Staffreplyview, name='Staffreplyview'),
    re_path(r'^Staffissuereply/$', views.Staffissuereply, name='Staffissuereply'),

    #**************************************   Subeesh  ************************************

    re_path(r'^Staff_leave/$', views.Staff_leave, name='Staff_leave'),
    re_path(r'^Staff_Student_det/$', views.Staff_Student_det, name='Staff_Student_det'),
    re_path(r'^Staff_apply_leave/$', views.Staff_apply_leave, name='Staff_apply_leave'),
    re_path(r'^Staff_Req_leave/$', views.Staff_Req_leave, name='Staff_Req_leave'),
    re_path(r'^Staff_studentsleave_table/$', views.Staff_studentsleave_table, name='Staff_studentsleave_table'),
    re_path(r'^Staff_current_students/$', views.Staff_current_students, name='Staff_current_students'),
    re_path(r'^Staff_previous_students/$', views.Staff_previous_students, name='Staff_previous_students'),

    re_path(r'^Staff_progress_det/$', views.Staff_progress_det, name='Staff_progress_det'),
    re_path(r'^Staff_progress_report/$', views.Staff_progress_report, name='Staff_progress_report'),
   
    re_path(r'^Staff_progress_report_table/$', views.Staff_progress_report_table, name='Staff_progress_report_table'),
    re_path(r'^Staff_student_dashboard/$', views.Staff_student_dashboard, name='Staff_student_dashboard'),
    re_path(r'^Staff_previous_student_dashboard/$', views.Staff_previous_student_dashboard, name='Staff_previous_student_dashboard'),
    re_path(r'^Staff_progress_report_show/$', views.Staff_progress_report_show, name='Staff_progress_report_show'),

    #**************************************Student module*****************************************
    #**************************************   Akhil & Anwar   ************************************

    re_path(r'^Student_index/$', views.Student_index, name='Student_index'),
    re_path(r'^Student_applyleave_cards/$', views.Student_applyleave_cards, name='Student_applyleave_cards'),
    re_path(r'^Student_leavereq/$', views.Student_leavereq, name='Student_leavereq'),
    re_path(r'^Student_reqedleave/$', views.Student_reqedleave, name='Student_reqedleave'),
    re_path(r'^Student_leaverejected/$', views.Student_leaverejected, name='Student_leaverejected'),
    re_path(r'^Student_progressreport/$', views.Student_progressreport, name='Student_progressreport'),

    # anwar student module

    re_path(r'^Student_accsetting/$', views.Student_accsetting, name='Student_accsetting'),
    re_path(r'^Student_accsettingimagechange/$', views.Student_accsettingimagechange, name='Student_accsettingimagechange'),
    re_path(r'^Student_changepwd/$', views.Student_changepwd, name='Student_changepwd'),  
    re_path(r'^Student_profiledash/$', views.Student_profiledash, name='Student_profiledash'),
    re_path(r'^Student_attendance/$', views.Student_attendance, name='Student_attendance'),
    re_path(r'^Student_attendancesort/$', views.Student_attendancesort, name='Student_attendancesort'),
    re_path(r'^Student_reportissues/$', views.Student_reportissues, name='Student_reportissues'),
    re_path(r'^Student_reportissue1/$', views.Student_reportissue1, name='Student_reportissue1'),
    re_path(r'^Student_reportissue2/$', views.Student_reportissue2, name='Student_reportissue2'),
    re_path(r'^Studentreportsuccess/$', views.Studentreportsuccess, name='Studentreportsuccess'),
    re_path(r'^Student_reportissuereply/$', views.Student_reportissuereply, name='Student_reportissuereply'),

    #**************************************Manager module*****************************************

    #------------sharon-------------------

    re_path(r'^Man_index/$', views.Man_index, name='Man_index'),
    re_path(r'^MAN_profile/$',views.MAN_profile, name="MAN_profile"),
    re_path(r'^MAN_registration/$',views.MAN_registration, name="MAN_registration"),
    re_path(r'^MAN_registrationstaff/$',views.MAN_registrationstaff, name="MAN_registrationstaff"),
    re_path(r'^MAN_registrationstudent/$',views.MAN_registrationstudent, name="MAN_registrationstudent"),
    re_path(r'^MAN_currentstaff/$',views.MAN_currentstaff, name="MAN_currentstaff"),
    re_path(r'^MAN_resignedstaff/$',views.MAN_resignedstaff, name="MAN_resignedstaff"),
    re_path(r'^MAN_currentstudent/$',views.MAN_currentstudent, name="MAN_currentstudent"),
    re_path(r'^MAN_resignedstudent/$',views.MAN_resignedstudent, name="MAN_resignedstudent"),
    re_path(r'^MAN_addbatch/$',views.MAN_addbatch, name="MAN_addbatch"),

    re_path(r'^MAN_changepwd/$', views.MAN_changepwd, name='MAN_changepwd'),
    re_path(r'^MAN_accsetting/$', views.MAN_accsetting, name='MAN_accsetting'),
    re_path(r'^MAN_accsettingimagechange/$', views.MAN_accsettingimagechange, name='MAN_accsettingimagechange'),

      #------------------Meenu---------------#

    re_path(r'^Manager_staff$',views.Manager_staff, name="Manager_staff"),  
    re_path(r'^Manager_currentstaffdetails$',views.Manager_currentstaffdetails, name="Manager_currentstaffdetails"),   
    re_path(r'^Manager_previousstaffdetails$',views.Manager_previousstaffdetails, name="Manager_previousstaffdetails"), 
    re_path(r'^Manager_staffprofile$',views.Manager_staffprofile, name="Manager_staffprofile"), 
    re_path(r'^Manager_attendancesearch$',views.Manager_attendancesearch, name="Manager_attendancesearch"),   
    re_path(r'^Manager_attendancesort$',views.Manager_attendancesort, name="Manager_attendancesort"),   
    re_path(r'^Manager_student$',views.Manager_student, name="Manager_student"),
    re_path(r'^Manager_currentstudentdetails$',views.Manager_currentstudentdetails, name="Manager_currentstudentdetails"),  
    re_path(r'^Manager_previousstudentdetails$',views.Manager_previousstudentdetails, name="Manager_previousstudentdetails"),  
    re_path(r'^Manager_studentprofile$',views.Manager_studentprofile, name="Manager_studentprofile"),  
    re_path(r'^Manager_student_attendancesearch$',views.Manager_student_attendancesearch, name="Manager_student_attendancesearch"),   
    re_path(r'^Manager_sort$',views.Manager_sort, name="Manager_sort"),
    re_path(r'^Manager_performance_report$',views.Manager_performance_report, name="Manager_performance_report"),   
    re_path(r'^Manager_leaverequest_staff$',views.Manager_leaverequest_staff, name="Manager_leaverequest_staff"),
    re_path(r'^Manager_apply_leave$',views.Manager_apply_leave, name="Manager_apply_leave"),
    re_path(r'^Manager_requestleave$',views.Manager_requestleave, name="Manager_requestleave"),
    re_path(r'^Manager_staffleave$',views.Manager_staffleave, name="Manager_staffleave"),
    re_path(r'^Manager_rejected_leave$',views.Manager_rejected_leave, name="Manager_rejected_leave"),
    re_path(r'^Manager_accepted_leave$',views.Manager_accepted_leave, name="Manager_accepted_leave"),
    re_path(r'^Manager_academics$',views.Manager_academics,name="Manager_academics"),
    re_path(r'^Manager_Academics_batch$', views.Manager_Academics_batch,name='Manager_Academics_batch'),
    re_path(r'^Manager_academics_viewbatch$',views.Manager_academics_viewbatch,name="Manager_academics_viewbatch"),
    re_path(r'^Manager_academics_delete$',views.Manager_academics_delete,name="Manager_academics_delete") , 
    re_path(r'^Manager_academics_update$', views.Manager_academics_update,name='Manager_academics_update'),
    re_path(r'^Manager_academics_updatesave$', views.Manager_academics_updatesave,name='Manager_academics_updatesave'),

    #---------------nimisha------------#
    re_path(r'^Manager_academics_class$', views.Manager_academics_class,name='Manager_academics_class'),
    re_path(r'^Manager_ViewClass$',views.Manager_ViewClass, name="Manager_ViewClass"),
    re_path(r'^Manager_UpdateClass$',views.Manager_UpdateClass, name="Manager_UpdateClass"),
    
    #------------anadhu----------#
    re_path(r'^MAN_AcademicAddClass$', views.MAN_AcademicAddClass, name='MAN_AcademicAddClass'),

    #---------------Akhil P T-----------#
    
    re_path(r'^MAN_Report$', views.MAN_Report, name='MAN_Report'),
    re_path(r'^MAN_ReportedissueShow$', views.MAN_ReportedissueShow, name='MAN_ReportedissueShow'),
    re_path(r'^MAN_ReportedissueShow1/$',views.MAN_ReportedissueShow1, name='MAN_ReportedissueShow1'),
    re_path(r'^MAN_ReportedissueShowstaff$', views.MAN_ReportedissueShowstaff, name='MAN_ReportedissueShowstaff'),
    re_path(r'^MAN_ReportedissueShow1staff/$',views.MAN_ReportedissueShow1staff, name='MAN_ReportedissueShow1staff'),
    re_path(r'^MAN_manager_report$', views.MAN_manager_report, name='MAN_manager_report'),
    re_path(r'^MAN_Reportissue$', views.MAN_Reportissue, name='MAN_Reportissue'),
    re_path(r'^MAN_reportsuccess$', views.MAN_reportsuccess, name='MAN_reportsuccess'),
    re_path(r'^MAN_manger_reportedissues$', views.MAN_manger_reportedissues, name='MAN_manger_reportedissues'),
    re_path(r'^MAN_manger_reportedissues1/$', views.MAN_manger_reportedissues1, name='MAN_manger_reportedissues1'),
    
    #------------------Subeesh-----------#
    re_path(r'^MAN_subjects/$', views.MAN_subjects, name='MAN_subjects'),
    re_path(r'^MAN_Viewsubject/$', views.MAN_Viewsubject, name='MAN_Viewsubject'),
    re_path(r'^MAN_Updatesubject/$', views.MAN_Updatesubject, name='MAN_Updatesubject'),

    #----------------Anwar---------------#
    re_path(r'^Man_AddSubject/$', views.Man_AddSubject, name='Man_AddSubject'),


#**************************************Account module*****************************************
#**************************************     sharon & subeesh   ****************************************

    re_path(r'^Account_Student_det/$', views.Account_Student_det, name='Account_Student_det'),
    re_path(r'^Account_previous_students/$', views.Account_previous_students, name='Account_previous_students'),
    re_path(r'^Acc_index$', views.Acc_index, name='Acc_index'),
    re_path(r'^Account_dashboard$', views.Account_dashboard, name='Account_dashboard'),

    # sharon

    re_path(r'^acc_issue/$',views.acc_issue, name="acc_issue"),
    re_path(r'^acc_reportedissue/$',views.acc_reportedissue, name="acc_reportedissue"),
    re_path(r'^acc_report_an_issue/$',views.acc_report_an_issue, name="acc_report_an_issue"),
    re_path(r'^account_issuereply/$',views.account_issuereply, name="account_issuereply"),
    re_path(r'^acc_leaverequest/$',views.acc_leaverequest, name="acc_leaverequest"),
    re_path(r'^acc_applyleave/$',views.acc_applyleave, name="acc_applyleave"),
    re_path(r'^acc_requestedleave/$',views.acc_requestedleave, name="acc_requestedleave"),


    #************************************Admin module*******************************

     
    #----------------Admin------------------ 
    re_path(r'^Admin_index/$',views.Admin_index,name='Admin_index'),
    #----------------Academic------------------ 
    re_path(r'^Admin_Academic/$',views.Admin_Academic,name='Admin_Academic'),
    re_path(r'^Admin_Academic_Class/$',views.Admin_Academic_Class,name='Admin_Academic_Class'),
    re_path(r'^Admin_Academic_AddClass/$',views.Admin_Academic_AddClass,name='Admin_Academic_AddClass'),
    re_path(r'^Admin_Academic_ViewClass/$',views.Admin_Academic_ViewClass,name='Admin_Academic_ViewClass'),
    re_path(r'^Admin_Academic_UpdateClass/$',views.Admin_Academic_UpdateClass,name='Admin_Academic_UpdateClass'),
    re_path(r'^Admin_Academic_Subject/$',views.Admin_Academic_Subject,name='Admin_Academic_Subject'),
    re_path(r'^Admin_Academic_AddSubject/$',views.Admin_Academic_AddSubject,name='Admin_Academic_AddSubject'),
    re_path(r'^Admin_Academic_ViewSubject/$',views.Admin_Academic_ViewSubject,name='Admin_Academic_ViewSubject'),
    re_path(r'^Admin_Academic_UpdateSubject/$',views.Admin_Academic_UpdateSubject,name='Admin_Academic_UpdateSubject'),
    #----------------Attendance------------------
    re_path(r'^Admin_Attendance/$',views.Admin_Attendance,name='Admin_Attendance'),
    re_path(r'^Admin_Attendance_Show/$',views.Admin_Attendance_Show,name='Admin_Attendance_Show'),
    #----------------Reportedissues------------------
    re_path(r'^Admin_Reportedissues_Card/$',views.Admin_Reportedissues_Card,name='Admin_Reportedissues_Card'),
    re_path(r'^Admin_Reportedissues_Show/$',views.Admin_Reportedissues_Show,name='Admin_Reportedissues_Show'),
    re_path(r'^Admin_Reportedissues/$',views.Admin_Reportedissues,name='Admin_Reportedissues'),
    re_path(r'^Admin_ManagerReportedissues/$',views.Admin_ManagerReportedissues,name='Admin_ManagerReportedissues'),
    #----------------LeaveRequest------------------
    re_path(r'^Admin_LeaveRequest/$',views.Admin_LeaveRequest,name='Admin_LeaveRequest'),
    re_path(r'^Admin_LeaveRejected/$',views.Admin_LeaveRejected,name='Admin_LeaveRejected'),

    #----------------Dashboard------------------
    re_path(r'^Admin_dashboard$', views.Admin_dashboard, name='Admin_dashboard'),
    re_path(r'^superadmin_changepwd$', views.superadmin_changepwd, name='superadmin_changepwd'),
    #----------------Academic Batch------------------
    re_path(r'^AcademicBatch_Admin$', views.AcademicBatch_Admin, name='AcademicBatch_Admin'),
    re_path(r'^AcademicAddBatch_Admin$', views.AcademicAddBatch_Admin, name='AcademicAddBatch_Admin'),
    re_path(r'^AcademicAddBatch_Adminsave$', views.AcademicAddBatch_Adminsave, name='AcademicAddBatch_Adminsave'),
    re_path(r'^AcademicAddBatchUpdate_Admin$', views.AcademicAddBatchUpdate_Admin, name='AcademicAddBatchUpdate_Admin'),
    re_path(r'^AcademicAddBatchUpdate_Adminsave$', views.AcademicAddBatchUpdate_Adminsave, name='AcademicAddBatchUpdate_Adminsave'),
    re_path(r'^AcademicViewBatch_Admin$', views.AcademicViewBatch_Admin, name='AcademicViewBatch_Admin'),
    re_path(r'^AcademicAddBatch_Admindelete$', views.AcademicAddBatch_Admindelete, name='AcademicAddBatch_Admindelete'),

    #----------------Registration------------------
    re_path(r'^Registration_Admin$', views.Registration_Admin, name='Registration_Admin'),
    re_path(r'^RegistrationStaff_Admin$', views.RegistrationStaff_Admin, name='RegistrationStaff_Admin'),
    re_path(r'^RegistrationStudent_Admin$', views.RegistrationStudent_Admin, name='RegistrationStudent_Admin'),
    re_path(r'^RegistrationCurrentStaff_Admin$', views.RegistrationCurrentStaff_Admin, name='RegistrationCurrentStaff_Admin'),
    re_path(r'^RegistrationCurrentStaff_Adminsave$', views.RegistrationCurrentStaff_Adminsave, name='RegistrationCurrentStaff_Adminsave'),
    re_path(r'^RegistrationCurrentStaffAdmin_update$', views.RegistrationCurrentStaffAdmin_update, name='RegistrationCurrentStaffAdmin_update'),
    re_path(r'^RegistrationCurrentStaffAdmin_updatessave$', views.RegistrationCurrentStaffAdmin_updatessave, name='RegistrationCurrentStaffAdmin_updatessave'),
    re_path(r'^RegistrationCurrentStaffAdmin_delete$', views.RegistrationCurrentStaffAdmin_delete, name='RegistrationCurrentStaffAdmin_delete'),
    re_path(r'^RegistrationResignedStaffAdmin_update$', views.RegistrationResignedStaffAdmin_update, name='RegistrationResignedStaffAdmin_update'),
    re_path(r'^RegistrationResignedStaffAdmin_updatessave$', views.RegistrationResignedStaffAdmin_updatessave, name='RegistrationResignedStaffAdmin_updatessave'),
    re_path(r'^RegistrationResignedStaffAdmin_delete$', views.RegistrationResignedStaffAdmin_delete, name='RegistrationResignedStaffAdmin_delete'),
    re_path(r'^RegistrationResignedStaff_Admin$', views.RegistrationResignedStaff_Admin, name='RegistrationResignedStaff_Admin'),
    re_path(r'^RegistrationCurrentStudent_Admin$', views.RegistrationCurrentStudent_Admin, name='RegistrationCurrentStudent_Admin'),
    re_path(r'^RegistrationCurrentStudent_Adminsave$', views.RegistrationCurrentStudent_Adminsave, name='RegistrationCurrentStudent_Adminsave'),
    re_path(r'^RegistrationCurrentStudentAdmin_update$', views.RegistrationCurrentStudentAdmin_update, name='RegistrationCurrentStudentAdmin_update'),
    re_path(r'^RegistrationCurrentStudent_updatessave$', views.RegistrationCurrentStudent_updatessave, name='RegistrationCurrentStudent_updatessave'),
    re_path(r'^RegistrationCurrentStudentAdmin_delete$', views.RegistrationCurrentStudentAdmin_delete, name='RegistrationCurrentStudentAdmin_delete'),
    re_path(r'^RegistrationPreviousstudent_Admin$', views.RegistrationPreviousstudent_Admin, name='RegistrationPreviousstudent_Admin'),
    re_path(r'^RegistrationPreviousstudentAdmin_update$', views.RegistrationPreviousstudentAdmin_update, name='RegistrationPreviousstudentAdmin_update'),
    re_path(r'^RegistrationPreviousstudentAdmin_updatessave$', views.RegistrationPreviousstudentAdmin_updatessave, name='RegistrationPreviousstudentAdmin_updatessave'),
    re_path(r'^RegistrationPreviousstudentAdmin_delete$', views.RegistrationPreviousstudentAdmin_delete, name='RegistrationPreviousstudentAdmin_delete'),
    #----------------Staff------------------
    re_path(r'^Staff_Admin$', views.Staff_Admin, name='Staff_Admin'),
    re_path(r'^StaffCurrentstaff_Admin$', views.StaffCurrentstaff_Admin, name='StaffCurrentstaff_Admin'),
    re_path(r'^StaffPreviousstaff_Admin$', views.StaffPreviousstaff_Admin, name='StaffPreviousstaff_Admin'),
    re_path(r'^StaffCurrentstaffProfile_Admin$', views.StaffCurrentstaffProfile_Admin, name='StaffCurrentstaffProfile_Admin'),
    re_path(r'^StaffPreviousstaffProfile_Admin$', views.StaffPreviousstaffProfile_Admin, name='StaffPreviousstaffProfile_Admin'),
    re_path(r'^StaffCurrentstaffAttendance_Admin$', views.StaffCurrentstaffAttendance_Admin, name='StaffCurrentstaffAttendance_Admin'),
    re_path(r'^StaffCurrentstaffAttendanceSort_Admin$', views.StaffCurrentstaffAttendanceSort_Admin, name='StaffCurrentstaffAttendanceSort_Admin'),
    re_path(r'^StaffCurrentstaffPerformance_Admin$', views.StaffCurrentstaffPerformance_Admin, name='StaffCurrentstaffPerformance_Admin'),
    re_path(r'^StaffPreviousstaffAttendance_Admin$', views.StaffPreviousstaffAttendance_Admin, name='StaffPreviousstaffAttendance_Admin'),
    re_path(r'^StaffPreviousstaffAttendanceSort_Admin$', views.StaffPreviousstaffAttendanceSort_Admin, name='StaffPreviousstaffAttendanceSort_Admin'),
    re_path(r'^StaffPreviousstaffPerformance_Admin$', views.StaffPreviousstaffPerformance_Admin, name='StaffPreviousstaffPerformance_Admin'),
    re_path(r'^StaffCurrentstaffPerformance_Adminsave$', views.StaffCurrentstaffPerformance_Adminsave, name='StaffCurrentstaffPerformance_Adminsave'),
    re_path(r'^StaffPreviousstaffPerformance_Adminsave$', views.StaffPreviousstaffPerformance_Adminsave, name='StaffPreviousstaffPerformance_Adminsave'),
    
    #----------------Student------------------
    re_path(r'^Student_Admin$', views.Student_Admin, name='Student_Admin'),
    re_path(r'^StudentCurrentstudent_Admin$', views.StudentCurrentstudent_Admin, name='StudentCurrentstudent_Admin'),
    re_path(r'^StudentPreviousstudent_Admin$', views.StudentPreviousstudent_Admin, name='StudentPreviousstudent_Admin'),
    re_path(r'^StudentCurrentstudentProfile_Admin$', views.StudentCurrentstudentProfile_Admin, name='StudentCurrentstudentProfile_Admin'),
    re_path(r'^StudentPreviousstudentProfile_Admin$', views.StudentPreviousstudentProfile_Admin, name='StudentPreviousstudentProfile_Admin'),
    re_path(r'^StudentCurrentstudentAttendance_Admin$', views.StudentCurrentstudentAttendance_Admin, name='StudentCurrentstudentAttendance_Admin'),
    re_path(r'^StudentCurrentstudentAttendanceSort_Admin$', views.StudentCurrentstudentAttendanceSort_Admin, name='StudentCurrentstudentAttendanceSort_Admin'),
    re_path(r'^StudentCurrentstudentPerformance_Admin$', views.StudentCurrentstudentPerformance_Admin, name='StudentCurrentstudentPerformance_Admin'),
    re_path(r'^StudentPreviousstudentAttendance_Admin$', views.StudentPreviousstudentAttendance_Admin, name='StudentPreviousstudentAttendance_Admin'),
    re_path(r'^StudentPreviousstudentAttendanceSort_Admin$', views.StudentPreviousstudentAttendanceSort_Admin, name='StudentPreviousstudentAttendanceSort_Admin'),
    re_path(r'^StudentPreviousstudentPerformance_Admin$', views.StudentPreviousstudentPerformance_Admin, name='StudentPreviousstudentPerformance_Admin'),
    re_path(r'^StudentCurrentstudentPerformance_Adminsave$', views.StudentCurrentstudentPerformance_Adminsave, name='StudentCurrentstudentPerformance_Adminsave'),
    re_path(r'^StudentPreviousstudentPerformance_Adminsave$', views.StudentPreviousstudentPerformance_Adminsave, name='StudentPreviousstudentPerformance_Adminsave'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
