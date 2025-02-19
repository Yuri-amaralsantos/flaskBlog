<template>
  <div>
    <h1>Blog Posts</h1>

    <!-- Search box -->
    <input type="text" v-model="searchQuery" placeholder="Search posts..." />

    <!-- Admin sees the Create Post button -->
    <button v-if="isLoggedIn && isAdmin" @click="goToCreatePost">Create Post</button>

    <p v-if="errorMessage">{{ errorMessage }}</p>

    <div class="cards">
      <div v-for="post in filteredPosts" :key="post.id">
        <button class="card" @click="goToPost(post.id)">
          <div>
            <h3>{{ post.title }}</h3>
            <small>By: {{ post.author }} | {{ formatDate(post.created_at) }}</small>
          </div>
          <div>
            <!-- Delete button visible if the user is logged in, is the author, or is an admin -->
            <button class="button" v-if="isLoggedIn && isAdmin" @click.stop="removePost(post.id)">
              Delete
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
</script>

<style scoped>
.cards {
  margin: 2rem;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  background-color: blue;
  border: 1px solid black;
  display: flex;
  width: 200px;
  justify-content: space-between;
  padding: 1rem;
  cursor: pointer;
}

h1 {
  color: #333;
}

.button {
  padding: 8px 16px;
  background: white;
  color: blue;
  border: none;
  cursor: pointer;
}

input {
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  width: 100%;
}
</style>
