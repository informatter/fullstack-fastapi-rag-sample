<template>
  <VBtn size="large" color="primary" @click="handleSignUp"> Sign Up </VBtn>
</template>

<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'

const { loginWithRedirect } = useAuth0()

const handleSignUp = () => {
  loginWithRedirect({
    appState: {
      target: '/app'
    },
    authorizationParams: {
      screen_hint: 'signup'
    }
  })
}
</script>
