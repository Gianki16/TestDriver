<template>
    <nav style="display: flex; justify-content: space-between; align-items: center; padding: 1em; background-color: #f8f9fa;">
      <router-link to="/" style="font-size: 1.5em; font-weight: bold;">TestDriver</router-link>
      <ul style="display: flex; gap: 1em; list-style-type: none; margin: 0; padding: 0;">
        <li><router-link to="/login">Iniciar sesión</router-link></li>
        <li><router-link to="/register">Registrarse</router-link></li>
        <li><router-link to="/support">Soporte</router-link></li>
        <li><router-link to="/results">Resultados</router-link></li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'NavbarView',
  }
  </script>
  
  <style scoped>
  /* Aquí puedes añadir tus estilos CSS para el navbar. */
  </style>
  