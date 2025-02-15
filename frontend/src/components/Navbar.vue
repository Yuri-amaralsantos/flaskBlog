<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const user = ref({
  username: localStorage.getItem('username') || 'Guest',
});
const isLoggedIn = computed(() => !!localStorage.getItem('token'));

const logout = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('username');
  user.value.username = 'Guest';
  router.push('/login');
  window.location.reload();
};
</script>

<template>
  <nav>
    <div class="nav-left">
      <router-link to="/">My Blog</router-link>
    </div>
    <div class="nav-right">
      <template v-if="isLoggedIn">
        <span>Welcome, {{ user.username }}</span>
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
