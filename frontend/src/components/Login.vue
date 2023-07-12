<template>
    <div>
      <h1>Iniciar sesión</h1>
      <form @submit.prevent="login">
        <label for="username">Usuario:</label>
        <input id="username" v-model="username" type="text" required>
  
        <label for="password">Contraseña:</label>
        <input id="password" v-model="password" type="password" required>
  
        <button type="submit">Iniciar sesión</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginComponent',
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      async login() {
        // Aquí deberías hacer una llamada a tu API para iniciar sesión.
        // Esto probablemente implicará enviar una solicitud POST a una ruta de tu API de Flask con el nombre de usuario y la contraseña.
        // Si la solicitud es exitosa, deberías guardar el token de autenticación en algún lugar (como en localStorage) y redirigir al usuario a la página principal.
      }
    }
  }
  </script>
  
  <style scoped>
  /* Aquí puedes añadir tus estilos CSS para la página de inicio de sesión. */
  </style>
  