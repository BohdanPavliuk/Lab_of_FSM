# Lab_of_FSM
My day in a way of FSM


Діаграма скінченно автомата - ![Станова діаграма](https://github.com/Vspotiv/Lab_of_FSM/assets/55399864/0d4fa911-cd3c-4c96-8d8d-5925e81da5e0)

Звідси видно, що у нас існує 7 станів між якими є переходити. Так все починається зі стану sleeping. В якому протягом 6-8 годин ранку може відбутись рандомна подія, яка є сном(dream).

Так для переходу між станами є 2 основні чинника. Перший і найважливіший - це час. В залежності від часу можуть відбуватись переходи з одного стану в інший і на екран буде виводить приблизний опис того, що відбулось. Іншим фактором є ймовірність. При однаковому часі з різною ймовірністю може відбуватись перехід до двох різних станів.

Так певні переходити між станами і відповідно події які ці стани ініціюють підвʼязане до рандому.

Єдина подія, яка не залежить від часу є smoking і вона може відбуватись лише, коли автомат у стані studying або wasting time
при запуску програми із затримкую в 1 секунду буде зʼявлятись інформація про поточну годину і події, що відбуваються

Приклад реалізації - <img width="335" alt="Screenshot 2023-05-23 at 22 35 34" src="https://github.com/Vspotiv/Lab_of_FSM/assets/55399864/252872f3-32b8-4117-963c-6515b7900f6c">
