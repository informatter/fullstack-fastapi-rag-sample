<script setup lang="ts">
import UserLogin from '@/components/UserLogin.vue';
</script>

<template>


    <div class="navbar">
      <v-icon size="x-large" color="secondary" icon="mdi-github"></v-icon>
      <VBtn color="secondary">GitHub</VBtn>
    </div>

  <main>
    <div class="welcome-text">
      <h1>
        Welcome to the sample RAG application!
      </h1>
      <UserLogin 
        style="margin-top: 20px;"
      >
      </UserLogin>
    </div>

  </main>
</template>

<style scoped>

.navbar {
  padding: 10px 20px;
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  /* background-color: var(--black); */
  box-shadow: rgb(90 95 102) 0-1.5px 0 inset;
}
.welcome-text {
  text-align: center;
  margin-top: 20%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: auto; /* Adjust as needed */
}
</style>
