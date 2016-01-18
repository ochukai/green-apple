## add message
output
```json
{
  "next_need_amount": 0,
  "next_status_code": 100,
  "message_pk": {
    "pk": 211,
    "create_time": "2016-01-12T18:58:04",
    "ts": 1452596284
  },
  "charge_amount": 0,
  "remain_free_message_count": 3,
  "mpk": "msg_211",
  "ts": 1452596284
}


{
  "next_status_code": 401,
  "next_need_amount": 5,
  "send_give_message": true,
  "mpk": "msg_216",
  "ts": 1452658266,
  "message_pk": {
    "pk": 216,
    "create_time": "2016-01-13T12:11:06",
    "ts": 1452658266
  },
  "charge_amount": 0,
  "remain_free_message_count": 0
}
```
---
## 患者获取剩余免费信息条数

> GET /doctors/<doctor_id>/message_charge/free_message_count/

### input:
> patient_pk: ``<int>``

### output
```json
{
    "free_message_count": 3 ,
}
```

---

## 医生赠送患者免费消息

>POST /doctors/<doctor_id>/message_charge/free_message_count/


### input

> patient_pk: ``<int>``

### output

```json

{
    "mpk": ,
    "actual_sender": ,
    "from_user": ,
    "to_user":  ,
    "type": , // SYS
    "text": ,
    "ts": ,
}

{
  "objects": [
    {
      "text": "祁芸芸医生赠送了3条免费消息",
      "actual_sender": "doc_29279",
      "ts": 1452595856,
      "mpk": "msg_28ce43e6-f356-4c19-8184-8aca31831ebe",
      "to_user": "pat_1",
      "data": null,
      "from_user": "doc_29279",
      "type": "SYS"
    }
  ]
}
```

## Check

### output
```json
{
  "status_code": 100,
  "need_amount": 0
}
```
---
## V2
```js
{
  // ...
  “data“: "{\"next_status_code\": 101, \"next_need_amount\": 0, \"charge_amount\": 0, \"remain_free_message_count\": 2}"  
  // ...
}

```
