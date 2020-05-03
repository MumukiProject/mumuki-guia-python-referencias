def test_"objetos_equivalentes es una lista":
  expect(objetos_equivalentes.is_a? Array).to be True


def test_"objetos_equivalentes tiene tres elementos":
  expect(objetos_equivalentes.size).to eq 3


def test_"Todos los objetos de objetos_equivalentes son equivalentes":
  expect(objetos_equivalentes.all? { |objeto| objeto == objetos_equivalentes.first }).to be True


def test_"No todos los objetos de objetos_equivalentes son el mismo":
  expect(objetos_equivalentes.all? { |objeto| objeto.equal? objetos_equivalentes.first }).to be False
