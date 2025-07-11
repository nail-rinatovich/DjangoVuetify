<template>
  <div>
    <v-container class="py-4">
      <!-- Заголовок -->
      <v-row>
        <v-col cols="12">
          <v-card color="primary" dark elevation="6" class="mb-6">
            <v-card-title class="d-flex flex-wrap align-center py-4">
              <div class="text-h4 font-weight-light">
                <v-icon large class="mr-2">mdi-post</v-icon>
                Последние посты
              </div>
              <v-spacer></v-spacer>
              <v-scale-transition>
                <v-progress-circular
                  v-if="loading"
                  indeterminate
                  color="white"
                  size="24"
                ></v-progress-circular>
              </v-scale-transition>
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>

      <!-- Сетка постов -->
      <v-row>
        <v-col v-for="post in posts" :key="post.id" cols="12" sm="6" lg="4">
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 8 : 2"
              :class="{ 'on-hover': hover }"
              class="mx-auto transition-swing fill-height post-card"
            >
              <v-img
                height="200"
                :src="getRandomImage()"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.6)"
              >
                <v-card-title class="text-h5">{{ post.title }}</v-card-title>
              </v-img>

              <v-card-text class="pt-4">
                <div class="text-truncate-3-lines grey--text text--darken-1">
                  {{ post.content }}
                </div>
              </v-card-text>

              <v-divider class="mx-4"></v-divider>

              <v-card-actions class="pa-4">
                <v-btn
                  text
                  color="primary"
                  :to="{ name: 'PostDetail', params: { id: post.id }}"
                  class="text-capitalize px-0"
                >
                  <v-icon left>mdi-book-open-page-variant</v-icon>
                  Читать
                </v-btn>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <v-chip
                      small
                      outlined
                      color="primary"
                      v-bind="attrs"
                      v-on="on"
                    >
                      <v-icon left small>mdi-calendar</v-icon>
                      {{ formatDate(post.published_date) }}
                    </v-chip>
                  </template>
                  <span>Дата публикации</span>
                </v-tooltip>
              </v-card-actions>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>

      <!-- Сообщение об отсутствии постов -->
      <v-row v-if="posts.length === 0 && !loading" class="mt-6">
        <v-col cols="12" sm="8" md="6" class="mx-auto">
          <v-card class="text-center pa-6" elevation="2">
            <v-icon color="primary" size="64" class="mb-4">mdi-post-outline</v-icon>
            <h2 class="text-h5 font-weight-regular mb-2">
              Пока нет опубликованных постов
            </h2>
            <p class="text-body-1 grey--text mb-0">
              Загляните позже, скоро здесь появится интересный контент!
            </p>
          </v-card>
        </v-col>
      </v-row>

      <!-- Пагинация -->
      <v-row v-if="totalPages > 1" class="mt-6">
        <v-col cols="12" class="text-center">
          <v-pagination
            v-model="currentPage"
            :length="totalPages"
            :total-visible="7"
            circle
            color="primary"
          ></v-pagination>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PostList',
  data() {
    return {
      posts: [],
      currentPage: 1,
      totalPages: 1,
      loading: false
    }
  },
  methods: {
    async fetchPosts() {
      this.loading = true
      try {
        console.log('Fetching posts from:', `/api/posts/?page=${this.currentPage}`)
        const response = await axios.get(`/api/posts/?page=${this.currentPage}`)
        console.log('API Response:', response.data)
        this.posts = response.data.results
        this.totalPages = Math.ceil(response.data.count / 10)
      } catch (error) {
        console.error('Error fetching posts:', error)
        console.error('Error details:', {
          message: error.message,
          response: error.response ? {
            status: error.response.status,
            data: error.response.data
          } : 'No response',
          config: {
            url: error.config.url,
            method: error.config.method,
            baseURL: error.config.baseURL
          }
        })
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
        year: 'numeric'
      })
    },
    getRandomImage() {
      return `https://picsum.photos/500/300?random=${Math.random()}`
    }
  },
  watch: {
    currentPage() {
      this.fetchPosts()
    }
  },
  created() {
    this.fetchPosts()
  }
}
</script>

<style scoped>
.text-truncate-3-lines {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.6;
}

.post-card {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border-radius: 12px;
}

.on-hover {
  transform: translateY(-8px);
}

.v-card__title {
  word-break: break-word;
  line-height: 1.4;
  text-shadow: 0 2px 4px rgba(0,0,0,0.4);
}

.v-pagination >>> .v-pagination__item {
  box-shadow: none;
}

.v-card {
  overflow: hidden;
}
</style> 