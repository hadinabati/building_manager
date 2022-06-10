<template>
  <div class="row">
    <div class="col-5">
      <q-card class="my-card bg-cyan-1">
        <h5>ایجاد هزینه</h5>
        <q-input dense standout rounded class="text" label="نام هزینه"></q-input>
        <q-select v-model="model" class="text2" :options="options" label="پرداخت کننده هزینه"/>
        <q-select v-model="model" class="text2" :options="options" label="براساس"/>
        <q-btn rounded color="indigo-13" class="buttons" dense label="ایجاد هزینه"></q-btn>
      </q-card>
    </div>
    <div class="col-1"></div>
    <div class="col-5" >
      <q-card class="my-card ">
        <h5>ایجاد صورتحساب</h5>
        <q-input dense standout rounded class="text" label="نام ماه"></q-input>
        <div>
          <q-input dense standout rounded class="text" label="تاریخ"></q-input>
          <q-popup-edit>
            <template v-slot="scope">
              <q-date minimal
                      v-model="date"
                      color="purple-8"
                      :locale="{daysShort  :['1','2','3','4 ','5','جمعه','شنبه'],
                months:['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']}"
                      calendar="persian">
                <q-btn label="انتخاب" @click="chose_date"></q-btn>
              </q-date>
            </template>
          </q-popup-edit>
        </div>

        <q-input dense standout rounded class="text" label="توضیحات"></q-input>
        <div>
          <q-btn color="pink-5" rounded class="buttons" label="ثبت اولیه "></q-btn>
        </div>

      </q-card>
    </div>
  </div>
  <q-dialog v-model="icon" style="width: auto">
    <q-card style="">
      <q-card-section class="row items-center q-pb-none">
        <q-space/>
        <q-btn icon="close" flat round dense v-close-popup/>
      </q-card-section>
      <div class="row">
        <q-select v-model="model" class="text2" :options="options" label="Standard"/>
        <q-input class="text2" label="مبلغ هزینه"></q-input>
        <q-input class="text2" label="توضیحات مربوطه"></q-input>
        <q-btn rounded class="text2" label="انتخاب" color="light-green-10"></q-btn>
      </div>
      <q-card-section>
      </q-card-section>
    </q-card>
  </q-dialog>
  <hr style="margin: 2rem">
  <div class="row">
    <q-btn color="blue-grey-8" rounded @click="icon = true" class="content-end" style="display: block ; width: 25% ; margin-right: 70% ; margin-left: 5%" label="اضافه کردن هزینه"></q-btn>
  </div>
  <div class="row">
    <q-input readonly standout style="display: block ; margin-top: 1rem ; width: 25% ; margin-right: 70% ; margin-left: 5%"  label="مبلغ کل فاکتور ایجاد شده"></q-input>
  </div>
  <div class="row">
    <q-table
      class="table"
      title="Treats"
      :rows="rows"
      :columns="columns"
      row-key="name"
    />
  </div>
</template>


<script>
import {ref} from 'vue'

export default {
  name: "out_money",
  data() {
    return {
      date: ref(''),
      icon: ref(false),
      bar: ref(false),
      bar2: ref(false),
      toolbar: ref(false)
    }
  },

  methods: {
    chose_date() {
      alert(this.date)
    }
  }
}
</script>


<style scoped>
.my-card {
  margin: 3rem 1rem 3rem 1rem;
}


.table{
  width: 60%;
  margin-top: 2rem;
  margin-right: 20%;
  margin-left: 20%;
  font-family: myvazir;
}
.text {
  font-family: myvazir;
  margin-top: 1rem;
  width: 80%;
  margin-right: 10%;
  margin-bottom: 1rem;
}

h5 {
  text-align: center;
  font-family: myyekan;
  margin-top: 1rem;
  padding-top: 2rem;
}

.buttons {
  margin-top: 1rem;
  margin-bottom: 1rem;
  width: 80%;
  margin-right: 10%;
}

.text2 {
  text-align: center;
  display: block;
  width: 70%;
  margin-right: 15%;
  margin-left: 15%;
  margin-top: 1rem;
}
</style>
