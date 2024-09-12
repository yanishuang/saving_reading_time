chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "getSelectedText",
    title: "✨ 使用划词助手分析",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "getSelectedText") {
    chrome.storage.local.set({ selectedText: info.selectionText }, () => {
      chrome.action.setBadgeText({ text: "!" });
      chrome.action.setBadgeBackgroundColor({ color: "#FF6B6B" });
    });
  }
});