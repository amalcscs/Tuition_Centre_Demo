import os
import random
from django.shortcuts import render, redirect
from app.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.http import HttpResponse


#**************************************Staff module*****************************************
#**************************************    Amal   *****************************************

def Software(request):
    return render(request,'Software.html')

def Staff_index(request):
    return render(request,'Staff_index.html')
    
def Staff_dashboard(request):
    return render(request,'Staff_dashboard.html')

def Staff_accsetting(request):
    return render(request,'Staff_accsetting.html')

def Staff_accsettingimagechange(request,id):
    return render(request, 'Staff_accsetting.html')
    
def Staff_changepwd(request):
    return render(request, 'Staff_changepwd.html')

def Staff_attendance(request):
    return render(request, 'Staff_attendance.html')
    
def Staff_attendancesort(request):
    return render(request, 'Staff_attendancesort.html')

def Staff_reportissues(request):
    return render(request,'Staff_reportissues.html')
    
def Staff_reportedissue(request):
    return render(request,'Staff_reportedissue.html')
    
def Staff_reportanissue(request):
    return render(request,'Staff_reportanissue.html')

def Staff_issuereportsstudents(request):
    return render(request,'Staff_issuereportsstudents.html')
    
def Staffreplyview(request):
    return render(request, 'Staffreplyview.html')
    
def Staffissuereply(request):
    return redirect('Staff_reportissues')

#**************************************    Subeesh   *****************************************

def Staff_leave(request):
    return render(request, 'Staff_leave.html')

def Staff_Student_det(request):
    return render(request, 'Staff_Student_det.html')

def Staff_apply_leave(request):
    return render(request, 'Staff_apply_leave.html')

def Staff_Req_leave(request):
    return render(request, 'Staff_Req_leave.html')

# def Student_profiledash(request):
#     return render(request, 'Student_profiledash.html')

def Staff_studentsleave_table(request):
    return render(request, 'Staff_studentsleave_table.html')

def Staff_current_students(request):
    return render(request, 'Staff_current_students.html')

def Staff_student_dashboard(request):
    return render(request, 'Staff_student_dashboard.html')


def Staff_previous_students(request):
    return render(request, 'Staff_previous_students.html')

def Staff_previous_student_dashboard(request):
    return render(request, 'Staff_previous_student_dashboard.html')

def Staff_progress_det(request):
    return render(request, 'Staff_progress_det.html')

def Staff_progress_report(request):
    return render(request, 'Staff_progress_report.html')
    
def Staff_progress_report_show(request):
    return render(request, 'Staff_progresss_report.html')


def Staff_progress_report_table(request):
    return render(request, 'Staff_progress_report_table.html')

   

#**************************************Student module*****************************************
#**************************************   Akhil & Anwar   ************************************

def Student_index(request):
    return render(request,'Student_index.html')

def Student_applyleave_cards(request):
    return render(request,'Student_applyleave_cards.html')

def Student_leavereq(request):
    return render(request,'Student_leavereq.html')   

def Student_reqedleave(request):
    return render(request, 'Student_reqedleave.html') 

def Student_leaverejected(request):
    return render(request, 'Student_leaverejected.html') 

def Student_progressreport(request):
    return render(request,'Student_progressreport.html')
   

# anwar student module


def Student_accsetting(request):
    return render(request,'Student_accsetting.html')
    
def Student_accsettingimagechange(request,id):
    return render(request, 'Student_accsetting.html')
   
def Student_changepwd(request):
    return render(request, 'Student_changepwd.html',)

def Student_profiledash(request):
    return render(request, 'Student_profiledash.html')

def Student_attendance(request):
    return render(request, 'Student_attendance.html')

def Student_attendancesort(request):
    return render(request, 'Student_attendancesort.html')

def Student_reportissues(request):
    return render(request, 'Student_reportissues.html')

def Studentreportsuccess(request):
    return render(request, 'Student_reportissues.html')

