<template>
  <div>
    <v-container class="py-8">
      <v-row>
        <v-col cols="12">
          <v-btn
            text
            color="primary"
            to="/"
            class="mb-8 text-capitalize"
            elevation="2"
          >
            <v-icon left>mdi-arrow-left</v-icon>
            Назад к списку
          </v-btn>
        </v-col>
      </v-row>

      <v-row v-if="loading" justify="center" align="center" style="min-height: 400px;">
        <v-col cols="auto">
          <v-progress-circular
            indeterminate
            color="primary"
            size="64"
          >
            <span class="caption">Загрузка...</span>
          </v-progress-circular>
        </v-col>
      </v-row>

      <template v-else-if="post">
        <v-row>
          <v-col cols="12" lg="8" class="mx-auto">
            <v-card class="mb-6" elevation="3">
              <v-img
                height="200"
                :src="getHeaderImage()"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                class="white--text align-end"
              >
                <v-card-title class="text-h3 font-weight-light pb-4 px-6">
                  {{ post.title }}
                </v-card-title>
              </v-img>

              <v-card-subtitle class="pt-4 pb-2">
                <v-chip
                  outlined
                  color="primary"
                  class="mr-2"
                >
                  <v-icon left small>mdi-calendar</v-icon>
                  {{ formatDate(post.published_date) }}
                </v-chip>
                <v-chip
                  outlined
                  small
                >
                  <v-icon left small>mdi-clock-outline</v-icon>
                  {{ getReadingTime() }} мин. чтения
                </v-chip>
              </v-card-subtitle>

              <v-divider class="mx-4"></v-divider>

              <v-card-text class="pa-6">
                <div class="text-body-1 post-content">{{ post.content }}</div>
              </v-card-text>

              <v-divider class="mx-4"></v-divider>

              <v-card-actions class="pa-4">
                <v-spacer></v-spacer>
                <v-btn
                  text
                  color="primary"
                  @click="sharePost"
                  class="text-capitalize"
                >
                  <v-icon left>mdi-share-variant</v-icon>
                  Поделиться
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </template>

      <v-row v-else justify="center">
        <v-col cols="12" sm="8" md="6" class="mx-auto">
          <v-card
            class="text-center pa-6"
            elevation="3"
          >
            <v-icon
              color="error"
              size="64"
              class="mb-4"
            >
              mdi-alert-circle
            </v-icon>
            <h2 class="text-h5 font-weight-regular mb-2">
              Пост не найден
            </h2>
            <p class="text-body-1 grey--text mb-4">
              Возможно, он был удален или перемещен.
            </p>
            <v-btn
              color="primary"
              to="/"
              class="text-capitalize"
            >
              <v-icon left>mdi-home</v-icon>
              Вернуться на главную
            </v-btn>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PostDetail',
  props: {
    id: {
      type: [String, Number],
      required: true
    }
  },
  data() {
    return {
      post: null,
      loading: false
    }
  },
  methods: {
    async fetchPost() {
      this.loading = true
      try {
        const response = await axios.get(`/api/posts/${this.id}/`)
        this.post = response.data
      } catch (error) {
        console.error('Error fetching post:', error)
        this.post = null
      } finally {
        setTimeout(() => {
          this.loading = false
        }, 500)
      }
    },
    formatDate(date) {
      return new Date(date).toLocaleString('ru-RU', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    },
    getReadingTime() {
      if (!this.post?.content) return 1
      const words = this.post.content.trim().split(/\s+/).length
      return Math.max(1, Math.ceil(words / 200))
    },
    getHeaderImage() {
      // Можно добавить логику выбора изображения на основе содержимого поста
      return 'https://picsum.photos/1920/1080?random'
    },
    sharePost() {
      if (navigator.share) {
        navigator.share({
          title: this.post.title,
          text: this.post.content.substring(0, 100) + '...',
          url: window.location.href
        })
      }
    }
  },
  created() {
    this.fetchPost()
  }
}
</script>

<style scoped>
.v-card {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border-radius: 12px;
  overflow: hidden;
}

.post-content {
  line-height: 1.8;
  white-space: pre-line;
}

.v-card__title {
  text-shadow: 0 2px 4px rgba(0,0,0,0.4);
}

.v-progress-circular {
  position: relative;
}

.v-progress-circular span {
  position: absolute;
  width: 100%;
  text-align: center;
  color: var(--v-primary-base);
}
</style> 