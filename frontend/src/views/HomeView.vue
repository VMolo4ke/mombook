<script setup>
import Item from '@/components/Item.vue'
</script>

<template>
  <div class="container">
    <header class="header">
      <input type="text" placeholder="Искать товар" class="header__input" />
      <div class="header__category">
        <div class="category__item">Книжки</div>
        <div class="category__item">Игрушка</div>
      </div>
    </header>
    <main class="main">
      <Item />
      <Item />
      <Item />
      <Item />
    </main>
  </div>
</template>

<style scoped>
.header {
  width: 95%;
  padding: 10px 0 0 0;
  margin: 0 auto 20px;
}
.header__input {
  width: 100%;
  height: 30px;
  background: var(--color-background-mute);
  padding: 0 0 0 10px;
  border-radius: 5px;
  border: none;
  outline: none;
  margin: 0 0 7px 0;
}
.header__input:hover {
  border: 1px solid var(--color-border-hover);
}
.header__category {
  display: flex;
  gap: 10px;
}
.category__item {
  background: var(--color-background-mute);
  padding: 5px 10px;
  border-radius: 10px;
  font-size: 12px;
}
.main {
  background: var(--color-background-mute);
  padding: 5px 0 0 0;
  display: grid;
  grid-template-columns: 1fr 1fr; /* Две колонки, каждая занимает 50% доступной ширины */
  gap: 10px;
}
</style>
