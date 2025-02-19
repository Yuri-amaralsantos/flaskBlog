<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const title = ref('');
const content = ref('');
const errorMessage = ref('');
const successMessage = ref('');

const createPost = async () => {
  if (!title.value || !content.value) {
    errorMessage.value = 'Title and content are required!';
    return;
  }

  try {
    const token = localStorage.getItem('token');
    if (!token) {
      errorMessage.value = 'User is not authenticated.';
      return;
    }

    const response = await axios.post(
      `${import.meta.env.VITE_API_URL}/blog/`,
      { title: title.value, content: content.value },  // No need to send username
      { headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' } }
    );

    successMessage.value = response.data.message;
    title.value = '';
    content.value = '';

    setTimeout(() => router.push('/'), 1000);
  } catch (error) {
    errorMessage.value = 'Failed to create post.';
  }
};
</script>

<template>
  <div class="page">
    <h1>Criar postagem</h1>

    <input v-model="title" placeholder="Titulo (maximo de 200 characteres)" class="input" />
    <textarea v-model="content" placeholder="Texto" class="textarea"></textarea>
    <button @click="createPost" class="button">Postar</button>

    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
  </div>
</template>

<style scoped>
.page {
  display: flex;
  flex-direction: column;
  align-items: start;
}

.input,
.textarea {
  width: 90%;
  margin: 10px 0;
  border-radius: 10px;
}

.input {
  padding: 1rem 1rem;
}

.textarea {
  padding: 1rem 1rem;
  min-height: 300px;
}

.button {
  padding: 8px 16px;
  border: 1px solid black;
  border-radius: 10px;
  cursor: pointer;
}

.error {
  color: red;
}

.success {
  color: green;
}
</style>
