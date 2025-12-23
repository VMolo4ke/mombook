<template>
  <footer class="footer">
    <div class="footer__title">Контакты</div>
    <div class="footer__info">
      <a href="mailto:mombook.sup@gmail.com" class="footer__item">Почта: mombook.sup@gmail.com</a>
      <a href="tel:+79220545826" class="footer__item">Номер: +79220545826</a>
      <a href="https://t.me/Evgeniya_myagrushki" target="_blank" class="footer__item"
        >Телеграм: @Evgeniya_myagrushki</a
      >
      <a class="footer__item">ИНН: 722406951147</a>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  padding: 20px;
  width: 100%;
  background: #333;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.footer__title {
  color: #fff;
  font-size: 18px;
}
.footer__item {
  display: block;
  font-size: 14px;
  margin: 10px 0;
  color: #fff;
  text-decoration: none;
}
</style>
