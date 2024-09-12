from flask import Flask, request, jsonify
from models import summarize_with_gpt4

# 配置日志
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/summary.json', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        summary = summarize_with_gpt4(text, max_length=200)
        return jsonify({
            'summary': summary,
            'model_used': 'gpt4'
        })
    except Exception as e:
        logger.error(f"Error during summarization: {str(e)}")
        return jsonify({'error': 'An error occurred during summarization'}), 500

if __name__ == '__main__':
    app.run(debug=True)