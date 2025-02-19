import { createRouter, createWebHistory } from 'vue-router';
import BlogPosts from '../pages/post/BlogPosts.vue';
import CreatePost from '../pages/post/CreatePost.vue';
import PostDetail from '../pages/post/PostDetail.vue';
import LoginPage from '../pages/auth/LoginPage.vue';
import RegisterPage from '../pages/auth/RegisterPage.vue';
import EditPost from '../pages/post/EditPost.vue';

const routes = [
    { path: '/', component: BlogPosts },  // Blog Page
    { path: '/newPost', component: CreatePost },  // Blog Page
    { path: '/post/:id', component: PostDetail, name: 'postDetail' },
    { path: '/edit/:id', component: EditPost, name: 'editPost' },
    { path: '/login', component: LoginPage }, // Login Page
    { path: '/register', component: RegisterPage } // Register Page
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
