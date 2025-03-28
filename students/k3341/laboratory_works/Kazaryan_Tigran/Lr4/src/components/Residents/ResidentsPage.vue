<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  check_in: "",
  check_out: "",
  passport_number: "",
  apartment_number: "",
});

function getPaper() {
  instance
    .get(`/main/resident/${router.currentRoute.value.params.id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        form.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function savePaper() {
  const { id, ...rest } = form.value;
  instance
    .patch(`/main/resident/${router.currentRoute.value.params.id}/`, rest, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        router.push("/residents");
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getPaper();
});
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Изменить</h2>
      <v-text-field
        label="Номер паспорта гостя"
        v-model="form.passport_number"
      ></v-text-field>
      <v-text-field
        label="Номер апартаментов"
        v-model="form.apartment_number"
      ></v-text-field>
      <v-text-field
        label="Дата заселения"
        v-model="form.check_in"
      ></v-text-field>
      <v-text-field
        label="Дата выселения"
        v-model="form.check_out"
      ></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>
h2 {
  margin-top: 10%;
  margin-bottom: 5%;
}
</style>
