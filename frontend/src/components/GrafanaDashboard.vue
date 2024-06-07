<template>
    <div>
      <h1>Grafana Dashboards</h1>
      <div v-if="dashboards.length">
        <h2>Available Dashboards</h2>
        <ul>
          <li v-for="dashboard in dashboards" :key="dashboard.uid">
            <a :href="`http://localhost:3000/d/${dashboard.uid}`" target="_blank">{{ dashboard.title }}</a>
            <button @click="embedDashboard(dashboard.uid)">Embed</button>
          </li>
        </ul>
      </div>
      <div v-if="selectedDashboard">
        <h2>Embedded Dashboard</h2>
        <iframe
          :src="`http://localhost:3000/d/${selectedDashboard}?orgId=1&refresh=10s`"
          width="100%"
          height="800px"
          frameborder="0"
        ></iframe>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        dashboards: [],
        selectedDashboard: null
      };
    },
    created() {
      this.fetchDashboards();
    },
    methods: {
      fetchDashboards() {
        fetch("http://localhost:3000/api/search", {
          headers: {
            "Authorization": "Bearer YOUR_API_KEY"
          }
        })
          .then(response => response.json())
          .then(data => {
            this.dashboards = data;
          })
          .catch(error => console.error("Error fetching dashboards:", error));
      },
      embedDashboard(uid) {
        this.selectedDashboard = uid;
      }
    }
  };
  </script>
  
  <style scoped>
  a {
    color: blue;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
  iframe {
    border: none;
  }
  </style>
  