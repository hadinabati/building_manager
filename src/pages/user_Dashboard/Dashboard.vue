<template>
  <div class="row">
    <div class="col-4">
      <q-card class="my_card">
        <h5>
          مشخصات واحد
        </h5>
        <q-input dense label="نام واحد" class="text" rounded standout readonly></q-input>
        <q-input dense label="متراژ واحد" class="text" rounded standout readonly></q-input>
        <q-input dense label="تعداد نفرات" class="text" rounded standout readonly></q-input>
        <q-input dense label="مجموع بدهی" class="text" rounded standout readonly></q-input>
        <hr>
        <q-input dense label="رمز عبور جدید" class="text" rounded standout></q-input>
        <q-btn class="btns" label="ثبت رمز عبور جدید"></q-btn>

      </q-card>
    </div>
    <div class="col-8">
      <div>

        <q-table
          class="tables"
          dense
          title="Treats"
          :rows="rows"
          :columns="columns"
          row-key="name"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard"
}
</script>

<style scoped>
.tables {
  margin-top: 9rem;
  margin-right: 5%;
  margin-left: 5%;
  width: 90%;
  font-family: myvazir;
}

h5 {
  font-family: mytanha;
  width: 100%;
  text-align: center;
  padding-top: 2rem;
}

.my_card {
  margin-right: 3rem;
  margin-top: 9rem;
}

.text {
  font-family: myvazir;
  margin-top: 1rem;
  width: 80%;
  margin-right: 10%;
  margin-left: 10%;
}

.btns {
  font-family: myyekan;
  width: 80%;
  margin-right: 10%;
  margin-top: 1rem;
  margin-bottom: 1rem;

}
</style>
