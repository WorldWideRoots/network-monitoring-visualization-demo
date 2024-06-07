<template>
  <div id="app">
    <GrafanaDashboard />
  </div>
</template>

<script>
import GrafanaDashboard from './components/GrafanaDashboard.vue';

export default {
  name: 'App',
  components: {
    GrafanaDashboard
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
