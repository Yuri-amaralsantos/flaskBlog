import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
});

export const fetchPosts = async () => {
    try {
        const response = await api.get('/blog');
        return response.data;
    } catch (error) {
        console.error('Error fetching posts:', error);
        return [];
    }
};
