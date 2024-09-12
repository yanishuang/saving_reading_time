from flask import Flask, request, jsonify
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/summary.json', methods=['POST'])
def summarize():
    try:
        # 记录客户端上报的所有内容
        logger.info(f"Received request data: {request.json}")

        # 获取POST请求中的文本
        text = request.json.get('text', '')
        
        # 这里应该是您的文本摘要逻辑
        # 为了示例,我们简单地返回文本的前50个字符作为"摘要"
        summary = text[:50] + '...' if len(text) > 50 else text
        
        # 记录处理结果
        logger.info(f"Generated summary: {summary}")

        # 返回JSON格式的响应
        return jsonify({'summary': summary})
    except Exception as e:
        # 记录异常信息
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)