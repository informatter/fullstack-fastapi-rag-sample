<template>
  <VBtn variant="outlined" color="secondary" @click="handleLogout"> Log Out </VBtn>
</template>

<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'

const { logout } = useAuth0()

const handleLogout = () =>
  logout({
    logoutParams: {
      returnTo: window.location.origin
    }
  })
</script>
