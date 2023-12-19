<template>
  <div>
    <Navbar/>
    <div style="background-image: url(../assets/logo.png);background-size: 100% 100%; min-height: 800px;background-repeat: no-repeat;">

    <div style="height: 40px"></div>

    <div style="display: flex; background-color: rgba(0, 0, 0, 0.4); background-size: contain; border-radius: 10px; width: 76%;height:690px;margin-left: auto;margin-right: auto;  /* 圆角边框 */
">
    <div style="  display: flex;  flex-direction: column;">
    <div class="click-button" @click="goToTourPage">
        <button class="tour">  
          <img src="../assets/tour.png"/>
        </button>
  </div>
  <div class="title"> Tour Guide</div>
  <div class="intro">Navigate the Road of Knowledge: </div>
  <div class="intro">        Your In-Car Companion for Instant Answers and Conversations.
 </div>
  </div>

  <div style="  display: flex;  flex-direction: column;">

  <div class="click-button" @click="goToRecommPage">
        <button class="recomm">
          <img src="../assets/recomm.png"/>
        </button>
  </div>
  <div class="title"> Recommendation</div>
  <div class="intro">Discover, Stay, and Play just for you:</div>
    <div class="intro">    Smart suggestions for hotels, sports, and music from Top Websites</div>
</div>
</div>
<div style="height: 40px"></div>

</div>
</div>
    
</template>


<script>
import Navbar from './navbar.vue';

export default {
    data() {
      return {
        
      };
    },
    components: {
        Navbar,
        // AudioRecorder
    },
    mounted() {
     
    },

    beforeUnmount() {
    // 清除定时器
    },
    methods: {
      goToTourPage() {
        this.$router.push('/tourguide');
      },
      goToRecommPage() {
        this.$router.push('/recomm');
      }
    }
}


</script>

<style>
.title {
  margin-top: 20px;
  font-family: 'Calibri', Arial, sans-serif;  
  font-weight:bold;
  font-size: 40px;
  color: #ffffff;
  text-align: center;
  width: 80%;
  padding-top:40px;
  margin-left: auto;
  margin-right: auto;
}
.intro {
  font-family: 'Calibri', Arial, sans-serif;  
  font-weight:bold;
  font-size: 26px;
  color: #ffffff;
  text-align: center;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}

.tour {
  width: 160px; /* Adjust width as needed */
  height: 160px; /* Ensure it's the same as width for a square shape */
  /* display: flex; */
  border-radius: 15px; /* Adjust border-radius for rounded corners */
  border: none;
  cursor: pointer;
  background-color: rgb( 255,255,255,0);
}
.tour img {
  max-width: 110%; /* Adjust image size */
  max-height: 110%; /* Adjust image size */
  border-radius: 15px; /* Adjust border-radius for rounded corners */
}
.recomm {
  width: 160px; /* Adjust width as needed */
  height: 160px; /* Ensure it's the same as width for a square shape */
  /* display: flex; */
  border-radius: 15px; /* Adjust border-radius for rounded corners */
  border: none;
  cursor: pointer;
  background-color: rgb( 255,255,255,0);
}
.recomm img {
  max-width: 110%; /* Adjust image size */
  max-height: 110%; /* Adjust image size */
  border-radius: 15px; /* Adjust border-radius for rounded corners */
}
.click-button {
  margin-left: auto;
  margin-right: auto;
  margin-top: 120px;
}



</style>