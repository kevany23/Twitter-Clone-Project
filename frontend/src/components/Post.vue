<template>
<div>
  <b-card>
    <h3>{{username}}</h3>
    <p>{{formatDate(timestamp)}}</p>
    <p>
    {{content}}
    </p>
    <b-button
    v-bind:style="likeButtonStyle"
    v-on:click="onLikeClick"
    >
      <b-icon-arrow-up class="h4 mb-0">
      </b-icon-arrow-up>
    </b-button>
  </b-card>
</div>
</template>

<script>
/* eslint-disable */
import formatPostDate from '../util/DateTime.js';
import { BootstrapVue, BIcon, BIconArrowUp } from 'bootstrap-vue';
export default {
  name: "Post",
  components: {
    BIconArrowUp,
  },
  props: ['id', 'content', 'username', 'timestamp', 'liked'],
  mounted() {
      this.buttonMode = this.liked;
      if (this.liked) {
        this.likeButtonStyle.backgroundColor = 'Gray';
      } else {
        this.likeButtonStyle.backgroundColor = 'DodgerBlue';
      }
  },
  data() {
    return {
      likeButtonStyle: {
        backgroundColor: 'DodgerBlue',
        buttonMode: false,
      }
    };
  },
  methods: {
    formatDate(timestamp) {
      return formatPostDate(timestamp);
    },
    onLikeClick() {
      this.buttonMode = ! this.buttonMode;
      if (this.buttonMode) {
        this.likeButtonStyle.backgroundColor = 'Gray';
        this.like();
      } else {
        this.likeButtonStyle.backgroundColor = 'DodgerBlue';
        this.unlike();
      }
    },
    like() {
      this.$emit('post-liked', this.id);
    },
    unlike() {
      this.$emit('post-unliked', this.id);
    },
  },
}
</script>

<style>
</style>