def Student_reportissue1(request):
    return render(request, 'Student_reportissue1.html')

def Student_reportissue2(request):
    return render(request, 'Student_reportissue2.html')

def Student_reportissuereply(request):
    return render(request, 'Student_reportissuereply.html')


#**************************************Manager module*****************************************

#-------------------Sharon--------------------

def Man_index(request):  
    return render(request, 'Man_index.html')

def MAN_profile(request):
    return render(request, 'MAN_profile.html') 

def MAN_accsetting(request):
    return render(request,'MAN_accsetting.html')

def MAN_accsettingimagechange(request):
    return render(request, 'MAN_accsetting.html')

def MAN_changepwd(request):
    return render(request,'MAN_changepwd.html')

def MAN_registration(request):
    return render(request,"MAN_registration.html") 
    
def MAN_registrationstaff(request):
    return render(request,"MAN_registrationstaff.html")

def MAN_currentstaff(request):
    return render(request,"MAN_currentstaff.html") 

def MAN_resignedstaff(request):
    return render(request,"MAN_currentstaff.html")

def MAN_registrationstudent(request):
    return render(request,"MAN_registrationstudent.html") 

def MAN_currentstudent(request):
    return render(request,"MAN_currentstudent.html") 

def MAN_resignedstudent(request):
    return render(request,"MAN_resignedstudent.html")

def MAN_addbatch(request):
    return render(request,"MAN_addbatch.html")

#------------------Meenu-----------------#

def Manager_staff(request):
    return render(request,'Manager_staff.html')

def Manager_currentstaffdetails(request):
    return render(request,'Manager_currentstaffdetails.html')

def Manager_previousstaffdetails(request):
    return render(request,'Manager_previousstaffdetails.html')

def Manager_staffprofile(request):
    return render(request,'Manager_staffprofile.html')

def Manager_attendancesearch(request):
    return render(request,'Manager_attendancesearch.html')

def Manager_attendancesort(request):
    return render(request,'Manager_attendancesort.html')
    
def Manager_performance_report(request):
    return render(request,'Manager_performanceReport.html')

def Manager_student(request):
    return render(request,'Manager_student.html')

def Manager_currentstudentdetails(request):
    return render(request,'Manager_currentstudentdetails.html')

def Manager_previousstudentdetails(request):
    return render(request,'Manager_previousstudentdetails.html')

def Manager_studentprofile(request):
    return render(request,'Manager_studentprofile.html')

def Manager_student_attendancesearch(request):
    return render(request,'Manager_studentattendancesearch.html')

def Manager_sort(request):
    return render(request,'Manager_studentattendancesort.html')

def Manager_leaverequest_staff(request):
    return render(request,'Manager_leaverequest_staff.html')

def Manager_apply_leave(request):
    return render(request, 'Manager_applyleave.html')

def Manager_requestleave(request):
    return render(request,'Manager_requestleave.html')
    
def Manager_staffleave(request):
    return render(request,'Manager_staffleave.html')


def Manager_rejected_leave(request,):
    return redirect('Manager_staffleave')

def Manager_accepted_leave(request):
    return redirect('Manager_staffleave')

def Manager_academics(request):
    return render(request,'Manager_academics.html')


def Manager_Academics_batch(request):
    return render(request,'Manager_Academics_Batch.html')

def Manager_academics_viewbatch(request):
    return render(request,'Manager_academics_viewbatch.html')


def Manager_academics_update(request):
    return render(request,'Manager_academics_update.html')


def Manager_academics_updatesave(request):
    return render(request,'Manager_academics_update.html')


def Manager_academics_delete(request):
    return redirect('/Manager_academics_viewbatch')

#---------------------NIMISHA----------------#

def Manager_academics_class(request):
    return render(request,'Manager_academics_class.html')

def Manager_ViewClass(request):
    return render(request,'Manager_ViewClass.html')

