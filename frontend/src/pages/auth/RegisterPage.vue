<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />


      <button type="submit">Register</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const username = ref('');
const password = ref('');
const errorMessage = ref('');

const register = async () => {
  try {
    await axios.post(`${import.meta.env.VITE_API_URL}/auth/register`, {
      username: username.value,
      password: password.value,
      role: "user"
    });
    alert('Registration successful!');
  } catch (error) {
    errorMessage.value = 'Registration failed';
  }
};
</script>
