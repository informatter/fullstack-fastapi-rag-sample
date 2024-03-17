<template>
  <v-app-bar :color="color">
    <UserLogout v-if="isAuthenticated"></UserLogout>
  </v-app-bar>
</template>

<script setup lang="ts">
import UserLogout from './UserLogout.vue'
import { useAuth0 } from '@auth0/auth0-vue'
const { isAuthenticated } = useAuth0()

defineProps<{
  color: string
}>()
</script>
