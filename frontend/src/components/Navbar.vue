<script setup>
import { inject, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isAuthenticated = inject("isAuthenticated"); // Inject global state
const logout = inject("logout"); // Inject logout function

const user = computed(() => localStorage.getItem('username') || 'Guest');
</script>

<template>
  <nav>
    <div class="nav-left">
      <router-link to="/">My Blog</router-link>
    </div>
    <div class="nav-right">
      <template v-if="isAuthenticated">
        <span>Welcome, {{ user }}</span>
        <button @click="logout">Log Out</button>
      </template>
      <template v-else>
        <router-link to="/register">Register</router-link>
        <router-link to="/login">Login</router-link>
      </template>
    </div>
  </nav>
</template>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  padding: 10px 20px;
  background: #333;
  color: white;
}

.nav-left a {
  color: white;
  font-size: 20px;
  text-decoration: none;
  font-weight: bold;
}

.nav-right a,
.nav-right button {
  margin-left: 10px;
  color: white;
  text-decoration: none;
  background: none;
  border: none;
  cursor: pointer;
}

.nav-right button:hover {
  text-decoration: underline;
}
</style>
