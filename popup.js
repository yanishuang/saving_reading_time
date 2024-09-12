document.addEventListener('DOMContentLoaded', () => {
  chrome.storage.local.get(['selectedText'], (result) => {
    document.getElementById('selectedText').textContent = result.selectedText || '没有选中的文本';
    // 清除标记
    chrome.action.setBadgeText({ text: "" });
  });

  document.getElementById('summaryButton').addEventListener('click', () => {
    chrome.storage.local.get(['selectedText'], (result) => {
      if (result.selectedText) {
        document.getElementById('summaryResult').textContent = '正在归纳...';
        fetch('http://127.0.0.1:5000/summary.json', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: result.selectedText }),
        })
        .then(response => response.json())
        .then(data => {
          document.getElementById('summaryResult').innerHTML = '<span class="icon">✨</span>归纳结果: ' + data.summary;
        })
        .catch((error) => {
          console.error('Error:', error);
          document.getElementById('summaryResult').innerHTML = '<span class="icon">❗</span>归纳失败，请检查服务器是否正常运行。';
        });
      } else {
        document.getElementById('summaryResult').innerHTML = '<span class="icon">🤔</span>没有可归纳的内容。';
      }
    });
  });
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "openPopup") {
    chrome.action.openPopup();
  }
});