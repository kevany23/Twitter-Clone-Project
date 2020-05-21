<template>
<div>
  <b-card>
    <h3>{{username}}</h3>
    <p>{{timestamp}}</p>
    <p>
    {{content}}
    </p>
  </b-card>
</div>
</template>

<script>
/* eslint-disable */
export default {
  name: "Post",
  props: ['content', 'username', 'timestamp'],
  methods: {
  },
}
</script>

<style>
</style>