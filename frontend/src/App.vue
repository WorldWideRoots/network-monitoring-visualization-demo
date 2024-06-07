<template>
  <div id="app">
    <header>
      <h1>Real-Time Flight Data Visualization</h1>
    </header>
    <FlightData />
  </div>
</template>

<script>
import FlightData from './components/FlightData.vue';

export default {
  name: 'App',
  components: {
    FlightData
  }
};
</script>

  