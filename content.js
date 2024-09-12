// 这个文件目前为空,因为我们不需要在页面中注入任何脚本
// 如果将来需要与页面交互,可以在这里添加代码

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "openPopup") {
    chrome.runtime.sendMessage({ action: "openPopup" });
  }
});