## Apple Message - `data`

```json
// [礼物已退回]
// from_user_type always 'DOC'
{
    // 未及时回复，错过了10个青苹果。
    "system_message_content": "\u672a\u53ca\u65f6\u56de\u590d\uff0c\u9519\u8fc7\u4e8610\u4e2a\u9752\u82f9\u679c\u3002", 
    "gift_transaction_list": [
        {
            "gift_name": "\u9752\u82f9\u679c", 
            "gift_id": 1, 
            "gift_amount": 10, 
            "gift_transaction_status": "PEG"
        }
    ], 
    "gift_transaction_status": "RET"
}

// [礼物获取成功]
// from_user_type always 'PAT'
{
    // 您获得了10个青苹果，感谢回复
    "system_message_content": "\u60a8\u83b7\u5f97\u4e8610\u4e2a\u9752\u82f9\u679c\uff0c\u611f\u8c22\u56de\u590d", 
    "gift_transaction_list": [
        {
            "gift_name": "\u9752\u82f9\u679c", 
            "gift_id": 1, 
            "gift_amount": 10, 
            "gift_transaction_status": "PEG"
        }
    ], 
    "gift_transaction_status": "RCV"
}

// [礼物]
// from_user_type = 'PAT'
{
    // 青苹果
    "gift_name": "\u9752\u82f9\u679c", 
    "gift_expired_ts": 1451329929, 
    "gift_id": 1, 
    "gift_amount": 10, 
    "gift_transaction_status": "PEG"
}

// DOC to KEFU from_user_type = 'DOC'
{
    "gift_name": "\u9752\u82f9\u679c", 
    "gift_id": 1, 
    "gift_amount": 1, 
    "gift_transaction_status": "PEG" // pending. no use for this message
}

{
    "gift_name": "\u9752\u82f9\u679c", 
    "gift_id": 1, 
    "gift_amount": 66
}

```