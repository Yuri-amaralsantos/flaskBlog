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
      <router-link to="/">Blog</router-link>
    </div>
    <div class="nav-right">
      <template v-if="isAuthenticated">
        <span>Bem vindo, {{ user }}</span>
        <button @click="logout">Desconectar</button>
      </template>
      <template v-else class="nonlogged">
        <button><router-link to="/register">Registrar</router-link></button>
        <button><router-link to="/login">Conectar</router-link></button>
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
