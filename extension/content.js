function processData(data, domElements, addresses, target) {
    console.log(data)
    messages = data['body']['messages']
    for (let i = 0; i < domElements.length; i++) {
        domElements[i].innerText = `${domElements[i].innerText} | Fastest commute from ${addresses[i]} to ${target}: ${messages[i]}`;
    }
}

function main(target){
    const city = document.getElementById("autocompinp").value;
    const domElements = document.querySelectorAll('.col-xs-11');
    let addresses = [];
    for (let i = 0; i < domElements.length; i++) {
        let text = domElements[i].innerText;
        let textarray = text.split(' | ');
        addresses.push(textarray[2]);
    }
    console.log(addresses);
    fetch("https://lambda.api", {method: 'POST', body: JSON.stringify({"add": addresses,"tgt": target,"city": city,"modes": ["driving", "bicycling", "transit"]})})
        .then((response) => response.text())
        .then((result) => {
            data = JSON.parse(result);
            processData(data, domElements, addresses, target);
        })
        .catch((error) => console.log("error", error));
}

chrome.storage.sync.get("location", ({ location }) => {
    console.log(location);
    main(location);
});

