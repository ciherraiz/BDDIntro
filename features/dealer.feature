Feature: El crupier para el juego del 21
Scenario: Cartas iniciales del crupier
  Given un crupier
  When comienza la ronda
  Then el crupier toma dos cartas

Scenario Outline: total de la mano
  Given una <mano>
  When el crupier suma las cartas
  Then el <total> es correcto

  Examples: Manos
  | mano          | total |
  | 5,7           | 12    |
  | 5,Q           | 15    |
  | Q,Q,A         | 21    |
  | Q,A           | 21    |
  | A,A,A         | 13    |
