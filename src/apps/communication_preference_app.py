from flask import Flask, request, jsonify

app = Flask(__name__)

preferences = [
    {"cafe_id": "1A88EBA6-5798-452D-AEA6-21103DF73A38", "data":
        {
            "collectedAt": 1759282811,
            "topics": {
                "exclusive_events": {
                    "email": {
                        "status": "granted"
                    },
                    "push": {
                        "status": "granted"
                    },
                    "sms": {
                        "status": "denied"
                    }
                }
            }
        }
     },
    {"cafe_id": "7A70AFDE-10F3-4872-8249-205BD4F01201", "data":
        {
        "collectedAt": 1759282811,
        "topics": {
            "newsletters": {
                "email": {
                    "status": "denied"
                },
                "push": {
                    "status": "granted"
                },
                "sms": {
                    "status": "granted"
                }
            }
        }
        }
     },
    {"cafe_id": "C81C4D4E-19FE-47EF-BDE4-7460A70AF23C", "data":
        {
        "collectedAt": 1759282811,
        "topics": {
            "newsletters": {
                "email": {
                    "status": "granted"
                },
                "push": {
                    "status": "granted"
                },
                "sms": {
                    "status": "granted"
                }
            }
        }
        }
     }
]


@app.route('/preferences/<cafe_id>', methods=['GET'])
def get_preferences(cafe_id):
    if not cafe_id:
        return jsonify({"error": "Email query parameter is required"}), 400

    preference = next((u for u in preferences if u['cafe_id'].lower() == cafe_id.lower()), None)
    if preference:
        return jsonify({"preference": preference['data']})
    else:
        return jsonify({"error": "Preferences not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
