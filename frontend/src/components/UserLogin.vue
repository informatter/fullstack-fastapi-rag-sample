<template>
  <VBtn size="large" color="primary" @click="handleLogin"> Log In </VBtn>
</template>

<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'

const { loginWithRedirect } = useAuth0()

const handleLogin = () => {
  loginWithRedirect({
    appState: {
      target: '/app'
    }
  })
}
</script>
