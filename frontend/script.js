const analyzeBtn = document.getElementById("analyzeBtn");
const newsInput = document.getElementById("newsInput");
const result = document.getElementById("result");

analyzeBtn.addEventListener("click", () => {
    const news = newsInput.value;

    if (news.trim() === "") {
        result.innerText = "Please enter some news";
        return;
    }

    // 🔥 BACKEND API CALL
    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: news })
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            result.innerText = data.error;
        } else {
            result.innerText = `${data.prediction} (${data.confidence}% confidence)`;
        }
    })
    .catch(err => {
        result.innerText = "Error connecting to server";
        console.error(err);
    });
});