<template>
  <div class="cart">
    <div class="cart__head">
      <div class="cart__close"></div>
      <h2 class="cart__title">Корзина</h2>
    </div>
    <div class="cart__content"></div>
    <div class="cart__pay">
      <div class="cart__total">1000 ₽</div>
      <div class="cart__button">Оплатить</div>
    </div>
  </div>
</template>

<style scoped>
.cart {
  display: none;
  z-index: 10;
  position: fixed;
  bottom: 0;
  height: 100vh;
  width: 100%;
  background: #fff;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border: 1px solid var(--color-background-mute);
}
.cart__close {
  margin: 15px auto;
  width: 100px;
  height: 2px;
  background: #959595;
}
</style>
