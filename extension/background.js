let location = 'Workplace';

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ location });
  console.log(`Default workplace location set to ${location}`);
});