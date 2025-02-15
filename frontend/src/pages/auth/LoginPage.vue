<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const username = ref('');
const password = ref('');
const errorMessage = ref('');

const login = async () => {
  try {
    const response = await axios.post(`${import.meta.env.VITE_API_URL}/auth/login`, {
      username: username.value,
      password: password.value
    });
    
    // Store token and username only
    localStorage.setItem('token', response.data.access_token);
    localStorage.setItem('username', response.data.username);
    
    // Redirect to home
    router.push('/');
    setTimeout(() => window.location.reload(), 100);
  } catch (error) {
    errorMessage.value = 'Invalid credentials';
  }
};
</script>