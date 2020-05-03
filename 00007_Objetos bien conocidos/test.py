def test_"AbuelaClotilde alimenta a su nieto dos veces":
  AbuelaClotilde.alimentar_nieto
  expect(Fito.cantidad_de_llamadas).to eq 2
  Fito.volve_a_tu_felicidad!


def test_"Cuando AbuelaClotilde alimenta a su nieto su felicidad aumenta 3 puntos":
  AbuelaClotilde.alimentar_nieto
  expect(Fito.felicidad).to eq 103
