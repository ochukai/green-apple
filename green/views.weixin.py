# -*- coding: UTF-8 -*-

import logging

from django.conf import settings
from django.core.files.images import ImageFile
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from backend.models import Patient, Doctor, User, Conversation_Message, Friendship
from backend.services import friendship_service, weixin_service, message_service
from backend.utils.shortcuts import GetFileAbsoluteURL
from wap.decorators import need_wechat_oauth_login
from wap.views import generate_js_sdk_params


# @need_wechat_oauth_login(require_patient=True)
def get_followers(request):
    # wx_open_id = request.session.get('wx_open_id', None)
    # patient = Patient.objects.filter(wx_openid=wx_open_id).first()
    return render(request, 'wxchat/list.html', {
        # 'debug': settings.DEBUG,
        # 'js_api_param': generate_js_sdk_params(request),
        # 'patient_id': patient.id
        'patient_id': 5
    })


# @need_wechat_oauth_login(require_patient=True)
def chat_conversation(request):
    # wx_open_id = request.session.get('wx_open_id', None)
    # patient = Patient.objects.filter(wx_openid=wx_open_id).first()

    doctor_id = request.GET.get('doctor_id')
    doctor = get_object_or_404(Doctor, id=doctor_id)
    # friendship_service.follow_doctor_if_has_not_followed(doctor, patient)
    # Friendship.objects.filter(doctor=doctor, patient=patient).update(is_virtual=False)

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

    # patient_dict = {
    #     'pk': patient.id
    # }
    #
    # if patient.header_pic:
    #     patient_dict['pic_url'] = GetFileAbsoluteURL(patient.header_pic.url, request)

    return render(request, 'wxchat/chat.html', {
        # 'debug': settings.DEBUG,
        # 'js_api_param': generate_js_sdk_params(request),
        # 'patient': patient_dict,
        'patient': { 'pk': 5, 'pic_url': '1234'},
        'doctor': doctor_data,
    })


@require_POST
@csrf_exempt
def send_pic_to_doctor(request, patient_id):
    doctor_id = request.POST.get('doctor_id')
    media_id = request.POST.get('media_id')
    if not media_id:
        return HttpResponseBadRequest()
    doctor = get_object_or_404(Doctor, id=doctor_id)
    patient = get_object_or_404(Patient, id=patient_id)

    try:
        request.file = ImageFile(weixin_service.get_wechat_media_file(media_id))
        return message_service.send_doctor_with_patient_conversation_msg(
                request, User.PATIENT, Conversation_Message.PIC, patient, doctor, from_vip=True)
    except Exception as e:
        logging.warning('wxchat.send_pic_to_doctor, %s', e)
        return HttpResponseBadRequest()


@require_POST
@csrf_exempt
def set_on_weixin_web(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.set_on_weixin_web()
    return HttpResponse()
