<template>
  <div class="login-page">
    <div class="brand-section">
      <h1 style="font-family: 'Calibri', Arial, sans-serif;  font-weight:bold;font-size: 60px;">WanderVoice</h1>
      <p style="font-family: 'Calibri', Arial, sans-serif; font-size: 24px;">Your innovative in-car voice assistant.</p>
      <p style="font-family: 'Calibri', Arial, sans-serif; font-size: 24px;">Experience the future of voice assistants in your car!</p>
    </div>
    <div class="login-section">
      <div class="login-container">
        <h1 style="font-family: 'Calibri', Arial, sans-serif;  font-weight:bold;font-size: 26px;">WanderVoice</h1>
        <h2 style="font-family: 'Calibri', Arial, sans-serif;  font-weight:bold;font-size: 16px;">Log in</h2>
        <form @submit.prevent="goToAnotherPage">
          <input type="text" style="font-family: 'Calibri', Arial, sans-serif;" placeholder="User Name" required>
          <input type="password"  style="font-family: 'Calibri', Arial, sans-serif;" placeholder="Password" required minlength="6">
          <button type="submit" style="font-family: 'Calibri', Arial, sans-serif;">Log in</button>
        </form>
        <div class="login-footer">
          <p style="font-family: 'Calibri', Arial, sans-serif;">Not a member? <router-link to="/signup">Sign Up</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  methods: {
    goToAnotherPage() {
      this.$router.push('/functions');
    }

  }
}
</script>

<style scoped>
.login-page {
  display: flex;
  width: 100vw; /* Full width of the viewport */
  height: 100vh; /* Full height of the viewport, making the page take up the entire screen */
}

.brand-section {
  background-image: url('../assets/logo.png'); /* Cover the entire div with the image */
  background-position: center; /* Center the image in the div */
  flex: 1; /* Take up half of the container */
  padding: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.login-section {
  flex: 1; /* Take up the other half of the container */
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-container {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  width: 300px; /* Adjust width as necessary */
}

.login-container h2, .login-container h3 {
  color: #333;
  margin-bottom: 10px;
}

input[type="text"], input[type="password"] {
  width: 92%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #e91e63; /* Pink for the button */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #d81b60; /* Darker pink on hover */
}

.login-footer {
  font-size: 0.8rem;
  text-align: center;
  margin-top: 20px;
}

.login-footer a, .router-link {
  color: #e91e63;
  text-decoration: none;
}

.login-footer a:hover, .router-link:hover {
  text-decoration: underline;
}
</style>
