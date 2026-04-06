from flask import Flask, jsonify, request
import sys
import random


app = Flask(__name__)

@app.route('/inquiry', methods=["GET", "POST"])
def index():
    # 사용자 발화 가져오기
    body = request.get_json(silent=True) or {}
    user_text = ""
    try:
        user_text = body["userRequest"]["utterance"]
    except:
        pass

    # 응답 메시지 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕하세요! 문의해 주셔서 감사합니다 😊\n잠재고객 확보가 어려우셨나요?\n저희가 함께합니다!"
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
