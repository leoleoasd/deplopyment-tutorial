<template>
  <div class="about">
    <h1>This is an about page</h1>

    <p> random value: {{ data }}</p>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { apiHost } from '@/config';
import {ref} from 'vue';
const data = ref(null);
axios.get(`${apiHost}/random`).then((res) => {
  data.value = res.data;
});
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    
    flex-direction: column;

  }
}
</style>
