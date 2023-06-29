
function drawChart() {
  google.charts.load('current', { packages: ['corechart'], language: 'in' });
  google.charts.setOnLoadCallback(draw);

  function draw() {
    // Set Data
    const data = google.visualization.arrayToDataTable([
      ['Time', 'Price'],
      ['00:00', 0],
      ['01:00', 200],
      ['02:00', 350],
      ['03:00', 400],
      ['04:00', 550],
      ['05:00', 1000],
      ['06:00', 1700],
      ['07:00', 2000],
      ['08:00', 2500],
      ['09:00', 2600],
      ['10:00', 2750],
      ['11:00', 2900],
      ['12:00', 3500],
      ]);

    // Set Options
    const options = {
      title: new Date().toLocaleDateString('en-GB', { day: '2-digit', month: '2-digit', year: 'numeric' }), // Set the title with "dd-mm-yyyy" format
      curveType: 'function',
      hAxis: {
  title: 'Time (12-hour format)',
  format: 'HH:mm', // Format for time display
  },
  vAxis: {
  title: 'Price (Rupees ₹)',
  format: 'currency', // Format for currency display
  minValue: 100, // Minimum value for the y-axis
  maxValue: 4000, // Maximum value for the y-axis
  },
      legend: 'none'
    };

    // Draw
    const chart = new google.visualization.LineChart(document.getElementById('myChart'));
    chart.draw(data, options);
  }
}