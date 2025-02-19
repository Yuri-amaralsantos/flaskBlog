<template>
    <div class="page">
        <h1>Editar Postagem</h1>
        <form class="form" @submit.prevent="updatePost">
            <label for="title">Título:</label>
            <input class="input" type="text" id="title" v-model="post.title" required />

            <label for="content">Conteúdo:</label>
            <textarea class="textarea" id="content" v-model="post.content" required></textarea>

            <button class="button" type="submit">Salvar Alterações</button>
        </form>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { fetchPostById, updatePostById } from '../../api';

const route = useRoute();
const router = useRouter();
const post = ref({ title: '', content: '' });
const errorMessage = ref('');

const loadPost = async () => {
    try {
        post.value = await fetchPostById(route.params.id);
    } catch (error) {
        errorMessage.value = 'Erro ao carregar post.';
    }
};

const updatePost = async () => {
    try {
        await updatePostById(route.params.id, post.value);
        router.push('/'); // Redirect after update
    } catch (error) {
        errorMessage.value = 'Erro ao atualizar post.';
    }
};

onMounted(loadPost);
</script>

<style scoped>
.form {
    display: flex;
    flex-direction: column;
    align-items: start;
}

.input,
.textarea {
    width: 90%;
    margin: 10px 0;
    border-radius: 10px;
}

.input {
    padding: 1rem 1rem;
}

.textarea {
    padding: 1rem 1rem;
    min-height: 200px;
}

.button {
    padding: 8px 16px;
    border: 1px solid black;
    border-radius: 10px;
    cursor: pointer;
}

.error {
    color: red;
}
</style>
