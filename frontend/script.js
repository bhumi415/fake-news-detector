async function checkNews() {
    let text = document.getElementById("news").value;
    let resultBox = document.getElementById("result");

    if (text.trim() === "") {
        resultBox.innerText = "⚠️ Enter some news!";
        return;
    }

    resultBox.innerText = "⚡ Processing...";

    try {
        let response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ text })
        });

        let data = await response.json();

        if (data.error) {
            resultBox.innerText = "❌ " + data.error;
            return;
        }

        // 🔥 CLEAN RESULT (NO %)
        if (data.prediction === "Real News") {
            resultBox.innerText = "✅ Real News";
            resultBox.style.color = "#00ffcc";
        } else {
            resultBox.innerText = "❌ Fake News";
            resultBox.style.color = "#ff4d4d";
        }

        // Keywords
        if (data.keywords && data.keywords.length > 0) {
            resultBox.innerText += "\n⚠️ Suspicious: " + data.keywords.join(", ");
        }

        saveHistory(text, data.prediction);

    } catch (error) {
        resultBox.innerText = "❌ Server Error";
    }
}

/* History */
function saveHistory(text, result) {
    let history = JSON.parse(localStorage.getItem("history")) || [];

    history.unshift({ text, result });

    if (history.length > 5) history.pop();

    localStorage.setItem("history", JSON.stringify(history));

    renderHistory();
}

function renderHistory() {
    let list = document.getElementById("historyList");
    let history = JSON.parse(localStorage.getItem("history")) || [];

    list.innerHTML = "";

    history.forEach(item => {
        let li = document.createElement("li");
        li.innerText = item.text.substring(0, 50) + " → " + item.result;
        list.appendChild(li);
    });
}

window.onload = renderHistory;