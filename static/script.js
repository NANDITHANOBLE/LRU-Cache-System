function put() {
    fetch("/put", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            key: document.getElementById("key").value,
            value: document.getElementById("value").value
        })
    })
    .then(res => res.json())
    .then(data => {
        showMessage(data.message, "green");
        loadCache();
    });
}

function get() {
    fetch("/get", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            key: document.getElementById("key").value
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.value === -1)
            showMessage("Key not found", "red");
        else
            showMessage("Value: " + data.value, "green");

        loadCache();
    });
}

function remove() {
    fetch("/delete", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            key: document.getElementById("key").value
        })
    })
    .then(res => res.json())
    .then(data => {
        showMessage(data.deleted ? "Deleted" : "Key not found", "orange");
        loadCache();
    });
}

function loadCache() {
    fetch("/display")
        .then(res => res.json())
        .then(items => {
            let list = document.getElementById("cacheList");
            list.innerHTML = "";
            items.forEach(item => {
                let li = document.createElement("li");
                li.textContent = item.key + " : " + item.value;
                list.appendChild(li);
            });
        });
}

function showMessage(msg, color) {
    let el = document.getElementById("message");
    el.textContent = msg;
    el.style.color = color;
}

loadCache();
