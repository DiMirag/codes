// Функция для получения случайного времени задержки от 3 до 5 секунд
function getRandomDelay(min = 3000, max = 5000) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Функция для нажатия на кнопку с заданной задержкой
function clickButtonWithDelay() {
    // Найдём кнопку по селектору (замените на нужный вам селектор)
    const button = document.querySelector('.button-class');

    if (button) {
        // Получаем случайное время задержки
        const delay = getRandomDelay();

        console.log(`Нажатие будет выполнено через ${delay / 1000} секунд`);

        // Используем setTimeout для нажатия с задержкой
        setTimeout(() => {
            button.click();
            console.log('Кнопка нажата!');
        }, delay);
    } else {
        console.log('Кнопка не найдена!');
    }
}

// Запускаем функцию для нажатия с задержкой
clickButtonWithDelay();
