<script setup>
import { ref, onMounted } from 'vue';
import { fetchPosts } from '../api';

const posts = ref([]);
const errorMessage = ref('');

const loadPosts = async () => {
  posts.value = await fetchPosts();
};

onMounted(loadPosts);
</script>

<template>
  <div>
    <h1>Blog Posts</h1>
    <p v-if="errorMessage">{{ errorMessage }}</p>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <h3>{{ post.title }}</h3>
        <p>{{ post.content }}</p>
        <small>By: {{ post.author }}</small>
      </li>
    </ul>
  </div>
</template>

<style scoped>
h1 {
  color: #333;
}
</style>
