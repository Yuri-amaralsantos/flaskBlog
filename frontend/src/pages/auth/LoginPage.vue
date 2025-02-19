<template>
  <div class="login">
    <div class="container">
      <h1>Conectar</h1>
      <form @submit.prevent="login" class="form">
        <input v-model="username" placeholder="Nome do usuário" />
        <input v-model="password" type="password" placeholder="Senha" />
        <button type="submit">Avançar</button>
      </form>
      <p v-if="errorMessage">Nome do usuário ou senha incorreta</p>
    </div>
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

    // Store token, username, and role
    localStorage.setItem('token', response.data.access_token);
    localStorage.setItem('username', response.data.username);
    localStorage.setItem('role', response.data.role);  // Store the user's role

    // Redirect to home
    router.push('/');
    setTimeout(() => window.location.reload(), 100);
  } catch (error) {
    errorMessage.value = 'Invalid credentials';
  }
};

</script>

<style scoped>
.login {
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