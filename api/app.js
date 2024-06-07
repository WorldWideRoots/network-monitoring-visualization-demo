const express = require('express');
const Influx = require('influx');
const app = express();
const port = 5000;

const influx = new Influx.InfluxDB({
  host: 'influxdb',
  database: 'flight_data'
});

app.get('/api/flights', async (req, res) => {
  try {
    const result = await influx.query('SELECT * FROM flights ORDER BY time DESC LIMIT 100');
    res.json(result);
  } catch (err) {
    res.status(500).send(err.stack);
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
