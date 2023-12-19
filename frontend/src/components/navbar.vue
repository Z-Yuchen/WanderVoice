<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <router-link to="/" style="display: flex;">
        <img src="../assets/voice-wave.png" alt="WanderVoice Logo" class="logo"/>
        <div class="navbar-item" style="font-size: 24px;">WanderVoice</div>
      </router-link>
    </div>
    <div class="navbar-menu">
      <router-link to="/functions" class="navbar-item">Functions</router-link>
      <router-link to="/support" class="navbar-item">Support</router-link>
      <router-link to="/login" class="navbar-item">Log out</router-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'App-Navbar'
}
</script>

<style>
    .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #000; /* Assuming a black background from the image */
    color: #fff; /* White text color */
    padding: 10px 20px; 
    height:50px
    }

    .navbar-brand {
    display: flex;
    align-items: center;
    }

    .logo {
    height: 30px; /* Adjust the size as needed */
    margin-right: 10px; /* Adds space between the logo and the brand name */
    }

    .navbar-menu {
    display: flex;
    }

    .navbar-item {
    color: #fff; /* White text color */
    text-decoration: none; /* Removes underline from links */
    margin-left: 20px; /* Space between menu items */
    font-family: 'Calibri', Arial, sans-serif;  font-weight:bold;
    align-items: center;
    display: flex;

    }

    .navbar-item:hover {
    text-decoration: underline; /* Adds underline on hover for visual feedback */
    }
</style>