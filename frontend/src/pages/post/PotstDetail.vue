<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { fetchPostById } from '../../api'; // Assuming you have a function to fetch a single post

const route = useRoute();
const post = ref(null);
const errorMessage = ref('');

// Load post by ID
const loadPost = async () => {
    const postId = route.params.id;
    if (!postId) {
        console.log(postId);
    }
    try {
        post.value = await fetchPostById(postId);
        console.log("Post loaded successfully");
    } catch (error) {
        errorMessage.value = 'Error loading post';
        console.error(error);  // Log the error for better debugging
    }
};

onMounted(loadPost);
</script>

<template>
    <div>
        <h1>Post Details</h1>

        <p v-if="errorMessage">{{ errorMessage }}</p>

        <div v-if="post">
            <h2>{{ post.title }}</h2>
            <p><strong>By:</strong> {{ post.author }} | <strong>Created:</strong> {{ new
                Date(post.created_at).toLocaleString() }}</p>
            <div>
                <p>{{ post.content }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Add your custom styles */
h1 {
    color: #333;
}

h2 {
    color: #555;
}
</style>
