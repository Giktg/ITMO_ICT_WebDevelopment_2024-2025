<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const others = ref([]);

function find() {
  console.log(
    `/main/resident/${router.currentRoute.value.params.id}/other_residents/`
  );
  instance
    .get(
      `/main/resident/${router.currentRoute.value.params.id}/other_residents/`,
      {
        headers: {
          Authorization: `Bearer ${Token.token}`,
        },
      }
    )
    .then((response) => {
      if (response.status === 200) {
        console.log(response.data);
        others.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  find();
});
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Другие жильцы:</h2>
      <template v-for="resident in others" :key="resident.id">
        <v-card
          width="400"
          :title="`${resident.passport_number} живет в номере ${resident.apartment_number}`"
          :subtitle="`С ${resident.check_in} по ${resident.check_out}`"
          style="white-space: pre-line; text-align: center"
        >
        </v-card>
      </template>
      <v-btn @click="router.push('/residents/')">Назад</v-btn>
    </div>
  </v-app>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
