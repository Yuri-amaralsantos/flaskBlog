<template>
  <div class="register">
    <div class="container">
      <h1>Registrar</h1>
      <form @submit.prevent="register" class="form">
        <input v-model="username" placeholder="Nome do usuário" />
        <input v-model="password" type="password" placeholder="Senha" />


        <button type="submit">Register</button>
      </form>
      <p v-if="errorMessage">Falha ao cadastrar usuário</p>
    </div>
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

<style scoped>
.register {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 500px;
}

.container {
  border: 1px solid black;
  border-radius: 10px;
  padding: 3rem;
  width: 25%;
}

@media (max-width: 374px) {
  .container {
    padding: 1rem;
    width: 80%;

  }
}

.form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form input {
  padding: 0.5rem;
  border-radius: 10px;
}

.form button {
  padding: 0.5rem;
  border-radius: 10px;
}
</style>