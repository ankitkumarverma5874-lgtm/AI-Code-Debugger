
async function debugCode() {

    const code = document.getElementById("codeInput").value;
    const button = document.getElementById("debugButton");
    const loading = document.getElementById("loading");
    const syntaxResult = document.getElementById("syntaxResult");
    const aiResult = document.getElementById("aiResult");

    if (!code.trim()) {
        alert("Please enter Python code first.");
        return;
    }

    button.disabled = true;
    button.textContent = "Analyzing...";
    loading.hidden = false;

    syntaxResult.textContent = "Checking syntax...";
    aiResult.textContent = "Waiting for AI response...";

    try {

        const response = await fetch("http://127.0.0.1:8000/debug", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code
            })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "API request failed.");
        }

        syntaxResult.textContent =
            result.syntax_check.message;

        aiResult.textContent =
            result.ai_analysis;

    } catch (error) {

        syntaxResult.textContent = "Debugging failed.";

        aiResult.textContent =
            "Error: " + error.message;

    } finally {

        loading.hidden = true;
        button.disabled = false;
        button.textContent = "Debug Code";
    }
}
