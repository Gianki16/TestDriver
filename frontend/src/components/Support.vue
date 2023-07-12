<template>
    <div>
      <h1>Soporte</h1>
      <form @submit.prevent="postComment">
        <label for="comment">Comentario:</label>
        <textarea id="comment" v-model="comment" required></textarea>
  
        <button type="submit">Publicar comentario</button>
      </form>
  
      <div v-for="comment in comments" :key="comment.id">
        <p>{{ comment.text }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SupportComponent',
    data() {
      return {
        comment: '',
        comments: []
      }
    },
    methods: {
      async postComment() {
        // Aquí deberías hacer una llamada a tu API para publicar un nuevo comentario.
        // Esto probablemente implicará enviar una solicitud POST a una ruta de tu API de Flask con el texto del comentario.
        // Si la solicitud es exitosa, podrías añadir el nuevo comentario a la lista de comentarios para que se muestre en la página.
      }
    },
    async created() {
      // Aquí deberías hacer una llamada a tu API para obtener todos los comentarios.
      // Esto probablemente implicará enviar una solicitud GET a una ruta de tu API de Flask.
      // Si la solicitud es exitosa, deberías guardar los comentarios en la data de tu componente para que se muestren en la página.
    }
  }
  </script>
  
  <style scoped>
  /* Aquí puedes añadir tus estilos CSS para la página de soporte. */
  </style>
  