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
  <div>
    <h1>Create Post</h1>

    <input v-model="title" placeholder="Title" />
    <textarea v-model="content" placeholder="Content"></textarea>
    <button @click="createPost">Submit Post</button>

    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
  </div>
</template>

<style scoped>
input,
textarea {
  display: block;
  width: 30%;
  margin-bottom: 10px;
  padding: 8px;
}

button {
  padding: 10px;
  background: blue;
  color: white;
  border: none;
  cursor: pointer;
}

.error {
  color: red;
}

.success {
  color: green;
}
</style>
