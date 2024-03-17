<script setup lang="ts">
import UserLogin from '@/components/UserLogin.vue'
import AppBar from '@/components/AppBar.vue'
</script>

<template>
  <v-layout>
    <AppBar color="accent"></AppBar>
    <v-main>
      <v-container fluid>
        <div class="welcome-text">
          <h1>Welcome to the sample RAG application!</h1>
          <UserLogin style="margin-top: 20px"> </UserLogin>
        </div>
      </v-container>
    </v-main>
  </v-layout>
</template>

<style scoped>
.welcome-text {
  text-align: center;
  margin-top: 20%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: auto;
}
</style>
