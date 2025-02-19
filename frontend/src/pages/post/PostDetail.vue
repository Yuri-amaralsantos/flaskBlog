<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { fetchPostById, fetchComments, addComment, deleteComment } from '../../api';

const route = useRoute();
const router = useRouter();
const post = ref(null);
const comments = ref([]);
const newComment = ref('');
const errorMessage = ref('');
const username = localStorage.getItem('username') || '';
const userRole = localStorage.getItem('role') || ''; // Get user role
const isLoggedIn = computed(() => !!localStorage.getItem('token'));

// Check if the user is admin
const isAdmin = computed(() => userRole === 'admin');

// Load post and comments
const loadPostAndComments = async () => {
    try {
        post.value = await fetchPostById(route.params.id);
        comments.value = await fetchComments(route.params.id);
    } catch (error) {
        errorMessage.value = 'Error loading post or comments';
    }
};

// Add a new comment
const submitComment = async () => {
    if (!newComment.value.trim()) return;

    try {
        await addComment(route.params.id, newComment.value);
        newComment.value = '';
        comments.value = await fetchComments(route.params.id); // Refresh comments
    } catch (error) {
        errorMessage.value = 'Error adding comment';
    }
};

// Delete a comment
const removeComment = async (commentId) => {
    if (!confirm('Are you sure you want to delete this comment?')) return;

    try {
        await deleteComment(commentId);
        comments.value = comments.value.filter(comment => comment.id !== commentId);
    } catch (error) {
        errorMessage.value = 'Error deleting comment';
    }
};

onMounted(loadPostAndComments);
</script>

<template>
    <div>
        <h1>{{ post?.title }}</h1>
        <p><small>By: {{ post?.author }} | {{ post?.created_at }}</small></p>
        <p>{{ post?.content }}</p>

        <h2>Comments</h2>
        <p v-if="errorMessage">{{ errorMessage }}</p>

        <div v-if="isLoggedIn">
            <textarea v-model="newComment" placeholder="Add a comment..."></textarea>
            <button @click="submitComment">Post Comment</button>
        </div>

        <div v-for="comment in comments" :key="comment.id" class="comment">
            <p><strong>{{ comment.author }}</strong> | {{ comment.created_at }}</p>
            <p>{{ comment.content }}</p>

            <!-- Delete button visible if the user is logged in and is the comment's author, or if the user is admin -->
            <button v-if="isLoggedIn && (comment.author === username || isAdmin)" @click="removeComment(comment.id)">
                Delete
            </button>
        </div>
    </div>
</template>

<style scoped>
.comment {
    border: 1px solid #ddd;
    padding: 10px;
    margin: 5px 0;
}

textarea {
    width: 100%;
    height: 80px;
    margin: 10px 0;
}

button {
    padding: 8px 16px;
    background: blue;
    color: white;
    border: none;
    cursor: pointer;
}
</style>
