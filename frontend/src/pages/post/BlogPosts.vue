<template>
  <div class="page">
    <div class="containerSearch">
      <h1>Postagens</h1>

      <!-- Search box -->
      <input type="text" v-model="searchQuery" placeholder="Search posts..." />
      <button v-if="isLoggedIn" @click="goToCreatePost">Nova Postagem</button>
    </div>

    <!-- Admin sees the Create Post button -->


    <p v-if="errorMessage">{{ errorMessage }}</p>

    <div class="cards">
      <div v-for="post in filteredPosts" :key="post.id">
        <button class="card" @click="goToPost(post.id)">
          <div class="text">
            <h3>{{ post.title }}</h3>
            <p>{{ truncateWords(post.content, 30) }}</p>
            <p>Por: {{ post.author }} | {{ formatDate(post.created_at) }}</p>
          </div>
          <div>
            <button v-if="isLoggedIn && (post.author === username || isAdmin)" @click.stop=" editPost(post.id)"
              class="edit">
              Editar
            </button>
            <button v-if="isLoggedIn && (post.author === username || isAdmin)" @click.stop="removePost(post.id)"
              class="delete">
              Deletar
            </button>
          </div>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { fetchPosts, deletePost } from '../../api';
import { useRouter } from 'vue-router';

const router = useRouter();
const posts = ref([]);
const searchQuery = ref('');
const errorMessage = ref('');
const userRole = localStorage.getItem('role') || '';

// Check if the user is logged in
const isLoggedIn = computed(() => !!localStorage.getItem('token'));

const username = localStorage.getItem('username') || '';

const editPost = (postId) => {
  router.push({ name: 'editPost', params: { id: postId } });
};


// Check if the user is admin
const isAdmin = computed(() => userRole === 'admin');

// Load posts from the API
const loadPosts = async () => {
  try {
    posts.value = await fetchPosts();
  } catch (error) {
    errorMessage.value = 'Error loading posts';
  }
};

// Navigate to a post detail page
const goToPost = (postId) => {
  router.push({ name: 'postDetail', params: { id: postId } });
};

// Remove a post
const removePost = async (postId) => {
  if (!confirm(`Are you sure you want to delete this post?`)) return;

  try {
    await deletePost(postId);
    posts.value = posts.value.filter((post) => post.id !== postId);
  } catch (error) {
    errorMessage.value = 'Error deleting post';
  }
};

const goToCreatePost = () => {
  router.push('/newPost');
};

onMounted(loadPosts);

// Format the post creation date
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleString();
};

// Computed property for filtering and sorting posts
const filteredPosts = computed(() => {
  return posts.value
    .filter((post) => post.title.toLowerCase().includes(searchQuery.value.toLowerCase()))
    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at)); // Sort by date (newest first)
});

const truncateWords = (text, maxWords) => {
  const words = text.split(" ");
  return words.length > maxWords ? words.slice(0, maxWords).join(" ") + "..." : text;
};


</script>

<style scoped>
.page {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.containerSearch {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  padding: 2rem 0;
  width: 80%;
}

.containerSearch h1 {
  margin: 0;
}

.containerSearch button {
  border-radius: 10px;
  min-width: 80px;
}

.cards {
  margin: 2rem;
  width: 80%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.card {
  border-radius: 20px;
  border: 1px solid black;
  display: flex;
  min-width: 100%;
  justify-content: space-between;

  padding: 1rem;
  cursor: pointer;
}

.text {
  display: flex;
  flex-direction: column;
  align-items: start;
  gap: 1rem;
  text-align: left;
  padding: 2rem 0;
}

.card h3 {
  font-weight: bold;
  font-size: 30px;
  margin: 0;
}

.card p {
  font-size: 18px;
  margin: 0;
}

.delete {
  margin-left: 1rem;
  padding: 8px 16px;
  background: red;
  color: white;
  cursor: pointer;
  border-radius: 10px;
}

.containerSearch input {
  padding: 0 1rem;
  border-radius: 10px;
  border: 1px solid black;
  width: 100%;
}

.edit {
  padding: 8px 16px;
  cursor: pointer;
  border-radius: 10px;
}
</style>
