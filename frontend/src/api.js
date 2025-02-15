import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000', // Correct URL for your API
});

// Fetch Posts
export const fetchPosts = async () => {
    try {
        const response = await api.get('/blog');
        // This will correctly hit the /blog route
        return response.data;
    } catch (error) {
        console.error('Error fetching posts:', error);
        return [];
    }
};

export const fetchPostById = async (postId) => {
    try {
        const response = await api.get(`/blog/${postId}`);
        return response.data;  // Axios response data is directly in response.data
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
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        // Axios throws an error on failure, so no need for response.ok check
        return response.data;  // Assuming the API returns a response body
    } catch (error) {
        console.error('Error deleting post:', error);
        throw error;  // Propagate the error to handle it in the component
    }
}
