<template>

<div class="header">
  <ul class="header-button-left">
    <li>
      <router-link to="/">Home</router-link>
      <router-link to="/canvas"> Canvas </router-link>
      <router-link to="/writing"> Diary </router-link>
      <router-link to="/calendar"> Calendar </router-link>
      <router-link to="/login"> Login </router-link>
      <router-link to="/signup"> Signup </router-link>
    </li>
  </ul>
</div>

  <!-- <diary-writing></diary-writing> -->
  <!-- <diary-calendar></diary-calendar> -->
  <!-- <canvas-drawing></canvas-drawing> -->

  


  <router-view></router-view>

  
</template>

<script>

import DiaryWriting from './components/DiaryWriting';
import CanvasDrawing from './components/CanvasDrawing'
import DiaryCalendar from './components/DiaryCalendar'


export default {
  name:'App',
  components:{
    DiaryWriting,
   DiaryCalendar,
   CanvasDrawing,
   
    
   
  }

}
</script>

<style>
#app {
  overflow-y: hidden !important;
}

.header {
  width: 100%;
  height: 20px;
  background-color: white;
  /* padding-bottom: 8px; */
  position: sticky;
  top: 2px;
  margin-left: 35%;
  position:fixed;
}
.header-button-left {
  color: grey;
  float: left;
  width: 50px;
  padding-left: 20px;
  cursor: pointer; 
  margin-top: 10px;
}


</style>