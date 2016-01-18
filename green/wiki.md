## doctor list
* id
* name
* department
* pic_url
* last_message_pk
* last_message_text
* last_message_date

```sql
SELECT
  "broadcast"."id",
  "broadcast"."create_time",
  "broadcast"."doctor_id",
  "broadcast"."text",
  "broadcast"."tag_id",
  "broadcast"."sent_tag_name",
  "broadcast"."sent_count",
  "broadcast"."doctor_disease_id",
  "broadcast"."sent_disease_name",
  "broadcast"."browse_count",
  "broadcast"."category",
  "broadcast"."source_url",
  "broadcast"."content",
  "broadcast"."is_created_by_internal_user",
  "broadcast"."pub_status",
  "broadcast"."is_deleted"
FROM "broadcast"
WHERE
(
  "broadcast"."tag_id" IS NULL
  AND "broadcast"."is_deleted" = False  
  AND "broadcast"."doctor_id" = 41118
)

ORDER BY "broadcast"."id" DESC  


```
url:
> /patients/`<patient_id>`/followings/

method: `GET`

input (不变):
output:
```json
{
    "following_list":
    [
        {
            "hospital": "上海中山医院",
            "ts": 1441863520,
            "doctor_name": "将家家户户",
            "medal_list":
            [
                {
                    "category": "message",
                    "level": 1
                }
            ],
            "department": "骨科",
            "pk": 300846,

            "doctor_pic_url": '',   # 医生头像
            "last_message_pk": '',   # 最近消息的id
            "last_message_text": '',   # 最近消息的text
            "last_message_time": ''      # 最近消息的时间
        }
    ]
}
```

---
## messaeges
url:
> patients/`<id>`/messages/v2/

method: `GET`

output
```json
{
  objects: [
  {
      actual_sender: pat_<patient_id>.
      from_user: pat_<patient_id>.
      to_user: doc_<doctor_id>,
      mpk: msg_21,
      type: 'TXT'
      text: hello
      data:{
        charge_amount: <int>
      }
      ts: 1442646936,
  }，

  {
      actual_sender: pat_<patient_id>,
      from_user: pat_<patient_id>,
      to_user: doc_<doctor_id>,
      mpk: msg_21,
      type: 'PIC'，
      text: ［图片］，
      data: {height: 120, width: 120, pic: xxxxx, pic_thumbnail: xxxx }
      ts: 1442646936,
  }，

  {
      actual_sender: pat_<patient_id>.
      from_user: pat_<patient_id>.
      to_user: doc_<doctor_id>,
      mpk: msg_21,
      type: 'TXT'
      text: hello
      ts: 1442646936,
  }，

  {
      actual_sender: pat_<patient_id>.
      from_user: pat_<patient_id>,
      to_user: doc_<doctor_id>,
      mpk: msg_21,
      type: 'VOE'
      text: ［语音］
      data: {'voice': <http_path>}
      ts: 1442646936,
  }，

  {
      actual_sender: pat_<patient_id>,
      from_user: pat_<patient_id>,
      to_user: doc_<doctor_id>,
      mpk: msg_23,
      type: 'GFT'
      text: ［礼物］
      data: {'amount': 10}
      ts: 1442646936,
  }，

  // 患者收到医生收到礼物的提示  
  {
      actual_sender: doc_<doctor_id>,
      from_user: doc_<doctor_id>,
      to_user: pat_<patient_id>,
      mpk: msg_25,
      type: 'GFT'
      text: ［礼物］
      data: { 'amount': 10 }
      ts: 1442646936,
  },

  // 患者收到医生的broadcast
  {
      actual_sender: doc_<doctor_id>,
      from_user: doc_<doctor_id>,
      to_user: pat_<patient_id>,
      mpk: brc_1,
      type: 'ART'         //文章
      data: {
          title:xxx,
          summary: xxx,  
          pics: [xxxxx, xxxx, xxx],
          is_complete:true
      }
      text: ‘[文章]’
      ts: 1442646936,
  }，

  // 患者收到医生的broadcast
  {
      "actual_sender": "doc_<doctor_id>",
      "from_user": "doc_<doctor_id>",
      "to_user": "pat_<patient_id>",
      "mpk": "brc_1",
      "type": "TXT",
      "text": "[通知]",
      "data": "",
      "ts": 1442646936,
  }


  // 患者收到医生单发的文章
  {
     actual_sender: doc_<doctor_id>,
     from_user: doc_<doctor_id>,
     to_user: pat_<patient_id>,
     mpk: msg_12,
     type: 'ART'         //文章
     data: {
         pk:102,
         article_url:'xxxxxxx',
         title:xxx,
         summary: xxx,  
         pics: [xxxxx, xxxx, xxx],
         is_complete:true
     }   //其中pk是 对应broadcast的pk
     text:   ‘[文章]’
     ts: 1442646236,
  }]
}
```
or