def Manager_UpdateClass(request):
    return render(request,'Manager_UpdateClass.html')

#--------------anandhu------------#

def MAN_AcademicAddClass(request):
    return render(request, 'Manager_academics_AddClass.html')

#-----------Akhil P T--------------#
def MAN_Report(request):
    return render(request,'MAN_Report.html')

def MAN_ReportedissueShow(request):
    return render(request,'MAN_ReportedissueShow.html')

def MAN_ReportedissueShow1(request):
    return render(request,'MAN_ReportedissueShow1.html')

def MAN_ReportedissueShowstaff(request):
    return render(request,'MAN_ReportedissueShowstaff.html')

def MAN_ReportedissueShow1staff(request):
    return render(request,'MAN_ReportedissueShow1staff.html')


def MAN_manager_report(request):
    return render(request,'MAN_manager_report.html')


def MAN_Reportissue(request):
    return render(request,'MAN_Reportissue.html')

def MAN_reportsuccess(request):
    return render(request, 'MAN_Reportissue.html')
    

def MAN_manger_reportedissues(request):
    return render(request,'MAN_manger_reportedissues.html')

def MAN_manger_reportedissues1(request):
    return render(request,'MAN_manger_reportedissues1.html')

#----------Subeesh----------------
def MAN_subjects(request):
    return render(request, 'Manager_subject.html')

def MAN_Viewsubject(request):
    return render(request, 'Manager_Viewsubject.html')

def MAN_Updatesubject(request):
    return render(request, 'Manager_Updatesubject.html')

#----------------Anwar-------------#
def Man_AddSubject(request):
    return render(request,'Manager_AddSubject.html')

    
#**************************************Account module*****************************************
#**************************************     Praveen   ****************************************
def Account_Student_det(request):
       
    return render(request, 'Account_Student_det.html')

def Account_previous_students(request):
  
    return render(request, 'Account_previous_students.html')

def Acc_index(request):
  
    return render(request, 'Acc_index.html')

def Account_dashboard(request):
      
    return render(request, 'Account_dashboard.html')

# sharon

def acc_issue(request):
    return render(request,"acc_issue.html")

def acc_reportedissue(request):
    return render(request,"acc_reportedissue.html")

def acc_report_an_issue(request):
    return render(request,"acc_report_an_issue.html")

def account_issuereply(request):
    return render(request,"account_issuereply.html")

def acc_leaverequest(request):
    return render(request,"acc_leaverequest.html")

def acc_applyleave(request):
    return render(request,"acc_applyleave.html")

def acc_requestedleave(request):
    return render(request,"acc_requestedleave.html")



#*********************************Admin module*************************************

def Admin_index(request):
    return render(request,'Admin_index.html')

#----------------Academic------------------
def Admin_Academic(request):
    return render(request,'Admin_Academic.html')

def Admin_Academic_Class(request):
    return render(request,'Admin_Academic_Class.html')

def Admin_Academic_AddClass(request):
    return render(request,'Admin_Academic_AddClass.html')

def Admin_Academic_ViewClass(request):
    return render(request,'Admin_Academic_ViewClass.html')

def Admin_Academic_UpdateClass(request):
    return render(request,'Admin_Academic_UpdateClass.html')

def Admin_Academic_Subject(request):
    return render(request,'Admin_Academic_Subject.html')

def Admin_Academic_AddSubject(request):
    return render(request,'Admin_Academic_AddSubject.html')

def Admin_Academic_ViewSubject(request):
    return render(request,'Admin_Academic_ViewSubject.html')

def Admin_Academic_UpdateSubject(request):
    return render(request,'Admin_Academic_UpdateSubject.html')

#----------------Attendance------------------
def Admin_Attendance(request):
    return render(request,'Admin_Attendance.html')

def Admin_Attendance_Show(request):
    return render(request,'Admin_AttendanceShow.html')

