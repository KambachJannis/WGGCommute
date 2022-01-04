function handleButtonClick(event) {
  let location = document.getElementById("location").value;
  chrome.storage.sync.set({ location });
}

function constructPage() {
  document.getElementById("update").addEventListener("click", handleButtonClick);
  chrome.storage.sync.get("location", ({location}) => {
    document.getElementById("location").value = location;
  });
}

constructPage();