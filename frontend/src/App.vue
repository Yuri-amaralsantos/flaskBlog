<script setup>
import Navbar from './components/Navbar.vue';
</script>

<template>
  <Navbar />
  <router-view />
</template>

<style scoped>
nav {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}
</style>
