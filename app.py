from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/text', methods=["GET", "POST"])
def text_skill():
    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": str(random.randint(1, 10))
                }
            }]
        }
    })

@app.route('/image', methods=["GET", "POST"])
def image_skill():
    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleImage": {
                    "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                    "altText": "hello I'm Ryan"
                }
            }]
        }
    })

@app.route('/inquiry', methods=["GET", "POST"])
def inquiry():
    body = request.get_json(silent=True) or {}
    user_text = ""
    try:
        user_text = body["userRequest"]["utterance"]
    except:
        pass

    if "채팅상담" in user_text:
        text = "상담사를 연결 중입니다. 잠시만 기다려주세요! 🙏"
    elif "견적서" in user_text:
        text = "견적서 요청을 접수했습니다.\n담당자가 곧 연락드릴게요 📄"
    elif "도입 문의" in user_text:
        text = "도입 문의 감사합니다!\n어떤 서비스에 관심 있으신가요? 🏢"
    else:
        text = "안녕하세요! 문의해 주셔서 감사합니다 😊\n잠재고객 확보가 어려우셨나요?\n저희가 함께합니다!"

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "채팅상담 요청",
                    "action": "message",
                    "messageText": "채팅상담 요청"
                },
                {
                    "label": "견적서 요청",
                    "action": "message",
                    "messageText": "견적서 요청"
                },
                {
                    "label": "도입 문의",
                    "action": "message",
                    "messageText": "도입 문의"
                }
            ]
        }
    }
    return jsonify(response)  # ✅ 여기가 핵심!

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # ✅ 맨 마지막에 한 번만