```http
HttpBadRequest 400
```

字段说明
```

actual_sender：可为：patient(pat)，doctor(doc)，grm（group member）  

from_user:  发出消息的位置，可为 doctor(doc)，patient(pat)， gourp chat(grp)

type: GIF, TXT, VOE, ART, PIC, SYS

mpk 前缀可为：msg（message），brc（broadcast），grp（group message）

注：Notice 沿用原来的接口 `doctors/<id>/notice` or `patients/<id>/notice`
```


```json

{
  "objects": [
    {
      "text": "ksdfjk",
      "actual_sender": "doc_304752",
      "ts": 1451378018,
      "mpk": "msg_3190715",
      "to_user": "pat_425515",
      "data": null,
      "from_user": "doc_304752",
      "type": "TXT"
    },
    {
      "text": "sdfs[鼓掌][惊恐]",
      "actual_sender": "doc_304752",
      "ts": 1451378043,
      "mpk": "msg_3190716",
      "to_user": "pat_425515",
      "data": null,
      "from_user": "doc_304752",
      "type": "TXT"
    },
    {
      "text": "[图片]",
      "actual_sender": "doc_304752",
      "ts": 1451378198,
      "mpk": "msg_3190717",
      "to_user": "pat_425515",
      "data": "{\"pic_thumbnail\": \"http://kkhgreenrel.u.qiniudn.com/messagepic/2015_12_29/4697f058ae0711e5a11b00163e001de1.png?imageMogr2/auto-orient/thumbnail/160x90/quality/100/&e=1451983002&token=5R-0cD4dr1uY-iKcNKHjNLFJL3wxk5_w0v-jy4-6:nWES_Jzr6RgfcolEsU-xBoixrdI=\", \"origin_size\": {\"width\": 391, \"height\": 692}, \"height\": 90, \"pic\": \"http://kkhgreenrel.u.qiniudn.com/messagepic/2015_12_29/4697f058ae0711e5a11b00163e001de1.png?e=1451983002&token=5R-0cD4dr1uY-iKcNKHjNLFJL3wxk5_w0v-jy4-6:D2YfKtO0YDXHqNN4ESr3yp3RPmE=\", \"width\": 50}",
      "from_user": "doc_304752",
      "type": "PIC"
    }
  ]
}
```

---


## last messages


---

## add messages

url:
> patients/`<id>`/add_message/

method: `POST`

input

```json
// 文本
{
    type: TXT,
    to_user: doc_<doctor_id>,
    text: '这个是怎么回事'
}


// 图片
{
    type: PIC,
    to_user: doc_<doctor_id>,
    file: <图片文件>
}

// 礼物
{
    type: GIF,
    to_user: doc_<doctor_id>,
    amount: 10
}


// 文本 (VIP发消息)
{
    type: TXT,
    to_user: doc_<doctor_id>,
    text:  '这个是怎么回事',
    from_vip: 1
}
```

output

```
{
  mpk:  msg_2,
  ts: 150342423490
  next_status_code: 100/101/400...
  next_need_amount: 0/5/10...
}
```
---

## history messages
```json
{
    "meta":{
        "has_next_page": true // false
    },
    "objects":[{
        "status": "8",
        "to_id": 41108,
        "text": "hello",
        "from_user": "pat_12",
        "mpk": "msg_483",
        "from_type": "PAT",
        "ts": 1392800412,
        "to_user": "doc_41108",
        "to_type": "DOC",
        "create_time": "2014-02-19T17:00:12",
        "data": "",
        "actual_sender": "pat_12",
        "pk": 483,
        "type": "TXT",
        "conv_pk": 15,
        "from_id": 12
    }]
}
```

> http://0.0.0.0:8000/wap/articles/16/
