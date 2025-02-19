<script setup>
import { ref, onMounted, provide } from "vue";
import { checkToken } from "./api";
import Navbar from './components/Navbar.vue';
import { useRouter } from "vue-router";

const router = useRouter();
const isAuthenticated = ref(true); // Assume user is authenticated initially

async function verifyToken() {
  isAuthenticated.value = await checkToken();

  if (!isAuthenticated.value) {
    console.warn("Token expired! Logging out...");
    logout(); // Call logout when token expires
  }
}

// Logout function to update state globally
function logout() {
  localStorage.removeItem("token");
  localStorage.removeItem("username");
  localStorage.removeItem("role");
  isAuthenticated.value = false; // Update state
  router.push("/login");
}

// Provide authentication state and logout function to all child components
provide("isAuthenticated", isAuthenticated);
provide("logout", logout);

onMounted(() => {
  verifyToken();
  setInterval(verifyToken, 30000); // Check token every 30 seconds
});
</script>

<template>
  <Navbar />
  <router-view />
</template>