#----------------Reportedissues------------------
def Admin_Reportedissues_Card(request):
    return render(request,'Admin_Reportedissues_Card.html')

def Admin_Reportedissues_Show(request):
    return render(request,'Admin_Reportedissues_Show.html')

def Admin_Reportedissues(request):
    return render(request,'Admin_Reportedissues.html')

def Admin_ManagerReportedissues(request):
    return render(request,'Admin_ManagerReportedissues.html')

#----------------LeaveRequest------------------
def Admin_LeaveRequest(request):
    return render(request,'Admin_LeaveRequest.html')

def Admin_LeaveRejected(request):
    return render(request,'Admin_LeaveRejected.html')

#----------------Dashboard------------------
def Admin_dashboard(request):
    return render(request,'Admin_dashboard.html')

def superadmin_changepwd(request):
    return render(request, 'Admin_changepassword.html')

#----------------Academic Batch------------------

def AcademicBatch_Admin(request):     
    return render(request, 'AcademicBatch_Admin.html')

def AcademicAddBatch_Admin(request):
    return render(request, 'AcademicAddBatch_Admin.html') 

def AcademicAddBatch_Adminsave(request):   
    return render(request, 'AcademicAddBatch_Admin.html') 

def AcademicAddBatchUpdate_Admin(request):      
    return render(request, 'AcademicAddBatchUpdate_Admin.html') 

def AcademicAddBatchUpdate_Adminsave(request):     
    return render(request,'AcademicAddBatch_Admin.html')

def AcademicViewBatch_Admin(request):     
    return render(request, 'AcademicViewBatch_Admin.html')

def AcademicAddBatch_Admindelete(request):    
    return render(request,'AcademicViewBatch_Admin.html')

#----------------Registration------------------

def Registration_Admin(request):     
    return render(request, 'Registration_Admin.html')    

def RegistrationStaff_Admin(request):  
    return render(request, 'RegistrationStaff_Admin.html')      

def RegistrationStudent_Admin(request):  
    return render(request, 'RegistrationStudent_Admin.html')       

def RegistrationCurrentStaff_Admin(request):  
    return render(request, 'RegistrationCurrentStaff_Admin.html')  

def RegistrationCurrentStaff_Adminsave(request):
    return redirect('RegistrationCurrentStaff_Admin')

def RegistrationCurrentStaffAdmin_update(request):
    return render(request,'RegistrationCurrentStaffAdmin_update.html')

def RegistrationCurrentStaffAdmin_updatessave(request):
    return render(request,'RegistrationCurrentStaff_Admin.html')
    
def RegistrationCurrentStaffAdmin_delete(request): 
    return redirect('RegistrationCurrentStaff_Admin')

def RegistrationResignedStaff_Admin(request):   
    return render(request, 'RegistrationResignedStaff_Admin.html')  

def RegistrationResignedStaffAdmin_update(request):    
    return render(request,'RegistrationResignedStaffAdmin_update.html')

def RegistrationResignedStaffAdmin_updatessave(request):
    return redirect('RegistrationResignedStaff_Admin')

def RegistrationResignedStaffAdmin_delete(request):
    return redirect('RegistrationResignedStaff_Admin')

def RegistrationCurrentStudent_Admin(request):
    return render(request, 'RegistrationCurrentStudent_Admin.html')     

def RegistrationCurrentStudent_Adminsave(request): 
    return redirect('RegistrationCurrentStudent_Admin')

def RegistrationCurrentStudentAdmin_update(request):        
    return render(request,'RegistrationCurrentStudentAdmin_update.html')
    
def RegistrationCurrentStudent_updatessave(request):   
    return redirect('RegistrationCurrentStudent_Admin')

def RegistrationCurrentStudentAdmin_delete(request):
    return redirect('RegistrationCurrentStudent_Admin')

def RegistrationPreviousstudent_Admin(request):  
    return render(request, 'RegistrationPreviousstudent_Admin.html')                              

