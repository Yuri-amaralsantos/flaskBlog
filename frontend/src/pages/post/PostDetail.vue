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
            <textarea v-model="newComment" placeholder="Add a comment..." class="textarea"></textarea>
            <button @click="submitComment" class="button">Post Comment</button>
        </div>

        <div v-for="comment in comments" :key="comment.id" class="comment">
            <div>
                <p><strong>{{ comment.author }}</strong> | {{ comment.created_at }}</p>
                <p>{{ comment.content }}</p>
            </div>
            <div>
                <!-- Delete button visible if the user is logged in and is the comment's author, or if the user is admin -->
                <button v-if="isLoggedIn && (comment.author === username || isAdmin)"
                    @click="removeComment(comment.id)">
                    Delete
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.comment {
    width: 90%;
    border: 1px solid black;
    padding: 10px;
    margin: 5px 0;
    border-radius: 10px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;

}

.comment button {
    padding: 8px 16px;
    border: 1px solid black;
    border-radius: 10px;
    cursor: pointer;
}

.textarea {
    padding: 24px;
    width: 90%;
    height: 80px;
    margin: 10px 0;
    border-radius: 10px;
}

.button {
    padding: 8px 16px;
    border: 1px solid black;
    border-radius: 10px;
    cursor: pointer;
}
</style>
