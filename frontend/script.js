// Initialize an empty chart
let chart;

// Function to generate the chart
function generateChart() {
    // Fetch JSON data from the server
    fetch('http://localhost:5500/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ /* Your request payload, if needed */ }),
    })
    .then(response => response.json())
    .then(data => {
        // Extract time and sensor values from the payload
        const timeArray = data.payload.map(entry => entry.time);
        const rotationRateXArray = data.payload.map(entry => entry.values.rotationRateX);
        const rotationRateYArray = data.payload.map(entry => entry.values.rotationRateY);
        const rotationRateZArray = data.payload.map(entry => entry.values.rotationRateZ);

        // Create a new chart or update existing one
        if (!chart) {
            const ctx = document.getElementById('myChart').getContext('2d');
            chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: timeArray,
                    datasets: [
                        {
                            label: 'Rotation Rate X',
                            borderColor: 'rgb(75, 192, 192)',
                            data: rotationRateXArray,
                            fill: false
                        },
                        {
                            label: 'Rotation Rate Y',
                            borderColor: 'rgb(255, 99, 132)',
                            data: rotationRateYArray,
                            fill: false
                        },
                        {
                            label: 'Rotation Rate Z',
                            borderColor: 'rgb(255, 205, 86)',
                            data: rotationRateZArray,
                            fill: false
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            type: 'linear',
                            position: 'bottom'
                        }
                    }
                }
            });
        } else {
            // Update chart data
            chart.data.labels = timeArray;
            chart.data.datasets[0].data = rotationRateXArray;
            chart.data.datasets[1].data = rotationRateYArray;
            chart.data.datasets[2].data = rotationRateZArray;
            chart.update();
        }
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}