def RegistrationPreviousstudentAdmin_update(request):    
    return render(request,'RegistrationPreviousstudentAdmin_update.html')

def RegistrationPreviousstudentAdmin_updatessave(request):
    return redirect('RegistrationPreviousstudent_Admin')

def RegistrationPreviousstudentAdmin_delete(request):
    return redirect('RegistrationPreviousstudent_Admin')

#----------------Staff------------------

def Staff_Admin(request):  
    return render(request, 'Staff_Admin.html') 

def StaffCurrentstaff_Admin(request):  
    return render(request, 'StaffCurrentstaff_Admin.html') 

def StaffPreviousstaff_Admin(request):  
    return render(request, 'StaffPreviousstaff_Admin.html') 

def StaffCurrentstaffProfile_Admin(request):  
    return render(request, 'StaffCurrentstaffProfile_Admin.html') 

def StaffPreviousstaffProfile_Admin(request):      
    return render(request, 'StaffPreviousstaffProfile_Admin.html') 

def StaffCurrentstaffAttendance_Admin(request):
    return render(request, 'StaffCurrentstaffAttendance_Admin.html')  

def StaffCurrentstaffAttendanceSort_Admin(request):
    return render(request,'StaffCurrentstaffAttendanceSort_Admin.html') 

def StaffCurrentstaffPerformance_Admin(request):      
    return render(request,'StaffCurrentstaffPerformance_Admin.html')

def StaffCurrentstaffPerformance_Adminsave(request):    
    return render(request,'StaffCurrentstaffPerformance_Admin.html')

def StaffPreviousstaffAttendance_Admin(request):  
    return render(request, 'StaffPreviousstaffAttendance_Admin.html')  

def StaffPreviousstaffAttendanceSort_Admin(request):  
    return render(request,'StaffPreviousstaffAttendanceSort_Admin.html')

def StaffPreviousstaffPerformance_Admin(request):  
    return render(request,'StaffPreviousstaffPerformance_Admin.html')

def StaffPreviousstaffPerformance_Adminsave(request): 
    return render(request,'StaffPreviousstaffPerformance_Admin.html')  

#----------------Student------------------

def Student_Admin(request):     
    return render(request, 'Student_Admin.html') 

def StudentCurrentstudent_Admin(request):  
    return render(request, 'StudentCurrentstudent_Admin.html') 

def StudentPreviousstudent_Admin(request):  
    return render(request, 'StudentPreviousstudent_Admin.html') 

def StudentCurrentstudentProfile_Admin(request):  
    return render(request, 'StudentCurrentstudentProfile_Admin.html')

def StudentPreviousstudentProfile_Admin(request):  
    return render(request, 'StudentPreviousstudentProfile_Admin.html')

def StudentCurrentstudentAttendance_Admin(request):
    return render(request, 'StudentCurrentstudentAttendance_Admin.html') 

def StudentCurrentstudentAttendanceSort_Admin(request):  
    return render(request,'StudentCurrentstudentAttendanceSort_Admin.html')

def StudentCurrentstudentPerformance_Admin(request):
    return render(request,'StudentCurrentstudentPerformance_Admin.html')

def StudentCurrentstudentPerformance_Adminsave(request):    
    return render(request,'StudentCurrentstudentPerformance_Admin.html')

def StudentPreviousstudentAttendance_Admin(request):     
    return render(request, 'StudentPreviousstudentAttendance_Admin.html')
      
def StudentPreviousstudentAttendanceSort_Admin(request):      
    return render(request,'StudentPreviousstudentAttendanceSort_Admin.html')        

def StudentPreviousstudentPerformance_Admin(request):     
    return render(request,'StudentPreviousstudentPerformance_Admin.html')

def StudentPreviousstudentPerformance_Adminsave(request):     
    return render(request,'StudentPreviousstudentPerformance_Admin.html')