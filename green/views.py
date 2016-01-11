# -*- coding: UTF-8 -*-
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from backend.models import Patient, Doctor
from backend.services import friendship_service
from backend.utils.shortcuts import GetFileAbsoluteURL
from wap.decorators import need_wechat_oauth_login
from wap.views import generate_js_sdk_params


@need_wechat_oauth_login(require_patient=True)
def get_followers(request):
    wx_open_id = request.session.get('wx_open_id', None)
    patient = Patient.objects.filter(wx_openid=wx_open_id).first()
    return render(request, 'wxchat/list.html', {
        'debug': settings.DEBUG,
        'js_api_param': generate_js_sdk_params(request),
        'patient_id': patient.id
        'patient_id': 5
    })


@need_wechat_oauth_login(require_patient=True)
def chat_conversation(request):
    wx_open_id = request.session.get('wx_open_id', None)
    patient = Patient.objects.filter(wx_openid=wx_open_id).first()

    doctor_id = request.GET.get('doctor_id')
    doctor = get_object_or_404(Doctor, id=doctor_id)
    friendship_service.follow_doctor_if_has_not_followed(doctor, patient)

    doctor_data = {
        'pk': doctor_id,
        'name': doctor.real_name,
        'hospital': doctor.hospital.name if (doctor and doctor.hospital) else None
    }

    if doctor.specialty is not None:
        doctor_data['specialty'] = doctor.specialty.name if (doctor and doctor.specialty) else None
    if doctor.department is not None:
        doctor_data['department'] = doctor.department.name if (doctor and doctor.department) else None
    if doctor.header_pic:
        doctor_data['pic_url'] = GetFileAbsoluteURL(doctor.header_pic.url, request)

    # TODO add patient pic url
    return render(request, 'wxchat/chat.html', {
        'debug': settings.DEBUG,
        'js_api_param': generate_js_sdk_params(request),
        'patient_id': patient.id,
        # 'patient_id': 5,
        'doctor': doctor_data,
    })
