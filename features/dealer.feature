Feature: El crupier para el juego del 21
Scenario: Cartas iniciales del crupier
  Given un crupier
  When comienza la ronda
  Then el crupier toma dos cartas
