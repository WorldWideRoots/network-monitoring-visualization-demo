<template>
    <div>
      <h2>Flight Data</h2>
      <svg id="chart"></svg>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import * as d3 from 'd3';
  
  export default {
    data() {
      return {
        flights: []
      };
    },
    async mounted() {
      const response = await axios.get('/api/flights');
      this.flights = response.data;
      this.createChart();
    },
    methods: {
      createChart() {
        const svg = d3.select('#chart')
          .attr('width', 800)
          .attr('height', 600);
  
        svg.selectAll('*').remove();
  
        svg.selectAll('circle')
          .data(this.flights)
          .enter()
          .append('circle')
          .attr('cx', d => d.longitude)
          .attr('cy', d => d.latitude)
          .attr('r', 3)
          .attr('fill', 'blue');
      }
    }
  };
  </script>
  ``
  