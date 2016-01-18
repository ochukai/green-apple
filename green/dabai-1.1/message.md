```python

    TEXT = 'TXT'
    VOICE = 'VOE'
    PIC = 'PIC'
    CONTACT = 'CNT'
    ORDER = 'ORD'
    APPOINTMENT = 'APT'
    ARTICLE = 'ART'
    GIFT = 'GFT'
    TRANSFER = 'TSF'
    OTHER = 'OTH'
    SYSTEM = 'SYS'
    SPECIAL_CHARGE_SETTINGS = 'SCS'
    FREE_MESSAGE_PRESENT = 'FMP'
    EVENT = 'EVT'

    MESSAGE_TYPE_CHOICES = (
        (TEXT, u'文本'),
        (VOICE, u'语音'),
        (PIC, u'图片'),
        (CONTACT, u'名片'),
        (ORDER, u'订单'),
        (APPOINTMENT, u'预约'),
        (ARTICLE, u'文章'),
        (GIFT, u'礼物'),
        (TRANSFER, u'转诊'),
        (OTHER, u'医生自定义服务'),
        (SYSTEM, u'系统消息'),
        (SPECIAL_CHARGE_SETTINGS, u'为患者设置特殊收费提示'),
        (FREE_MESSAGE_PRESENT, u'赠送免费消息提示'),
        (EVENT, u'事件'),
    )

    DRAFT = "0"
    SENT = "2"
    DELIVERED = "4"
    READ = "8"

    STATUS_CHOICES = (
        (DRAFT, u'草稿'),
        (SENT, u'已发出'),
        (DELIVERED, u'已送达'),
        (READ, u'已读'),
    )

    # charge_status
    CHARGE_FREE = 'FREE'
    CHARGE_PAID = 'PAID'
    CHARGE_REPLIED = 'REPLIED'
    CHARGE_REFUNDED = 'REFUNDED'

```
