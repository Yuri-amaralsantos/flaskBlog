import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000', // API URL from env or default
});

// Check if Token is Valid
export async function checkToken() {
    const token = localStorage.getItem("token");
    if (!token) return false; // No token, so it's invalid

    try {
        const response = await api.get('/auth/check_token', {
            headers: { Authorization: `Bearer ${token}` },
        });
        return response.data.valid;
    } catch (error) {
        return false; // Token expired or invalid
    }
}

// Fetch Posts
export const fetchPosts = async () => {
    try {
        const response = await api.get('/blog');
        return response.data;
    } catch (error) {
        console.error('Error fetching posts:', error);
        return [];
    }
};

// Fetch Single Post
export const fetchPostById = async (postId) => {
    try {
        const response = await api.get(`/blog/${postId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching post:', error);
        throw new Error('Post not found');
    }
};

// Delete Post
export async function deletePost(postId) {
    const token = localStorage.getItem('token');
    try {
        const response = await api.delete(`/blog/${postId}`, {
            headers: { Authorization: `Bearer ${token}` }
        });
        return response.data;
    } catch (error) {
        console.error('Error deleting post:', error);
        throw error;
    }
}

// Fetch Comments for a Post
export const fetchComments = async (postId) => {
    try {
        const response = await api.get(`/blog/${postId}/comments`);
        return response.data;
    } catch (error) {
        console.error('Error fetching comments:', error);
        return [];
    }
};

// Add a Comment
export const addComment = async (postId, content) => {
    const token = localStorage.getItem('token');
    try {
        const response = await api.post(
            `/blog/${postId}/comments`,
            { content },
            { headers: { Authorization: `Bearer ${token}` } }
        );
        return response.data;
    } catch (error) {
        console.error('Error adding comment:', error);
        throw error;
    }
};

// Delete a Comment
export const deleteComment = async (commentId) => {
    const token = localStorage.getItem('token');
    try {
        const response = await api.delete(`/blog/comments/${commentId}`, {
            headers: { Authorization: `Bearer ${token}` }
        });
        return response.data;
    } catch (error) {
        console.error('Error deleting comment:', error);
        throw error;
    }
};

export default api;
