<template>
  <div class="about-page">
    <Navbar></Navbar>
    <section class="about-intro">
      <h1>About Us</h1>
      <p>Welcome to WanderVoice – your intelligent companion on every journey.</p>
      <p>
      In today's world, in-car voice assistants have become an integral part of our driving experience. 
      While they successfully set navigational goals and follow basic commands, there's a vast expanse of road untraveled when it comes to providing personalized, 
      real-time suggestions and travel insights. That's where WanderVoice steps in.
      </p>
    </section>

    <section class="why-wander-voice">
      <h2>Why WanderVoice?</h2>
      <p>Traditional voice assistants just aren't enough anymore. Whether you're a tourist exploring unfamiliar terrains or a local in search of new experiences, 
      WanderVoice is designed to enrich your journey. We recognized the need for a dynamic assistant – one that goes beyond the basic functionalities and delves 
      into the realm of real-time travel guidance.
      </p>
      <p>
      With WanderVoice, you're not just getting from point A to B. Our advanced AI system serves dual purposes: acting as a travel chatbot, answering any questions 
      you might have about your trip, and offering spontaneous real-time suggestions, ensuring you get the most out of every drive.\n
      </p>
    </section>

    <section class="team-behind">
      <h2>Meet The Team Behind WanderVoice</h2>
      <p>Founded by a team of passionate innovators - Yuchen Zhu (yz4396), Yizhan Zhang (yz4703), and Xinyang Wang (xw2964). 
      WanderVoice is a testament to our collective vision. Our dedication stems from understanding drivers' needs and 
      our aim to revolutionize the driving experience.</p>


    </section>

    <section class="embark-journey">
      <h2>Embark on a Journey Like Never Before</h2>
      <p>Let WanderVoice be the soundtrack to your adventures, offering insights, recommendations, and answering every curious thought that might cross your mind during a drive. 
      It's not about the destination but the journey, and with WanderVoice, you're guaranteed a memorable one.</p>
      <p>Join us and redefine your driving experience. Welcome to WanderVoice – Where every journey has a story.</p>
    </section>
  </div>
</template>

<script>
import Navbar from './navbar.vue';

export default {
  name: 'AboutPage',
  components: {
    Navbar
  },
}
</script>

<style scoped>
.about-page {
  /* Style your page according to the design */
}

.about-intro, .why-wander-voice, .team-behind, .embark-journey {
  /* Apply common styles to each section */
}

/* Add additional styles for each section as needed */
</style>
