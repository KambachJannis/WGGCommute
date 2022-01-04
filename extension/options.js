function handleButtonUpdate(event) {
  let location = document.getElementById("location").value;
  chrome.storage.sync.set({ location });
}

function handleButtonAPISave(event) {
  let api = document.getElementById("api").value;
  chrome.storage.sync.set({ api });
}

function constructPage() {
  document.getElementById("update").addEventListener("click", handleButtonUpdate);
  document.getElementById("save").addEventListener("click", handleButtonAPISave);
  chrome.storage.sync.get("location", ({location}) => {
    document.getElementById("location").value = location;
  });
}

constructPage();