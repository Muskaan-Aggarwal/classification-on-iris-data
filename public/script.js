// public/script.js
document.getElementById('predictionForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const sepalLength = document.getElementById('sepalLength').value;
    const sepalWidth = document.getElementById('sepalWidth').value;
    const petalLength = document.getElementById('petalLength').value;
    const petalWidth = document.getElementById('petalWidth').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sepalLength: parseFloat(sepalLength),
            sepalWidth: parseFloat(sepalWidth),
            petalLength: parseFloat(petalLength),
            petalWidth: parseFloat(petalWidth)
        })
    });

    const data = await response.json();
    document.getElementById('result').innerText = `Predicted Species: ${data.prediction}`;
});
