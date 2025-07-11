<template>
  <v-app>
    <!-- Главное меню -->
    <v-app-bar app color="primary" dark elevation="4">
      <v-container class="py-0">
        <v-row align="center" no-gutters>
          <v-col cols="auto">
            <v-toolbar-title class="text-h4 font-weight-light d-flex align-center">
              <v-btn text to="/" class="text-h4 font-weight-light pa-0">
                <v-icon large class="mr-2">mdi-notebook</v-icon>
                Мой блог
              </v-btn>
            </v-toolbar-title>
          </v-col>
          
          <v-col cols="auto" class="ml-auto">
            <v-btn text to="/" class="text-capitalize mx-2">
              <v-icon left>mdi-home</v-icon>
              Главная
            </v-btn>
            <v-btn text class="text-capitalize mx-2">
              <v-icon left>mdi-archive</v-icon>
              Архив
            </v-btn>
            <v-btn text class="text-capitalize mx-2">
              <v-icon left>mdi-information</v-icon>
              О блоге
            </v-btn>
          </v-col>

          <v-col cols="auto" class="ml-4">
            <v-btn icon>
              <v-icon>mdi-brightness-6</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>

    <!-- Основной контент -->
    <v-main>
      <v-container class="py-0" fluid>
        <v-row no-gutters>
          <!-- Боковое меню -->
          <v-col cols="12" md="3" lg="2" class="hidden-sm-and-down">
            <v-card flat class="transparent">
              <v-list rounded class="mt-4">
                <v-list-item-group color="primary">
                  <v-list-item to="/">
                    <v-list-item-icon>
                      <v-icon>mdi-home</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title>Главная</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>

                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon>mdi-archive</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title>Архив</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>

                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon>mdi-tag</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title>Категории</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-card>
          </v-col>

          <!-- Основной контент -->
          <v-col cols="12" md="9" lg="10" class="grey lighten-5">
            <v-fade-transition mode="out-in">
              <router-view></router-view>
            </v-fade-transition>
          </v-col>
        </v-row>
      </v-container>
    </v-main>

    <!-- Подвал -->
    <v-footer app color="primary" dark padless>
      <v-container>
        <v-row class="py-4">
          <!-- Информация о блоге -->
          <v-col cols="12" md="4" class="text-center text-md-left">
            <div class="text-h6 font-weight-light mb-2">Мой блог</div>
            <div class="text-body-2">Личный блог о веб-разработке и технологиях</div>
          </v-col>

          <!-- Навигация -->
          <v-col cols="12" md="4" class="text-center">
            <div class="text-subtitle-1 mb-2">Навигация</div>
            <v-btn text small class="mx-2">Главная</v-btn>
            <v-btn text small class="mx-2">Архив</v-btn>
            <v-btn text small class="mx-2">О блоге</v-btn>
          </v-col>

          <!-- Копирайт -->
          <v-col cols="12" md="4" class="text-center text-md-right">
            <div class="text-subtitle-1">
              {{ new Date().getFullYear() }} — <strong>Мой блог</strong>
            </div>
            <div class="text-caption mt-1 grey--text text--lighten-1">
              Создано с <v-icon small color="red lighten-1">mdi-heart</v-icon> и Vue.js
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    darkMode: false
  })
}
</script>

<style>
.v-application {
  font-family: 'Roboto', sans-serif;
}

.v-btn.text-h4 {
  text-transform: none !important;
  letter-spacing: normal !important;
}

.v-main {
  background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%);
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .2s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.v-card {
  border-radius: 12px !important;
}

.v-btn {
  letter-spacing: 0.5px;
}

.v-footer {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.v-list {
  background: transparent !important;
}

.v-list-item {
  border-radius: 8px !important;
  margin: 4px 0;
}

.transparent {
  background-color: transparent !important;
}
</style> 