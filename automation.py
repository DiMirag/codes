// Функция для получения случайной задержки в диапазоне от 5 до 8 секунд
function getRandomDelay(min = 5000, max = 8000) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Основная функция для выполнения последовательности действий
function automateActions(value) {
    // 1. Нажатие на первую кнопку с задержкой от 5 до 8 секунд
    setTimeout(() => {
        const firstButton = document.querySelector('.first-button-class');
        if (firstButton) {
            firstButton.click();
            console.log('Нажата первая кнопка.');

            // 2. Нажатие на вторую кнопку после первой
            setTimeout(() => {
                const secondButton = document.querySelector('.second-button-class');
                if (secondButton) {
                    secondButton.click();
                    console.log('Нажата вторая кнопка.');

                    // 3. Ввод значения и нажатие третьей кнопки
                    const inputField = document.querySelector('.input-class');
                    const thirdButton = document.querySelector('.third-button-class');
                    if (inputField && thirdButton) {
                        inputField.value = value;
                        inputField.dispatchEvent(new Event('input'));  // Генерация события ввода
                        thirdButton.click();
                        console.log(`Введено значение "${value}" и нажата третья кнопка.`);

                        // 4. Нажатие четвёртой кнопки
                        setTimeout(() => {
                            const fourthButton = document.querySelector('.fourth-button-class');
                            if (fourthButton) {
                                fourthButton.click();
                                console.log('Нажата четвёртая кнопка.');

                                // 5. Нажатие пятой кнопки
                                setTimeout(() => {
                                    const fifthButton = document.querySelector('.fifth-button-class');
                                    if (fifthButton) {
                                        fifthButton.click();
                                        console.log('Нажата пятая кнопка.');

                                        // 6. Задержка в 5 секунд перед нажатием шестой кнопки
                                        setTimeout(() => {
                                            const sixthButton = document.querySelector('.sixth-button-class');
                                            if (sixthButton) {
                                                sixthButton.click();
                                                console.log('Нажата шестая кнопка.');

                                                // Повторение цикла
                                                automateActions(value);
                                            } else {
                                                console.log('Шестая кнопка не найдена!');
                                            }
                                        }, 5000);  // Задержка 5 секунд
                                    } else {
                                        console.log('Пятая кнопка не найдена!');
                                    }
                                }, 0);  // Без задержки для пятой кнопки
                            } else {
                                console.log('Четвёртая кнопка не найдена!');
                            }
                        }, 0);  // Без задержки для четвёртой кнопки
                    } else {
                        console.log('Текстовое поле или третья кнопка не найдены!');
                    }
                } else {
                    console.log('Вторая кнопка не найдена!');
                }
            }, 0);  // Без задержки для второй кнопки
        } else {
            console.log('Первая кнопка не найдена!');
        }
    }, getRandomDelay());  // Задержка от 5 до 8 секунд
}

// Запуск скрипта с определённым значением для ввода
automateActions('Ваше значение');
