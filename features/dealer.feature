Feature: El crupier para el juego del 21
Scenario: Cartas iniciales del crupier
  Given un crupier
  When comienza la ronda
  Then el crupier toma dos cartas

Scenario: total de la mano
  Given una <mano>
  When el crupier suma las cartas
  Then el <total> es correcto
