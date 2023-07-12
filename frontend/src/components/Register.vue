<template>
    <div>
      <h1>Registrarse</h1>
      <form @submit.prevent="register">
        <label for="username">Usuario:</label>
        <input id="username" v-model="username" type="text" required>
  
        <label for="password">Contraseña:</label>
        <input id="password" v-model="password" type="password" required>
  
        <button type="submit">Registrarse</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RegisterComponent',
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      async register() {
        // Aquí deberías hacer una llamada a tu API para registrar a un nuevo usuario.
        // Esto probablemente implicará enviar una solicitud POST a una ruta de tu API de Flask con el nombre de usuario y la contraseña.
        // Si la solicitud es exitosa, podrías redirigir al usuario a la página de inicio de sesión para que pueda iniciar sesión con su nueva cuenta.
      }
    }
  }
  </script>
  
  <style scoped>
  /* Aquí puedes añadir tus estilos CSS para la página de registro. */
  </style>
  