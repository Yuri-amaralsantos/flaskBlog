<script setup>
import { ref, onMounted, computed } from 'vue';
import { fetchPosts, deletePost } from '../../api'; // Import delete function
import { useRouter } from 'vue-router';

const router = useRouter();
const posts = ref([]);
const errorMessage = ref('');
const username = localStorage.getItem('username') || ''; // Get logged-in username

// Check if the user is logged in
const isLoggedIn = computed(() => !!localStorage.getItem('token'));

// Load posts from the API
const loadPosts = async () => {
  try {
    posts.value = await fetchPosts();

  } catch (error) {
    errorMessage.value = 'Error loading posts';
  }
};

// Format the post creation date
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleString(); // Formats date to local timezone
};

// Remove a post
const removePost = async (postId) => {
  if (!postId) {
    console.error('Invalid postId:', postId);
    return;
  }
  if (!confirm(`Are you sure you want to delete this post?` + postId)) return;

  try {
    await deletePost(postId);
    posts.value = posts.value.filter(post => post.post_id !== postId); // Remove from UI
  } catch (error) {
    errorMessage.value = 'Error deleting post';
  }
};

onMounted(loadPosts);

// Navigate to create post page
const goToCreatePost = () => {
  router.push('/newPost');
};
</script>

<template>
  <div>
    <h1>Blog Posts</h1>

    <button v-if="isLoggedIn" @click="goToCreatePost">Create Post</button>

    <p v-if="errorMessage">{{ errorMessage }}</p>

    <div v-for="post in posts" :key="post.id">
      <div class="card">
        <div>
          <h3>{{ post.title }}</h3>
          <small>By: {{ post.author }} | {{ formatDate(post.created_at) }}</small>
        </div>
        <div>
          <!-- Link to Post Detail Page -->
          <button><router-link class="link" :to="{ name: 'postDetail', params: { id: post.id } }">Read
              More</router-link></button>
          <!-- Delete button visible if the user is logged in and is the author -->
          <button v-if="isLoggedIn && post.author === username" @click="removePost(post.id)">
            Delete
          </button>


        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.link {
  color: white;
  text-decoration: none;
}

.card {
  border: 1px solid black;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

h1 {
  color: #333;
}

button {
  padding: 8px 16px;
  background: blue;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
