<template>
<div class="row">
  <q-input class="mySelect"  label="موجودی صندوق"  readonly standout rounded></q-input>
  <hr>
  <h5 style="text-align: center; font-family: myvazir ; width: 100%">لیست واحد های بدهکار</h5>
  <q-table
    style="margin-right: 5% ; margin-left: 5% ; margin-top: 2rem"
    class="table"
    dense
    title="Treats"
    :rows="rows"
    :columns="columns"
    row-key="name"
  />
</div>
</template>

<script>
export default {
  name: "sandbox"
}
</script>

<style scoped>
.mySelect{
  font-family: myvazir;
  width: 60%;
  margin-right: 20%;
  margin-left: 20%;
  margin-top: 2rem;
}
.table{
  width: 90%;
  margin-top: 2rem;
  margin-right: 5%;
  margin-left: 5%;
  font-family: myvazir;
}
</style>
