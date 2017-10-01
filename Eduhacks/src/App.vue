<template>
  <div>
    <ul>
      <li>
        <router-link to="/MainStudent">Home</router-link>
      </li>
      <li>
        <router-link to="/SearchStudent">Search</router-link>
        </li>
      <li>
        <router-link to="/ConnectStudent">Connect</router-link>
        </li>
      <li>
        <router-link to="/">Login</router-link>
        </li>
    </ul>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
*,
*::before,
*::after {
    box-sizing: border-box;
}

html {
    font-size: 100%;
}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}
li {
    float: left;
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover:not(.active) {
    background-color: #111;
}
.active {
    background-color: #4CAF50;
}
</style>
