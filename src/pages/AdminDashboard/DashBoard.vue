<template>
  <div class="row">
  <div class="col-4">
    <q-card class="my-card">
      <q-card-section>
        <h5>اطلاعات اولیه ساختمان</h5>
        <q-img class="q-img" src="../../pages/AdminDashboard/image/base.png"></q-img>
        <q-separator></q-separator>
        <q-btn color="pink-6" @click="routes('building_info')"  rounded  class="q-btn full-width" > ورود </q-btn>
      </q-card-section>
    </q-card>
  </div>
    <div class="col-4">
      <q-card class="my-card">
        <q-card-section>
          <h5>هزینه ها </h5>
          <q-img class="q-img" src="../../pages/AdminDashboard/image/money.jpg"></q-img>
          <q-separator></q-separator>
          <q-btn color="pink-6"  rounded  class="q-btn full-width" @click="routes('money')"> ورود </q-btn>
        </q-card-section>
      </q-card>
    </div>

    <div class="col-4">
      <q-card class="my-card">
        <q-card-section>
          <h5>شارژ</h5>
          <q-img class="q-img" src="../../pages/AdminDashboard/image/income.jpg"></q-img>
          <q-separator></q-separator>
          <q-btn color="pink-6" @click="routes('incoming') " rounded  class="q-btn full-width" > ورود </q-btn>
        </q-card-section>
      </q-card>
    </div>

    <div class="col-4">
      <q-card class="my-card">
        <q-card-section>
          <h5>صندوق</h5>
          <q-img class="q-img" src="../../pages/AdminDashboard/image/sandbox.jpg"></q-img>
          <q-separator></q-separator>
          <q-btn color="pink-6"  @click="routes('cash_box')" rounded  class="q-btn full-width" > ورود </q-btn>
        </q-card-section>
      </q-card>
    </div>


  </div>
</template>

<script>

export default {
  name: "DashBoard" ,
  methods:{
    routes(address){
      this.$router.push('/Dashboard/' + address)
    }
  }
}
</script>

<style scoped>
.my-card{
  margin: 3rem 1rem 1rem 1rem;
}
h5{
  font-family: myvazir;
  text-align: center;
}
.q-img{
  height: 250px;
  margin-top: 1rem ;
  margin-bottom: 1rem;
}
.q-btn{
  font-family: myyekan;
  margin-top: 1rem ;
  margin-bottom: 1rem;
}
</style>
