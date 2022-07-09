<template>
  <div class="row">
    <div class="col-md-3 col-xs-12">
      <div class="q-pa-md row items-start q-gutter-md">
        <q-card class="my-card bg-green-2 box_one" square bordered>
          <q-card-section style="height: 100%">
            <div class="absolute-top">
              <div class="row" style="height: 45% ; margin-top: 5%">
                <p class="col-6 text-center ps">تعداد ساختمان</p>
                <div class="col-6">
                </div>
              </div>
            </div>
            <div class="absolute-bottom">
              <div class="row" style="height: 40% ; margin-top: 5% ; margin-bottom: 5% ">
                <div  class="col-6 text-center">
                  <q-icon name="home" size="5rem" style="height: 100px ; margin-top: 5rem; color: #054a08"></q-icon>
                </div>
                <div class="col-6">
                  <h4 style="margin-top: 6rem; text-align: center">6</h4>
                </div>

              </div>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
    <div class="col-md-3 col-xs-12">
      <div class="q-pa-md row items-start q-gutter-md">
        <q-card class="my-card bg-indigo-2 box_two" square>
          <q-card-section style="height: 100%">
            <div class="absolute-top">
              <div class="row" style="height: 45% ; margin-top: 5%">
                <p class="col-6 text-center">تعداد آپارتمان</p>
                <div class="col-6">
                </div>
              </div>
            </div>
            <div class="absolute-bottom">
              <div class="row" style="height: 40% ; margin-top: 5% ; margin-bottom: 5% ">
                <div  class="col-6 text-center">
                  <q-icon name="apartment" size="5rem" style="height: 100px ; margin-top: 5rem; color: #0c059e"></q-icon>
                </div>
                <div class="col-6">
                  <h4 style="margin-top: 6rem; text-align: center">6</h4>
                </div>

              </div>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
    <div class="col-md-3 col-xs-12">
      <div class="q-pa-md row items-start q-gutter-md">
        <q-card class="my-card bg-amber-3 box_three" square bordered>
          <q-card-section style="height: 100%">
            <div class="absolute-top">
              <div class="row" style="height: 45% ; margin-top: 5%">
                <p class="col-6 text-center">تعداد ساختمان</p>
                <div class="col-6">
                </div>
              </div>
            </div>
            <div class="absolute-bottom">
              <div class="row" style="height: 40% ; margin-top: 5% ; margin-bottom: 5% ">
                <div  class="col-6 text-center">
                  <q-icon name="sell" size="5rem" style="height: 100px ; margin-top: 5rem; color: #9e9105"></q-icon>
                </div>
                <div class="col-6">
                  <h4 style="margin-top: 6rem; text-align: center">6</h4>
                </div>

              </div>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
    <div class="col-md-3 col-xs-12">
      <div class="q-pa-md row items-start q-gutter-md">
        <q-card  class="my-card bg-pink-2 box_one" square bordered>
          <q-card-section style="height: 100%">
            <div class="absolute-top">
              <div class="row" style="height: 45% ; margin-top: 5%">
                <p class="col-6 text-center ps">تعداد ساختمان</p>
                <div class="col-6">
                </div>
              </div>
            </div>
            <div class="absolute-bottom">
              <div class="row" style="height: 40% ; margin-top: 5% ; margin-bottom: 5% ">
                <div  class="col-6 text-center">
                  <q-icon name="home" size="5rem" style="height: 100px ; margin-top: 5rem; color: #970748"></q-icon>
                </div>
                <div class="col-6">
                  <h4 style="margin-top: 6rem; text-align: center">6</h4>
                </div>

              </div>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </div>

  <q-separator></q-separator>
  <div class="row">
    <div class="col-4">
      <q-select  label="انتخاب ساختمان" class="text" model-value="" bg-color="grey-1" rounded outlined dense standout style="margin-top: 2rem ; margin-right: 1rem"></q-select>
    </div>
    <div class="col-4">
      <q-select :options="chart" option-label="value" option-value="id"  label="انتخاب نمودار" class="text" model-value="" bg-color="grey-1" rounded outlined dense standout style="margin-top: 2rem ; margin-right: 1rem"></q-select>
    </div>
    <div class="col-4">
      <q-btn label="اعمال"  dense rounded class="bg-deep-purple-8 text" style="margin-top: 2rem ; margin-right: 1rem ; width: 80%" text-color="white"></q-btn>
    </div>
  </div>
  <q-separator  style="margin-top: 2rem"></q-separator>
  <div class="row">
    <h1>chart</h1>
  </div>

</template>

<script>
import {reactive} from "vue";

export default {
  name: "info",
  data(){
    const chart = reactive([
      {value :'باقی مانده سود ها' , id:0}, {value :'وضعیت بدهی ها' , id:1}, {value :'وضعیت پرداختی های ماه' , id:2}
    ])
    return{
      chart,
    }
  }

}
</script>

<style scoped>
.my-card {
  height: 200px;
  width: 100%;
}
.text{
  font-family: mytanha;
}
p{
  font-family: mytanha;
  margin-bottom: 1rem;
}
.box_one {
  border: 0px solid #074605;
}
.box_two {
  border: 0px solid #336582;
}
.box_three {
  border: 0px solid #625908;
}
</style>
